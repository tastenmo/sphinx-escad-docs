import os
import re
from typing import Any, Dict
import subprocess
import weasyprint

from collections import Counter

import sass

import logging
import logging.handlers

from bs4 import BeautifulSoup

from sphinx import __version__
from sphinx.application import Sphinx

from sphinx.builders.singlehtml import SingleFileHTMLBuilder

from sphinx_escaddocs.builders.debug import DebugPython

from sphinx.util import logging as sphinx_logging

from sphinx_escaddocs.writers.escaddocs import EscadDocsTranslator

logger = sphinx_logging.getLogger(__name__)

weasy_logger = weasyprint.LOGGER
weasy_logger.setLevel(logging.DEBUG)
weasy_logger.addHandler(sphinx_logging.NewLineStreamHandler())

weasy_progress_logger = weasyprint.PROGRESS_LOGGER
weasy_progress_logger.addHandler(sphinx_logging.NewLineStreamHandler())
#weasy_logger.addHandler(logging.StreamHandler())



class EscadDocsBuilder(SingleFileHTMLBuilder):
    name = "escaddocs"
    format = "html"  # Must be html instead of "pdf", otherwise plantuml has problems
    file_suffix = ".pdf"
    links_suffix = None

    default_translator_class = EscadDocsTranslator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.app.config.escaddocs_theme is not None:
            logger.info(f"Setting theme to {self.app.config.escaddocs_theme}")
            self.app.config.html_theme = self.app.config.escaddocs_theme

        # We need to overwrite some config values, as they are set for the normal html build, but
        # escaddocs can normally not handle them.
        self.app.config.html_sidebars = self.app.config.escaddocs_sidebars
        self.app.config.html_theme_options = self.app.config.escaddocs_theme_options
        # Sphinx would write warnings, if given options are unsupported.

        # Add escaddocs specific functions to the html_context. Mostly needed for printing debug information.
        self.app.config.html_context["escaddocs_debug"] = self.config["escaddocs_debug"]
        self.app.config.html_context["pyd"] = DebugPython()

        debug_sphinx = {
            "version": __version__,
            "confidr": self.app.confdir,
            "srcdir": self.app.srcdir,
            "outdir": self.app.outdir,
            "extensions": self.app.config.extensions,
            "simple_config": {x.name: x.value for x in self.app.config if x.name.startswith("escaddocs")},
        }
        self.app.config.html_context["spd"] = debug_sphinx

        # Generate main.css
        logger.info("Generating css files from scss-templates")
        css_folder = os.path.join(self.app.outdir, f"_static")
        scss_folder = os.path.join(
            os.path.dirname(__file__), "..", "themes", "escaddocs_theme", "static", "styles", "sources"
        )
        sass.compile(
            dirname=(scss_folder, css_folder),
            output_style="nested",
            custom_functions={
                sass.SassFunction("config", ("$a", "$b"), self.get_config_var),
                sass.SassFunction("theme_option", ("$a", "$b"), self.get_theme_option_var),
            },
        )

    def get_config_var(self, name, default):
        """
        Gets a config variables for scss out of the Sphinx configuration.
        If name is not found in config, the specified default var is returned.

        Args:
            name: Name of the config var to use
            default: Default value, if name can not be found in config

        Returns: Value
        """
        escaddocs_vars = self.app.config.escaddocs_vars
        if name not in escaddocs_vars:
            return default
        return escaddocs_vars[name]

    def get_theme_option_var(self, name, default):
        """
        Gets a option  variables for scss out of the Sphinx theme options.
        If name is not found in theme options, the specified default var is returned.

        Args:
            name: Name of the option var to use
            default: Default value, if name can not be found in config

        Returns: Value
        """
        escaddocs_theme_options = self.app.config.escaddocs_theme_options
        if name not in escaddocs_theme_options:
            return default
        return escaddocs_theme_options[name]

    def finish(self) -> None:
        super().finish()

        index_path = os.path.join(self.app.outdir, f"{self.app.config.root_doc}.html")

        # Manipulate index.html
        with open(index_path, "rt", encoding="utf-8") as index_file:
            index_html = "".join(index_file.readlines())

        new_index_html = self._toctree_fix(index_html)

        with open(index_path, "wt", encoding="utf-8") as index_file:
            index_file.writelines(new_index_html)

        args = ["weasyprint"]

        if isinstance(self.config["escaddocs_weasyprint_flags"], list) and (
            0 < len(self.config["escaddocs_weasyprint_flags"])
        ):
            args.extend(self.config["escaddocs_weasyprint_flags"])

        file_name = self.app.config.escaddocs_file_name or f"{self.app.config.project}.pdf"

        args.extend(
            [
                index_path,
                os.path.join(self.app.outdir, f"{file_name}"),
            ]
        )

        timeout = self.config["escaddocs_weasyprint_timeout"]

        filter_list = self.config["escaddocs_weasyprint_filter"]
        filter_pattern = "(?:% s)" % "|".join(filter_list) if 0 < len(filter_list) else None

        if self.config["escaddocs_use_weasyprint_api"]:
            logger.info("Using weasyprint API")
            doc = weasyprint.HTML(index_path)

            doc.write_pdf(
                target=os.path.join(self.app.outdir, f"{file_name}"),
            )

        else:
            retries = self.config["escaddocs_weasyprint_retries"]
            success = False
            for n in range(1 + retries):
                try:
                    wp_out = subprocess.check_output(args, timeout=timeout, text=True, stderr=subprocess.STDOUT)

                    for line in wp_out.splitlines():
                        if filter_pattern is not None and re.match(filter_pattern, line):
                            pass
                        else:
                            print(line)
                    success = True
                    break
                except subprocess.TimeoutExpired:
                    logger.warning(f"TimeoutExpired in weasyprint, retrying")
                except subprocess.CalledProcessError as e:
                    logger.warning(f"CalledProcessError in weasyprint, retrying\n{str(e)}")
                finally:
                    if (n == retries - 1) and not success:
                        raise RuntimeError(f"maximum number of retries {retries} failed in weasyprint")

    def _toctree_fix(self, html):
        soup = BeautifulSoup(html, "html.parser")
        sidebar = soup.find("div", class_="sphinxsidebarwrapper")

        if sidebar is not None:
            links = sidebar.find_all("a", class_="reference internal")
            for link in links:
                link["href"] = link["href"].replace(f"{self.app.config.root_doc}.html", "")
                
            # search for duplicates
            counts = dict(Counter([str(x).split(">")[0] for x in links]))
            duplicates = {key: value for key, value in counts.items() if value > 1}

            if duplicates:
                print("found duplicate references in toctree attempting to fix")

            for text, counter in duplicates.items():

                ref = re.findall("href=\"#.*\"", str(text))

                # clean href data for searching
                cleaned_ref_toc = ref[0].replace("href=\"", "").replace("\"", "") # "#target"
                cleaned_ref_target = ref[0].replace("href=\"#", "").replace("\"", "") # "target"

                occurences = soup.find_all('section', attrs={"id": cleaned_ref_target})

                # rename duplicate references, relies on fact -> order in toc is order of occurence in document
                replace_counter = 0

                for link in links:
                    if link["href"] == cleaned_ref_toc:
                        # edit reference in table of content
                        link["href"] = link["href"] + "-" + str(replace_counter + 1)

                        # edit target reference
                        occurences[replace_counter]["id"] = occurences[replace_counter]["id"] + "-" + str(
                            replace_counter + 1)

                        replace_counter += 1

        for heading_tag in ["h1", "h2"]:
            headings = soup.find_all(heading_tag, class_="")
            for number, heading in enumerate(headings):
                class_attr = heading.attrs["class"] if heading.has_attr("class") else []
                logger.debug(f"found heading {heading}")
                if 0 == number:
                    class_attr.append("first")
                if 0 == number % 2:
                    class_attr.append("even")
                else:
                    class_attr.append("odd")
                if len(headings) - 1 == number:
                    class_attr.append("last")

                heading.attrs["class"] = class_attr

        return soup.prettify(formatter="html")

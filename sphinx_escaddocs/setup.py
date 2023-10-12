import json
import os
from pathlib import Path
from typing import Any, Dict, List

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.environment import BuildEnvironment
from sphinx.errors import SphinxError

from sphinx_escaddocs.builders.escaddocs import EscadDocsBuilder

from sphinx_escaddocs.directives.ifbuilder import IfBuilderDirective
from sphinx_escaddocs.directives.ifinclude import IfIncludeDirective
from sphinx_escaddocs.directives.pdfinclude import PdfIncludeDirective


def setup(app: Sphinx) -> Dict[str, Any]:

    app.add_config_value("escaddocs_vars", {}, "html", types=[dict])
    app.add_config_value("escaddocs_file_name", None, "html", types=[str])
    app.add_config_value("escaddocs_debug", False, "html", types=bool)
    app.add_config_value("escaddocs_weasyprint_timeout", None, "html", types=[int])
    app.add_config_value("escaddocs_weasyprint_retries", 0, "html", types=[int])
    app.add_config_value("escaddocs_weasyprint_flags", None, "html", types=[list])
    app.add_config_value("escaddocs_weasyprint_filter", [], "html", types=[list])
    app.add_config_value("escaddocs_use_weasyprint_api", None, "html", types=[bool])
    app.add_config_value("escaddocs_theme", "escaddocs_theme", "html", types=[str])
    app.add_config_value("escaddocs_theme_options", {}, "html", types=[dict])
    app.add_config_value("escaddocs_sidebars", {"**": ["localtoc.html"]}, "html", types=[dict])

    app.add_builder(EscadDocsBuilder)

    app.add_directive('if-builder', IfBuilderDirective)
    app.add_directive('if-include', IfIncludeDirective)
    app.add_directive('pdf-include', PdfIncludeDirective)

    here = Path(__file__).parent.resolve()
    escaddocs_theme_path = here / "themes" / "escaddocs_theme"

    app.add_html_theme("escaddocs_theme", str(escaddocs_theme_path))

    #app.add_html_theme('escaddocs_theme', path.abspath(path.dirname(__file__)))


    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

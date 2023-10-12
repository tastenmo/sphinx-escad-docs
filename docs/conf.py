# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sphinx
import datetime

project = 'DOCUMENTATION'
copyright = '2023, ESCAD Automation GmbH'
author = 'Martin Heubuch'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_escaddocs',
    'sphinxcontrib.plantuml',
    'sphinx_needs',
    'sphinx_copybutton',
]

version = "0.1"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

plantuml_output_format = "svg_img"
local_plantuml_path = os.path.join(os.path.dirname(__file__), "utils", "plantuml.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"

escaddocs_theme = 'escaddocs_theme'

escaddocs_file_name = 'Sphinx-ESCAD-docs.pdf'

escaddocs_vars = {
    'cover-overlay': 'rgba(84, 84, 84, 0.7)',
    'primary-opaque': 'rgba(211, 77, 40, 0.7)',
    'cover-bg': 'url(BackgroundReportA4.png) no-repeat center',
    'primary': '#d34c27',
    'secondary': '#54bfd3',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': '#54bfd3',
    'top-left-content': 'url(REscad.svg) no-repeat left center',
    'top-center-content': '',
    'top-right-content': '"Sphinx-ESCAD-docs Manual"',
    'bottom-left-content': '"Sphinx-ESCAD-docs.pdf"',
    'bottom-center-content': '',
    'bottom-right-content': 'counter(page)',
}

# use this to force using the weasyprint python API instead of building via the binary
# escaddocs_use_weasyprint_api = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_immaterial'
#html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'
#html_theme = 'sphinx_needs_pdf'
html_static_path = ['_static']

html_logo = './_static/REscad.svg'

html_theme_options = {
    'github_user': 'tastenmo',
    'github_repo': 'sphinx-escad-docs',
    'fixed_sidebar': True,
    'github_banner': True,
    'github_button': False,
}

html_context = {   
    'docs_scope': 'external',
    'cover_logo_title': '',
    'cover_meta_data': 'Sphinx-ESCAD-docs manual',
    'cover_footer': f'Build: {datetime.datetime.now().strftime("%d.%m.%Y")}<br>'
                    f'Maintained by <a href="https://www.escad.de">ESCAD Automation GmbH</a>',                                                              
    'authors' : [
        ("Martin Heubuch", "Softwareentwicklung", "martin.heubuch@escad.de"),
        ("Thomas Strohmaier", "Softwareentwicklung", "thomas.strohmaier@escad.de"),
        ("", "", "")
    ]} 


def setup_jquery(app, exception):
    """
    Inject jQuery if Sphinx>=6.x

    Staring on Sphinx 6.0, jQuery is not included with it anymore.
    As this extension depends on jQuery, we are including it when Sphinx>=6.x
    """

    if sphinx.version_info >= (5, 0, 0):
        # https://jquery.com/download/#using-jquery-with-a-cdn
        jquery_cdn_url = "https://code.jquery.com/jquery-3.6.0.min.js"
        html_js_files = getattr(app.config, "html_js_files", [])
        html_js_files.append((
            jquery_cdn_url,
            {
                'integrity': 'sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=',
                'crossorigin': 'anonymous'
            }
        ))
        app.config.html_js_files = html_js_files


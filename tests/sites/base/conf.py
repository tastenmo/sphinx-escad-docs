"""Test conf file."""

# -- Project information -----------------------------------------------------

project = "ESCAD Docs test"
copyright = '2023, ESCAD Automation GmbH'
author = 'Martin Heubuch'

root_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_escaddocs'

]

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_logo = './_static/REscad.svg'
html_copy_source = True
html_sourcelink_suffix = ""

# Base options, we can add other key/vals later
html_theme_options = {"navigation_with_keys": False}

html_sidebars = {"section1/index": ["sidebar-nav-bs.html"]}


# ESCAD docs theme
escaddocs_theme = 'escaddocs_theme'

escaddocs_debug = True

escaddocs_use_weasyprint_api = True

escaddocs_file_name = 'ESCAD Docs test.pdf'

escaddocs_vars = {
    'cover-overlay': 'rgba(84, 84, 84, 0.7)',
    'primary-opaque': 'rgba(211, 77, 40, 0.7)',
    'cover-logo' : 'url(REscad.svg) no-repeat left',
    'cover-bg': 'url(BackgroundReportA4.png) no-repeat left',
    'primary': '#d34c27',
    'secondary': '#54bfd3',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': '#54bfd3',
    #'top-left-content': 'url(emptylogo.png) no-repeat left',
    'top-left-content': '""',
    'top-center-content': '',
    'top-right-content': '',
    'bottom-left-content': '"ESCAD Docs test.pdf"',
    'bottom-center-content': '',
    'bottom-right-content': 'counter(page)',
}
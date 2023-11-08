

import re
from pathlib import Path

import pytest
import sphinx.errors
from sphinx_escaddocs.utils import escape_ansi

COMMON_CONF_OVERRIDES = dict(
    navigation_with_keys=False,
    surface_warnings=True,
)

def test_build_html(sphinx_build_factory, file_regression) -> None:
    """Test building the base html template and config."""
    sphinx_build = sphinx_build_factory("base")

    # Basic build with defaults
    sphinx_build.build()
    assert (sphinx_build.outdir / "index.html").exists(), sphinx_build.outdir.glob("*")

    index_html = sphinx_build.html_tree("index.html")
    subpage_html = sphinx_build.html_tree("section1/index.html")

    # Navbar structure
    navbar = index_html.select("div.navbar-header-items__center")[0]
    file_regression.check(navbar.prettify(), basename="navbar_ix", extension=".html")

    # Sidebar subpage
    sidebar = subpage_html.select(".bd-sidebar")[0]
    file_regression.check(
        sidebar.prettify(), basename="sidebar_subpage", extension=".html"
    )

    # Secondary sidebar should not have in-page TOC if it is empty
    assert not sphinx_build.html_tree("page1.html").select("div.onthispage")

    # Secondary sidebar should not be present if page-level metadata given
    assert not sphinx_build.html_tree("page2.html").select("div.bd-sidebar-secondary")

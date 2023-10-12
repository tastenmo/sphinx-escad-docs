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

    app.add_builder(EscadDocsBuilder)

    app.add_directive('if-builder', IfBuilderDirective)
    app.add_directive('if-include', IfIncludeDirective)
    app.add_directive('pdf-include', PdfIncludeDirective)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

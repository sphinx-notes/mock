"""
    sphinxnotes.mock
    ~~~~~~~~~~~~~~~

    Sphinx extension for mocking directives and roles.

    :copyright: Copyright 2022 Shengyu Zhang
    :license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import List, Dict

from sphinx.util import logging
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.docutils import SphinxDirective

from docutils.parsers.rst import directives

__title__= 'sphinxnotes-mock'
__license__ = 'BSD'
__version__ = '1.0.0b0'
__author__ = 'Shengyu Zhang'
__url__ = 'https://sphinx-notes.github.io/mock'
__description__ = ' Sphinx extension for mocking directives and roles'
__keywords__ = 'documentation, sphinx, extension'

logger = logging.getLogger(__name__)

class MockOptionSpec(Dict):
    def __getitem__(self, key):
        return directives.unchanged


class MockDirective(SphinxDirective):
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = MockOptionSpec()
    has_content = True

    def run(self) -> List[nodes.Node]:
        return []


def _config_inited(app:Sphinx, config:Config) -> None:
    for d in app.config.mock_directives:
        app.add_directive(d, MockDirective, override=True)


def setup(app:Sphinx) -> None:
    """Sphinx extension entrypoint."""

    app.add_config_value('mock_directives', [], 'env', types=List[str])
    app.connect('config-inited', _config_inited)

    return {'version': __version__}

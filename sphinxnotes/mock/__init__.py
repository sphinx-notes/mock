from __future__ import annotations
from typing import List, Dict

from sphinx.util import logging
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.docutils import SphinxDirective

from docutils.parsers.rst import directives
from docutils import nodes

__title__= 'sphinxnotes-mock'
__license__ = 'BSD'
__version__ = '1.0.1'
__author__ = 'Shengyu Zhang'
__url__ = 'https://sphinx.silverrainz.me/mock/'
__description__ = 'Sphinx extension for mocking directives and roles without modifying documents'
__keywords__ = 'documentation, sphinx, extension'

logger = logging.getLogger(__name__)

class MockOptionSpec(Dict):
    def __getitem__(self, _):
        return directives.unchanged


class MockDirective(SphinxDirective):
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = MockOptionSpec()
    has_content = True

    def run(self) -> List[nodes.Node]:
        mode = None
        for d in self.config.mock_directives:
            name = d if isinstance(d, str) else d[0]
            if self.name != name:
                continue
            mode = self.config.mock_mode if isinstance(d, str) else d[1]
            break

        if mode == 'literal':
            literal = nodes.literal_block(self.block_text, self.block_text)
            literal['language'] = 'rst'
            return [literal]
        elif mode == 'hide':
            return []
        else:
            raise ValueError('unsupported mock mode')



def _config_inited(app:Sphinx, config:Config) -> None:
    for d in config.mock_directives:
        name = d if isinstance(d, str) else d[0]
        app.add_directive(name, MockDirective, override=True)


def setup(app:Sphinx) -> Dict:
    """Sphinx extension entrypoint."""

    app.add_config_value('mock_directives', [], 'env')
    app.add_config_value('mock_mode', 'hide', 'env')
    app.connect('config-inited', _config_inited)

    return {'version': __version__}

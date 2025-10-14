from __future__ import annotations
from typing import List, Dict

from sphinx.util import logging
from sphinx.application import Sphinx
from sphinx.config import Config, ENUM
from sphinx.util.docutils import SphinxDirective

from docutils.parsers.rst import directives
from docutils import nodes

from . import meta

logger = logging.getLogger(__name__)


class MockOptionSpec(Dict):
    def __getitem__(self, _):
        return directives.unchanged


class _MockDirectiveLiteral(SphinxDirective):
    """Mock directive that shows the directive as a literal block."""

    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = MockOptionSpec()
    has_content = True

    def run(self) -> List[nodes.Node]:
        literal = nodes.literal_block(self.block_text, self.block_text)
        literal['language'] = 'rst'
        return [literal]


class _MockDirectiveHide(SphinxDirective):
    """Mock directive that hides the directive content."""

    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = MockOptionSpec()
    has_content = True

    def run(self) -> List[nodes.Node]:
        return []


_MOCK_DIRECTIVE_CLASSES = {
    'literal': _MockDirectiveLiteral,
    'hide': _MockDirectiveHide,
}


def _config_inited(app: Sphinx, config: Config) -> None:
    for d in config.mock_directives:
        name = d if isinstance(d, str) else d[0]
        mode = config.mock_default_mode if isinstance(d, str) else d[1]

        if mode not in ('literal', 'hide'):
            raise ValueError(
                f'Invalid mock mode for directive "{name}": {mode}. '
                f'Must be "literal" or "hide"'
            )

        directive_class = _MOCK_DIRECTIVE_CLASSES[mode]
        app.add_directive(name, directive_class, override=True)


def setup(app: Sphinx) -> Dict:
    """Sphinx extension entrypoint."""
    meta.pre_setup(app)

    app.add_config_value(
        'mock_directives',
        default=[],
        rebuild='env',
        types=list,
        description='List of directive names to mock. Each item can be a string (directive name) '
        'or a tuple (directive name, mode).',
    )
    app.add_config_value(
        'mock_default_mode',
        default='hide',
        rebuild='env',
        types=ENUM('hide', 'literal'),
        description='Default mode for mocking directives. Valid values: "hide", "literal".',
    )
    app.connect('config-inited', _config_inited)

    return meta.post_setup(app)

=============
Configuration
=============

The extension provides the following configuration:

:mock_directives: (Type: ``list[str|tuple[str,str]]``, Default: ``[]``)

                  Directive names in this list will be mocked by extension.

                  When a tuple given, the first field is the directive name and the second field is the custom mock mode (see ``mock_default_mode``),

                  For example, ``['toctree', ('contents', 'hide')]`` means that:

                  - mock ``toctree`` directive in default mode
                  - mock ``contents`` directive in ``hide`` mode

:mock_default_mode: (Type: ``str``, ''Default: ``'hide'``)

                    The default mode for mocking a directive/role.
                    Available values:

                    :hide: Hide the directive, it will not be seen on the document.
                    :literal_block: Show the raw text of directive in a `literal block`__

__ https://docutils.sourceforge.io/docs/user/rst/quickref.html#literal-blocks

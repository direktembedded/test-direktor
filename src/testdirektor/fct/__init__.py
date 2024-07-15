import argparse
from .. import version


_host_config_help = """Path to file containing host and test fixture configuration.
Configuration file is a json file conforming to a Marshmallow Dataclass as defined in module
testdirektor.control.hostconfig
"""

_visibility_help = """Specify how application UI is shown.
Suggested Options: FullScreen, Maximized
Full Options from Qt: https://doc.qt.io/qt-6/qwindow.html#Visibility-enum
"""


_fct_title = 'Test Executor™ FCT'


def base_argument_parser(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--version', '-v', action='version',
                        version=f'{version.TEST_EXECUTOR_FCT_VERSION}')
    parser.add_argument('host_config', help=_host_config_help)
    parser.add_argument('--visibility', help=_visibility_help, default="FullScreen")
    return parser


def run():
    from testdirektor.control.engine import Engine

    args = base_argument_parser(_fct_title).parse_args()
    engine = Engine(args.host_config)
    engine.run(visibility=args.visibility, about_text=f'<b>{_fct_title}</b><p>')

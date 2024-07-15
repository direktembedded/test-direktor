
import os
from marshmallow.exceptions import ValidationError as MarshMallowValidationError
from testexecutor.model.TestSuiteGroup import TestSuiteGroup
from testexecutor.model.MultiTestWindowModel import MultiTestWindowModel
from robottestexecutor.control.TestExecutorController import TestExecutorController
from testdirektor.config.hostconfig import HostConfigSchema
from ..config.configexception import FctConfigException


class Engine(object):

    def __init__(self, host_config=None, single_selector=False):
        if host_config:
            self.my_suite_group = None
            self.host_name = None
            self.ui_config = None
            self.single_selector = single_selector
            self.setup(host_config)
        else:
            raise FctConfigException("No host configuration file provided")

    def setup(self, host_config_file=None):
        host_config_file = Engine.prepend_working_path(host_config_file)
        base_path = os.path.dirname(host_config_file)
        host_config = Engine.load_host_config(host_config_file)

        if host_config:
            # Base path is the path that paths in ui and id config are base against if they specify ./
            base_path = Engine.prepend_working_path(base_path)
            id_config_file = Engine.prepend_base_path(host_config.id_config, base_path)
            db_file = Engine.prepend_base_path(host_config.db_config, base_path)
            test_path = Engine.prepend_base_path(host_config.test_path, base_path)
            self.ui_config = Engine.prepend_base_path(host_config.ui_config, base_path)
            self.host_name, host_id = Engine.fetch_host_name(host_config)
            unique_ids = host_config.unique_identifiers

            fixture_count = len(host_config.fixtures)
            if self.single_selector and fixture_count != 1:
                raise FctConfigException(
                    f"Only one fixture must be specified in {host_config_file} fixtures element")
            elif fixture_count > 0:
                self.my_suite_group = TestSuiteGroup()
                for station in host_config.fixtures:
                    host_info = {'td.host_fixture':
                                 {
                                    'host_id': host_id,
                                    'fixture_id': station.fixture_id
                                 }
                                }

                    id_monitor = Engine.load_monitor(station)

                    self.my_suite_group.addData(TestExecutorController(f"{station.title}",
                                                id_config=id_config_file,
                                                db_config_file=db_file,
                                                testpath=test_path,
                                                instance_table_records=host_info,
                                                id_monitor=id_monitor,
                                                output_folder=host_config.output_path,
                                                unique_ids=unique_ids,
                                                useselector=self.single_selector))

            else:
                raise FctConfigException(f"At least one fixture must be specified in {host_config_file} fixtures element")
        else:
            raise FctConfigException(f"Failed to load host configuration {host_config_file}")

    def run(self, visibility="FullScreen", about_text="<b>Test Direktor™ FCT</b><p>", title=None):
        import sys
        sys.argv += ['--style', 'Fusion']

        if not title:
            title = f"{self.host_name}: {title}"

        with open(self.ui_config) as f:
            window_model = MultiTestWindowModel(self.my_suite_group, title)
            window_model.visibility = visibility
            window_model.config = f.read()
            window_model.about = about_text

            exit(window_model.exec())

    @staticmethod
    def load_host_config(host_config_file):
        host_config_ret = None
        try:
            if os.path.isfile(host_config_file):
                with open(host_config_file) as f:
                    host_config_str = f.read()
                    host_config_ret = HostConfigSchema().loads(host_config_str)
        except MarshMallowValidationError as ex:
            raise
        except Exception as ex:
            raise Exception("Failed to load host configuration data") from ex

        return host_config_ret

    @staticmethod
    def prepend_working_path(file_name):
        current_path = os.getcwd()
        if file_name.startswith('.'):
            file_name = os.path.join(current_path, file_name)
        return file_name

    @staticmethod
    def prepend_current_path(file_name):
        current_path = os.path.dirname(os.path.abspath(__file__))
        if file_name.startswith('.'):
            file_name = os.path.join(current_path, file_name)
        return file_name

    @staticmethod
    def prepend_base_path(file_name, base_path):
        _base_path = Engine.prepend_working_path(base_path)
        if file_name.startswith('.'):
            file_name = os.path.join(_base_path, file_name)
        return file_name

    @staticmethod
    def fetch_host_name(host_config):
        if host_config.host and host_config.host.name:
            name = host_config.host.name
        else:
            import socket
            name = socket.gethostname()
        if host_config.host and host_config.host.id:
            _id = host_config.host.id
        else:
            _id = name
        return name, _id

    @staticmethod
    def load_monitor(fixture):
        monitor = None
        if fixture.id_monitor:
            import importlib

            # TODO catch exception and handle cleaner for user if missing module
            # ModuleNotFoundError: No module named 'fct_parser_det'
            module = importlib.import_module(fixture.id_monitor.module)
            monitor_class = getattr(module, fixture.id_monitor.implementation)
            monitor = monitor_class(**fixture.id_monitor.arguments)
        return monitor

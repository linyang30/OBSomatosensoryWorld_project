from airtest.core.api import *
import yaml

class BaseView:

    def get_config_data(self):
        with open('../config/device_config.yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file)
        return data

    def start_app(self):
        data = self.get_config_data()
        start_app(data['app_package'])

    def stop_app(self):
        data = self.get_config_data()
        stop_app(data['app_package'])

    def connect(self):
        data = self.get_config_data()
        connect_device('Android://' + str(data['ip']) + ':' + str(data['port']) + '/' + str(
            data['device_name']) + '?ori_method=' + str(data['connect_func']))
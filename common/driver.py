from airtest.core.api import connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import yaml
from baseView.baseView import BaseView

class Driver(BaseView):

    def get_poco(self):
        with open('../config/device_config.yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file)
        connect_device('Android://' + str(data['ip']) + ':' + str(data['port']) + '/' + str(data['device_name']) + '?ori_method=' + str(data['connect_func']))
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False, force_restart=True)
        return poco


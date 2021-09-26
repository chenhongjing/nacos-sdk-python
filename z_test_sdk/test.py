import logging
import time

from v2.nacos.config.nacos_config_service import NacosConfigService
from v2.nacos.naming.ievent_listener import EventListener
from v2.nacos.naming.nacos_naming_service import NacosNamingService
import sys

SERVER_ADDRESSES = "http://mse-96d50180-p.nacos-ans.mse.aliyuncs.com:8848"
# SERVER_ADDRESSES = "http://10.62.188.68:8848"
NAMESPACE = "public"


class TestEventListener(EventListener):

    def on_event(self) -> None:
        print("Hello!")


mode = 1

if __name__ == '__main__':
    properties = {
        "namespace": NAMESPACE,
        "serverAddr": SERVER_ADDRESSES,
        "username": "nacos",
        "password": "nacos",
        "endpoint": "",
        "contextPath": "/nacos",
        "ak": "nnn",
        "sk": "nnn"
    }

    logger = logging.getLogger("nacos")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s:%(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.removeHandler(handler)

    if mode == 1:

        naming = NacosNamingService(logger, properties)
        naming.register_instance("nacos.test.1", "default", "11.11.11.11", 8880, "default")
        naming.register_instance("nacos.test.2", "default", "11.11.11.11", 8882, "default")
        naming.register_instance("nacos.test.3", "default", "11.11.11.11", 8888, "default")
        print("registered!")
        time.sleep(5)
        #
        # naming.subscribe("nacos.test.1", "default", ["default"], TestEventListener())
        # print("subscribed!")
        # time.sleep(5)
        #
        # # naming.unsubscribe()
        #
        list_view = naming.get_services_of_server(0, 1024, "default", None)
        print(str(list_view))
        print("get services of server done!")
        time.sleep(5)
        #
        print(naming.get_server_status())
        print("check server status done!")
        time.sleep(5)

        # todo ?
        instances = naming.get_all_instances("nacos.test.3", "default", ["default"], True)
        print(instances)
        print("get all instances!")
        time.sleep(5)

        # todo select instances, select one healthy instance

        # todo subscribe

        # todo unsubscribe

        naming.deregister_instance("nacos.test.3", "default", "11.11.11.11", 8888, "default")
        print("deregistered!")
        time.sleep(5)

        # todo shutdown
        #
        # time.sleep(10)
        # naming.shutdown()
    else:
        config = NacosConfigService(logger, properties)

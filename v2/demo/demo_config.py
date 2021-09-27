import logging
import time

# SERVER_ADDRESSES = "http://127.0.0.1:8848"
from v2.nacos.config.ilistener import Listener
from v2.nacos.config.nacos_config_service import NacosConfigService

SERVER_ADDRESSES = "http://mse-96d50180-p.nacos-ans.mse.aliyuncs.com:8848"
NAMESPACE = "public"

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


class DemoListener(Listener):
    def get_executor(self):
        return

    def receive_config_info(self, config_info: str):
        print("receive_config_info:", config_info)


if __name__ == '__main__':
    config = NacosConfigService(logger, properties)

    # get server status
    server_status = config.get_server_status()
    print("server_status:", server_status)

    # publish config
    publish_config = config.publish_config("nacos_config_test1", "default", "content", "text")
    print("publish_config:", str(publish_config))
    time.sleep(1)

    # publish config cas

    # get config
    config_content = config.get_config("nacos_config_test1", "default", 3000)
    print("get_config:", config_content)

    # add listener
    demo_listener = DemoListener()
    config.add_listener("nacos_config_test1", "default", demo_listener)
    print("add_listener complete")
    time.sleep(1)

    # # remove listener 暂时有问题，在查
    # config.remove_listener("nacos_config_test1", "default", demo_listener)
    # print("remove_listener complete")
    # time.sleep(1)
    #
    # get config and sign listener

    # remove config

    # shutdown
    config.shutdown()

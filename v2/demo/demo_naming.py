import logging
import time

from v2.nacos.naming.dtos.instance import Instance
from v2.nacos.naming.dtos.service import Service
from v2.nacos.naming.ievent_listener import EventListener
from v2.nacos.naming.nacos_naming_service import NacosNamingService

# SERVER_ADDRESSES = "http://mse-96d50180-p.nacos-ans.mse.aliyuncs.com:8848"
SERVER_ADDRESSES = "10.63.251.116:8848"
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


class DemoListener(EventListener):

    def on_event(self, event) -> None:
        print("on event!")


if __name__ == '__main__':
    naming = NacosNamingService(logger, properties)

    # register instance
    service_meta = {"test": True}
    service = Service(
        name="nacos.test.1", groupName="TEST", appName="nacos-naming", protectThreadhold=0.8, metadata=service_meta
    )

    instance_meta = {"site": "test"}
    instance = Instance(instanceId=1111, ip="11.11.11.11", port=8888, weight=2.0, service=service, metadata=instance_meta)

    naming.register_instance("nacos.test.2", "default", instance)

    # get all instances
    all_instances = naming.get_all_instances("nacos.test.2", "default", [], True)
    print(all_instances)

    # get selected instances
    if all_instances:
        selected_instances = naming.select_instances("nacos.test.2", "default", [], True, True)
        print(selected_instances)

    # select one healthy instance
    # one_healthy_instance = naming.select_one_healthy_instance()

    # get services of server
    list_view = naming.get_services_of_server(0, 1024, "default", None)
    print(str(list_view))

    # subscribe
    naming.subscribe("nacos.test.2", "default", [], DemoListener())
    print("subscribe done!")

    service_meta = {"test": True}
    service = Service(
        name="nacos.test.8", groupName="TEST", appName="nacos-naming", protectThreadhold=8.8, metadata=service_meta
    )

    instance_meta = {"site": "test"}
    instance = Instance(instanceId=1112, ip="11.11.11.11", port=8880, weight=3.0, service=service,
                        metadata=instance_meta)

    naming.register_instance("nacos.test.2", "default", instance)

    print("register new instance!")

    # # time.sleep(10)
    # # naming.shutdown()



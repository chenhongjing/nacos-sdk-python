import logging
import time

from v2.nacos.naming.ievent_listener import EventListener
from v2.nacos.naming.nacos_naming_service import NacosNamingService

# SERVER_ADDRESSES = "http://127.0.0.1:8848"
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


class DemoListener(EventListener):
    def on_event(self, event) -> None:
        print("on listening...")


if __name__ == '__main__':
    naming = NacosNamingService(logger, properties)

    instance_meta = {"site": "test"}
    naming.register_instance(
        service_name="nacos.test.2", group_name="default", cluster_name="DEFAULT", ip="11.11.11.11", port=8888,
        weight=2.0, metadata=instance_meta
    )
    time.sleep(1)

    naming .register_instance(
        service_name="nacos.test.2", group_name="default", cluster_name="DEFAULT", ip="11.11.11.11", port=8880,
        weight=1.5, healthy=False, metadata=instance_meta
    )
    time.sleep(1)

    # get all instances
    all_instances = naming.get_all_instances("nacos.test.2", "default", ["DEFAULT"], True)
    print(all_instances)

    # select instances
    selected_healthy_instances = naming.select_instances("nacos.test.2", "default", ["DEFAULT"], True, True)
    print("select healhty instances:", str(selected_healthy_instances))

    selected_unhealthy_instances = naming.select_instances("nacos.test.3", "default", ["DEFAULT"], False, True)
    print("select unhealthy instances:", str(selected_unhealthy_instances))

    # select one healthy instance
    one_healthy_instance = naming.select_one_healthy_instance("nacos.test.2", "default", ["DEFAULT"], True)
    print("select one healthy instance:", str(one_healthy_instance))

    # get services of server
    list_view = naming.get_services_of_server(0, 1024, "default", None)
    print("list_view:", str(list_view))

    # subscribe
    demo_listener = DemoListener()
    naming.subscribe("nacos.test.2", "default", [], demo_listener)
    time.sleep(1)

    # get server status
    server_status = naming.get_server_status()
    print("server_status:", server_status)

    # unsubscribe
    naming.unsubscribe("nacos.test.2", "default", [], demo_listener)
    time.sleep(1)
    print("unsubscribed!")

    # deregister instance
    naming.deregister_instance("nacos.test.2", "default", "11.11.11.11", 8888, "DEFAULT")
    time.sleep(1)

    # shutdown
    naming.shutdown()

from abc import ABCMeta

from v2.nacos.remote.requests.request import Request


class AbstractNamingRequest(Request, metaclass=ABCMeta):
    def __init__(self, namespace: str, serviceName: str, groupName: str):
        super().__init__()
        self.__MODULE = "naming"
        self.namespace = namespace
        self.serviceName = serviceName
        self.groupName = groupName

    def get_module(self):
        return self.__MODULE

    def get_namespace(self) -> str:
        return self.namespace

    def set_namespace(self, namespace: str) -> None:
        self.namespace = namespace

    def get_service_name(self) -> str:
        return self.serviceName

    def set_service_name(self, serviceName: str) -> None:
        self.serviceName = serviceName

    def get_group_name(self) -> str:
        return self.groupName

    def set_group_name(self, groupName: str) -> None:
        self.groupName = groupName

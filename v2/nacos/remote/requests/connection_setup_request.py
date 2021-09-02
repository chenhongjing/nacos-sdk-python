from typing import Dict
from v2.nacos.remote.requests import request
from v2.nacos.remote.utils import remote_request_type
from v2.nacos.ability.client_abilities import ClientAbilities


class ConnectionSetupRequest(request.Request):
    def init(self):
        super().init()
        self.clientVersion = ""
        self.clientAbilities = None
        self.abilities = ClientAbilities()
        self.tenant = ""
        self.labels = {}

        self.MODULE = "internal"

    def get_client_version(self) -> str:
        return self.clientVersion

    def set_client_version(self, clientVersion: str) -> None:
        self.clientVersion = clientVersion

    def get_labels(self) -> Dict[str, str]:
        return self.labels

    def set_labels(self, labels: Dict[str, str]) -> None:
        self.labels = labels

    def get_tenant(self) -> str:
        return self.tenant

    def set_tenant(self, tenant: str) -> None:
        self.tenant = tenant

    def get_abilities(self) -> ClientAbilities:
        return self.abilities

    def set_abilities(self, abilities: ClientAbilities) -> None:
        self.abilities = abilities

    def get_module(self):
        return self.MODULE

    def get_remote_type(self):
        return remote_request_type["ConnectionSetup"]
from v2.nacos.exception.nacos_exception import NacosException


class GroupKey:
    PLUS = '+'

    PERCENT = '%'

    TWO = '2'

    B = 'B'

    FIVE = '5'

    @staticmethod
    def get_key(data_id: str, group: str, datum_str: str) -> str:
        return GroupKey.__do_get_key(data_id, group, datum_str)

    @staticmethod
    def get_key_tenant(data_id: str, group: str, tenant: str) -> str:
        return GroupKey.__do_get_key(data_id, group, tenant)

    @staticmethod
    def parse_key(group_key: str) -> list:
        pass

    @staticmethod
    def url_encode(string: str) -> str:
        sb = ""
        for c in string:
            if GroupKey.PLUS == c:
                sb += "%2B"
            elif GroupKey.PERCENT == c:
                sb += "%25"
            else:
                sb += c
        return sb

    @staticmethod
    def __do_get_key(data_id: str, group: str, datum_str: str) -> str:
        if not data_id or not data_id.strip():
            raise NacosException("invalid dataId")
        if not group or not group.strip():
            raise NacosException("invalid group")

        sb = ""
        sb += GroupKey.url_encode(data_id)
        sb += GroupKey.PLUS
        sb += GroupKey.url_encode(group)
        if datum_str:
            sb += GroupKey.PLUS
            sb += GroupKey.url_encode(datum_str)
        return sb

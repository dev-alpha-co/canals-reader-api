
from logics.utils.dynamodb_util import DynamoDbUtil


TABLE_NAME = "CHARACTERS"


class CharactersTable:
    @staticmethod
    def get(char_id):
        return DynamoDbUtil.get_item(
            TABLE_NAME,
            "charId", char_id)

    @staticmethod
    def get_all():
        return DynamoDbUtil.scan_all(TABLE_NAME)

    @staticmethod
    def put(char_id, url, proc_type):
        item = {
            "charId": DynamoDbUtil.to_str_field(char_id),
            "url": DynamoDbUtil.to_str_field(url),
            "procType": DynamoDbUtil.to_str_field(proc_type),
        }

        return DynamoDbUtil.put_item(TABLE_NAME, item)

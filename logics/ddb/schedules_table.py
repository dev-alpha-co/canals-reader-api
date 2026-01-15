
from decimal import Decimal
from boto3.dynamodb.conditions import Attr, And
from logics.utils.dynamodb_util import DynamoDbUtil


TABLE_NAME = "SCHEDULES"


class SchedulesTable:
    @staticmethod
    def scan(charId, start, end):
        filter_expression = And(
            Attr('charId').eq(charId),
            Attr('date').between(Decimal(start), Decimal(end))
        )
        return DynamoDbUtil.scan(
            TABLE_NAME,
            filter_expression=filter_expression
        )

    @staticmethod
    def put(charId, date, start, end, ttl):
        DynamoDbUtil.upsert_item(
            TABLE_NAME,
            {
                "charId": charId,
                "date": date,
            },
            {
                "startTime": start,
                "endTime": end,
                "expire_at": ttl
            },
            None
        )

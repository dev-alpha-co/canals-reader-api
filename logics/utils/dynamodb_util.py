
import os
import boto3
import itertools
from botocore.exceptions import ClientError


class DynamoDbUtil:
    @staticmethod
    def create_table_dao(table_name):
        _table_name = DynamoDbUtil.to_env_table_name(table_name)
        res = boto3.resource("dynamodb")
        return res.Table(_table_name)

    @staticmethod
    def to_env_table_name(table_name):
        env = os.getenv('ENV', 'dev')
        if table_name.startswith(env):
            return table_name

        return f"{table_name}"

    @staticmethod
    def get_item(table_name, key):
        table = DynamoDbUtil.create_table_dao(table_name)
        res = table.get_item(Key=key)

        if "Item" in res:
            return res["Item"]
        else:
            return None

    @staticmethod
    def scan_all(table_name):
        table = DynamoDbUtil.create_table_dao(table_name)
        try:
            results = []
            while True:
                response = table.scan()

                if response and response["Count"] > 0:
                    results += response["Items"]
                last_key = response.get("LastEvaluatedKey")
                if last_key:
                    scan_kwargs = {
                        'ExclusiveStartKey': last_key
                    }
                    response = table.scan(**scan_kwargs)
                else:
                    break
            return results
        except ClientError as e:
            print(e.response['Error']['Message'])
            raise e

    @staticmethod
    def scan(table_name, filter_expression=None, expression_names=None):
        table = DynamoDbUtil.create_table_dao(table_name)
        try:
            arg = {
                "FilterExpression": filter_expression
            }

            if expression_names:
                arg["ExpressionAttributeNames"] = expression_names

            results = []
            while True:
                response = table.scan(**arg)

                if response and response["Count"] > 0:
                    results += response["Items"]
                last_key = response.get("LastEvaluatedKey")
                if last_key:
                    arg["ExclusiveStartKey"] = last_key
                else:
                    break
            return results
        except ClientError as e:
            print(e.response['Error']['Message'])
            raise e

    @staticmethod
    def query(table_name, kwargs):
        table = DynamoDbUtil.create_table_dao(table_name)
        try:
            results = []
            while True:
                response = table.query(**kwargs)

                if response and response["Count"] > 0:
                    results += response["Items"]
                last_key = response.get("LastEvaluatedKey")
                if last_key:
                    kwargs["ExclusiveStartKey"] = last_key
                else:
                    break
            return results
        except ClientError as e:
            print(e.response['Error']['Message'])
            raise e

    @staticmethod
    def batch_get_item(table_name, keys_json):
        _table_name = DynamoDbUtil.to_env_table_name(table_name)
        res = boto3.resource("dynamodb")
        table = res.Table(_table_name)
        try:
            results = []
            keys_data = [dict(zip(keys_json, i))
                         for i in itertools.product(*keys_json.values())]
            kwargs = {
                "RequestItems": {
                    table_name: {
                        'Keys': keys_data
                    }
                },
                "ReturnConsumedCapacity": 'TOTAL'
            }
            while True:
                response = table.batch_get_item(**kwargs)
                response = response.get("Responses")
                if response.get(_table_name):
                    results += response.get(_table_name)
                last_key = response.get("UnprocessedKeys")
                if last_key:
                    kwargs["RequestItems"][_table_name]["Keys"] = \
                        last_key[_table_name]["Keys"]
                else:
                    break
            return results
        except ClientError as e:
            print(e.response['Error']['Message'])
            raise e

    @staticmethod
    def upsert_item(table_name, key, update_data, condition):
        _table_name = DynamoDbUtil.to_env_table_name(table_name)
        res = boto3.resource("dynamodb")
        table = res.Table(_table_name)
        try:
            update_expression = "set "
            express_values = {}
            if update_data:
                for _key, value in update_data.items():
                    update_expression += f"{_key} = :{_key},"
                    express_values[f":{_key}"] = value
            # Add condition
            condition_expression = ""
            if condition:
                for _key, value in condition.items():
                    condition_expression += f"{_key} = :{_key} and"
                    express_values[f":{_key}"] = value

            update_arg = {
                "Key": key,
                "UpdateExpression": update_expression[:-1],
                "ExpressionAttributeValues": express_values,
                "ReturnValues": "UPDATED_NEW"
            }
            if condition_expression:
                update_arg["ConditionExpression"] = condition_expression[:-3]

            response = table.update_item(**update_arg)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def auto_increment(table_name, key, field_name):
        _table_name = DynamoDbUtil.to_env_table_name(table_name)
        res = boto3.resource("dynamodb")
        table = res.Table(_table_name)
        try:

            update_arg = {
                "Key": key,
                "UpdateExpression": f'SET {field_name} = if_not_exists({field_name}, :ZERO) + :Increment',
                "ExpressionAttributeValues": {
                    ':ZERO': 0,
                    ':Increment': 1,
                },
                "ReturnValues": "UPDATED_NEW"
            }

            response = table.update_item(**update_arg)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return int(response['Attributes'][field_name])

    def delete_item(table_name, key):
        table = DynamoDbUtil.create_table_dao(table_name)
        try:

            delete_arg = {
                "Key": key
            }

            response = table.delete_item(**delete_arg)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

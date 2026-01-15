
import ulid
import time
import secrets


class CommonUtil:
    @staticmethod
    def is_null_or_empty(value: str):
        if value is None:
            return True

        if not value:
            return True

        if value == "":
            return True

        return False

    @staticmethod
    def has_not_key_or_empty(obj, key):
        if key not in obj:
            return True

        return CommonUtil.is_null_or_empty(obj[key])

    @staticmethod
    def to_dict(records, key):
        result = {}

        for r in records:
            result[r[key]] = r

        return result

    @staticmethod
    def to_values(records, key):
        return list(CommonUtil.to_dict(records, key).keys())

    @staticmethod
    def extract_values(old, mapping):
        r = {}
        for key_info in mapping:
            old_key = key_info["old_key"]
            if old_key in old:
                new_key = key_info["new_key"]
                r[new_key] = old[old_key]

        return r

    @staticmethod
    def ulid():
        time.sleep(0.001)
        return ulid.new().str.lower()

    @staticmethod
    def first(ary):
        if ary is None:
            return None

        if len(ary) == 0:
            return None

        return ary[0]

    @staticmethod
    def unique(ary):

        return list(dict.fromkeys(ary))

    @staticmethod
    def rand_num_code(digit):
        under = int(f"1{'0' * digit}")
        upper = int(f"1{'9' * digit}")

        rand_num = CommonUtil.secretsRandint(under, upper)

        return f"{rand_num}"[-digit:]

    def secretsRandint(a, b):
        return (secrets.randbelow((b - a) + 1)) + a

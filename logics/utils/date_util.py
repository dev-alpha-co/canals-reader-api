import re
from datetime import datetime, timedelta, timezone
from monthdelta import monthmod
from monthdelta import monthdelta
from dateutil.relativedelta import relativedelta

JST = timezone(timedelta(hours=+9), 'JST')


class DateUtil:
    @staticmethod
    def jst():

        return datetime.now(JST)

    @staticmethod
    def date(dt: datetime):
        return DateUtil.str_to_datetime(
            DateUtil.to_str(dt, '%Y-%m-%d'), '%Y-%m-%d')

    @staticmethod
    def delta(years=0, days=0, hours=0, minutes=0, seconds=0):

        return relativedelta(years=years, days=days, hours=hours, minutes=minutes, seconds=seconds)

    @staticmethod
    def ymd(year, month, day, hour=0, minute=0, second=0):
        return datetime(year=year, month=month, day=day,
                        hour=hour, minute=minute, second=second)

    @staticmethod
    def to_str(dt, format='%Y/%m/%d'):
        if dt in (None, ""):
            return None
        if isinstance(dt, str):
            return dt
        return dt.strftime(format)

    @staticmethod
    def str_to_datetime(_str, _format="%Y/%m/%d %H:%M:%S",
                        _timezone=None, _replace_tzinfo=False):
        if _str in (None, ""):
            return None

        _datetime = datetime.strptime(_str, _format)

        if _timezone:
            _datetime = DateUtil.switch_to_timezone(_datetime, _timezone)

        if _replace_tzinfo:
            _datetime = _datetime.replace(tzinfo=_replace_tzinfo)

        return _datetime

    @staticmethod
    def switch_to_timezone(_dt, _timezone=JST):
        if _dt and isinstance(_dt, datetime):
            return _dt.astimezone(_timezone)

        return None

    @staticmethod
    def first_day(year, month):
        _month = f'{month}'.zfill(2)
        return DateUtil.str_to_datetime(f"{year}/{_month}/01 00:00:00")

    @staticmethod
    def last_day(year, month):
        if month == 12:
            next_month_first_day = DateUtil.first_day(year + 1, 1)
        else:
            next_month_first_day = DateUtil.first_day(year, month + 1)
        return next_month_first_day - timedelta(days=1)

    @staticmethod
    def age(birthday, target):
        # 対象日より誕生日が未来の場合、0を返す
        diff = int(target.strftime("%Y%m%d")) - \
            int(birthday.strftime("%Y%m%d"))
        if diff < 0:
            return 0

        return diff // 10000

    @staticmethod
    def age_month(birthday, target):
        month_diff = DateUtil.month_diff(birthday, target)

        y = month_diff // 12
        m = month_diff % 12

        return y, m

    @staticmethod
    def month_diff(dt1, dt2):
        if dt2 <= dt1:
            return 0

        mmod = monthmod(dt1, dt2)
        diff_month = mmod[0].months

        if dt1.day > dt2.day and DateUtil.is_last_day(dt2):
            diff_check = dt1 + monthdelta(diff_month)
            if diff_check < dt2:
                diff_month += 1

        return diff_month

    @staticmethod
    def is_last_day(dt):
        # if dt.month == 2 and dt.day == 28:
        #     return True

        last_day = DateUtil.last_day(dt.year, dt.month)
        if last_day.day == dt.day:
            return True

    @staticmethod
    def calc_class(birthday, target):

        # 4/1時点の年齢をクラスとする
        baseDate = DateUtil.term_start(target)

        _age = DateUtil.age(birthday, baseDate)
        if _age < 0:
            _age = 0

        return f'{_age}歳児'

    def term_start(dt):
        if dt.month < 4:
            return DateUtil.ymd(dt.year - 1, 4, 1)
        else:
            return DateUtil.ymd(dt.year, 4, 1)

    @staticmethod
    def day_of_week(dt):
        w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
        return (w_list[dt.weekday()])

    @staticmethod
    def is_duplicate(x_from, x_to, y_from, y_to, same_ng=False):
        now = DateUtil.jst()
        today = DateUtil.to_str(now, '%Y-%m-%d')

        _x_from = DateUtil.str_to_datetime(
            f'{today} {x_from}:00', "%Y-%m-%d %H:%M:%S")
        _x_to = DateUtil.str_to_datetime(
            f'{today} {x_to}:00', "%Y-%m-%d %H:%M:%S")
        _y_from = DateUtil.str_to_datetime(
            f'{today} {y_from}:00', "%Y-%m-%d %H:%M:%S")
        _y_to = DateUtil.str_to_datetime(
            f'{today} {y_to}:00', "%Y-%m-%d %H:%M:%S")

        if same_ng:
            if _y_to < _x_from:
                return False
            if _x_to < _y_from:
                return False
        else:
            if _y_to <= _x_from:
                return False
            if _x_to <= _y_from:
                return False

        return True

    @staticmethod
    def generate_date_list(start_date, end_date, delta):
        """
        start_dateとend_dateの間の日付リストを生成する
        """
        date_list = []
        current_date = start_date

        while current_date <= end_date:
            date_list.append(current_date)
            current_date += delta

        return date_list

    @staticmethod
    def to_date_from_MMDD(txt):
        if "(" not in txt:
            return None
        if "/" not in txt:
            return None

        now = DateUtil.jst()
        ymd = DateUtil.str_to_datetime(
            f"{now.year}/{txt.split('(')[0]}",
            "%Y/%m/%d"
        )

        if now.month == 12 and ymd.month == 1:
            return ymd + relativedelta(years=1)
        return ymd

    @staticmethod
    def is_time(txt):
        if re.match("^([01]?[0-9]|2[0-3]):([0-5]?[0-9])$", txt):
            return True

        return False

    @staticmethod
    def to_epoch_seconds(dt):
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=JST)
        return int(dt.timestamp())

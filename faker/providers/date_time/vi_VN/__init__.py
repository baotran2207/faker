# coding: utf-8
from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    """Datetime generator for Vietnamese locale"""

    day_names = {
        "0": "Chủ nhật",
        "1": "Thứ hai",
        "2": "Thứ ba",
        "3": "Thứ tư",
        "4": "Thứ năm",
        "5": "Thứ sáu",
        "6": "Thứ bảy",
    }

    month_names = {
        "01": "Tháng một",
        "02": "Tháng hai",
        "03": "Tháng ba",
        "04": "Tháng tư",
        "05": "Tháng năm",
        "06": "Tháng sáu",
        "07": "Tháng bảy",
        "08": "Tháng tám",
        "09": "Tháng chín",
        "10": "Tháng mười",
        "11": "Tháng mười một",
        "12": "Tháng mười hai",
    }

    def day_of_week(self):
        day = self.date('%w')
        return Provider.day_names[day]

    def month_name(self):
        month = self.month()
        return Provider.month_names[month]

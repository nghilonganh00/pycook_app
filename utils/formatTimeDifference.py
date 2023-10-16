from datetime import datetime


def format_time_difference(createdDate):
    time_format = "%a, %d %b %Y %H:%M:%S GMT"
    time_object = datetime.strptime(createdDate, time_format)
    time_difference = datetime.now() - time_object
    # Lấy số năm, tháng, ngày từ kết quả phép trừ
    years, remainder = divmod(time_difference.days, 365)
    months, days = divmod(remainder, 30)
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if years != 0:
        return f"cách đây {years} năm"
    elif months != 0:
        return f"cách đây {months} tháng"
    elif days != 0:
        return f"cách đây {days} ngày"
    elif hours != 0:
        return f"cách đây {hours} giờ"
    elif minutes != 0:
        return f"cách đây {minutes} phút"
    elif seconds != 0:
        return f"cách đây {seconds} giây"


def conver_date_fotmat(createdDate):
    time_format = "%a, %d %b %Y %H:%M:%S GMT"
    time_object = datetime.strptime(createdDate, time_format)
    formatted_date = time_object.strftime("%d tháng %m, %Y")

    return formatted_date

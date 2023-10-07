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
        return f'cach day {years} nam'
    elif months != 0:
        return f'cach day {months} thang'
    elif days != 0:
        return f'cach day {days} ngay'
    elif hours != 0:
        return f'cach day {hours} gio'
    elif minutes != 0:
        return f'cach day {minutes} phut'
    elif seconds != 0:
        return f'cach day {seconds} giay'



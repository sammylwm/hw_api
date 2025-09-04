import datetime

from api_v1.classes.schedule import get_schedule_with_class

date = "03.09.2025"
date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
weekday = date_obj.strftime("%A").lower()
subject = "Алгебра"
class_name = "11A"
print(weekday)
if not subject in get_schedule_with_class(class_name)[weekday]:
    print(get_schedule_with_class(class_name)[weekday])
    print(0)

import datetime
import locale

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

date_obj = datetime.datetime.strptime("10.09.2025", "%d.%m.%Y")
weekday = date_obj.strftime("%A").lower()

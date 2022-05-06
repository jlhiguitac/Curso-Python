from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y %H:%M:%S"))

paris_timezone = pytz.timezone("Europe/Paris")
paris_date = datetime.now(paris_timezone)
print("París: ", paris_date.strftime("%d/%m/%Y %H:%M:%S"))

mexico_city_timezone = pytz.timezone("America/mexico_city")
mexico_city_date = datetime.now(mexico_city_timezone)
print("Ciudad de México: ", mexico_city_date.strftime("%d/%m/%Y %H:%M:%S"))
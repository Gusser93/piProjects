from gpiozero import LED
from pyowm import OWM

sunny = LED(17)
rain = LED(18)
cold = LED(19)
hot = LED(20)

API_KEY = '695b1925a51da2f8e4123e099501cdf6'
owm = OWM(API_key=API_KEY, language='de')

mainzId = 2874225

#mainzWeather = owm.weather_at_id(mainzId)
mainzFc = owm.three_hours_forecast_at_id(mainzId)
mainzF = mainzFc.get_forecast()
weatherList = mainzF.get_weathers()
threeHours = 3*60*60
newWeatherList = []
time = mainzFc.when_starts()
interval = mainzF.get_interval()
reception_time = mainzF.get_reception_time(timeformat='unix')
location = mainzF.get_location()


for i in range(0,2):
	newWeatherList.append(mainzFc.get_weather_at(time+threeHours*i))

MainzF = pyowm.webapi25.forecast.Forecast(interval,reception_time,location,newWeatherList)
MainzFc = pyowm.webapi25.forecaster.Forecaster(MainzF)




if mainzFc.will_have_rain():
    #rain.on()
    print('Regen')
else:
    #rain.off()
    print('Kein Regen')
if mainzFc.will_have_sun():
    #sunny.on()
    print('Sonne')
else:
    #sunny.off()
    print('keine Sonne')
if (mainzFC.most_hot().get_temperature(unit='celsius') < 7):
    #cold.on()
    print('Kalt')
else:
    #cold.off()
    print('nicht Kalt')

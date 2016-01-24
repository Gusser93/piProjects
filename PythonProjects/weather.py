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
mainzFc = owm.three_hours_forecast(mainzId, limit=3)



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

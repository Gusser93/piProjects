from gpiozero import LED
#from time import sleep
import pyowm

sunny = LED(17)
rain = LED(18)
freez = LED(19)

sunny.on()
sleep(1)
rain.on()
sleep(1)
freez.on()
sleep(1)
sunny.off()
rain.off()
freez.off()

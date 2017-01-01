from neopixel import *
import re

global NUM_DIGITS
NUM_DIGITS = 0

addresses = [3, 4, 2, 0, 8, 6, 5, 7, 9, 1]

led_states = []
colors_on = []
colors_off = []

global strip
strip = 0

def write(number):
	global strip
	clear(False)
	number = str(number)
	number = re.sub('[^0-9]','', number)
	places = len(str(number))

	for i in range(places):
		push_digit(int(number[i]),i)
	show()

def write_digit(number,address):
	offset = address*20
	L1 = (addresses[number])+offset
	L2 = (addresses[number]+10)+offset

	i = offset
	end = i+20
	while i < end:
		led_states[i] = 0
		i+=1

	led_states[L1] = 1
	led_states[L2] = 1
	show()

def push_digit(number,address):
	global strip

	digit = []
	for i in range(20):
		digit.append(0)

	L1 = 19-(addresses[number])
	L2 = 19-(addresses[number]+10)

	digit[L1] = 1
	digit[L2] = 1

	for i in range(20):
		del led_states[-1]
		led_states.insert(0,digit[i])

def show():
	for i in range(LED_COUNT):
		if led_states[i] == 1:
			strip.setPixelColor(i, colors_on[i/20])
		if led_states[i] == 0:
			strip.setPixelColor(i, colors_off[i/20])
	strip.show()

def clear(show_change = True):
	global strip
	for i in range(LED_COUNT):
		led_states[i] = 0
		strip.setPixelColor(i, Color(0,0,0))
	if show_change == True:
		show()

def color_on(r,g,b, index = -1):
	if index == -1:
		for i in range(LED_COUNT/20):
			colors_on[i] = Color(r,g,b)
	else:
		colors_on[index] = Color(r,g,b)

def color_off(r,g,b, index = -1):
	if index == -1:
		for i in range(LED_COUNT/20):
			colors_off[i] = Color(r,g,b)
	else:
		colors_off[index] = Color(r,g,b)

def begin(digit_count):
	global strip
	global NUM_DIGITS
	global LED_COUNT

	NUM_DIGITS = digit_count
	LED_COUNT = NUM_DIGITS*20

	LED_PIN        = 18             # GPIO pin connected to the pixels (must support PWM!).
	LED_FREQ_HZ    = 800000         # LED signal frequency in hertz (usually 800khz)
	LED_DMA        = 5              # DMA channel to use for generating signal (try 5)
	LED_BRIGHTNESS = 255            # Set to 0 for darkest and 255 for brightest
	LED_INVERT     = False          # True to invert the signal (when using NPN transistor level shift)
	LED_CHANNEL    = 0
	LED_STRIP      = ws.SK6812_STRIP

	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()
	for i in range(LED_COUNT):
		led_states.append(0)

	for i in range(LED_COUNT/20):
		colors_on.append(Color(255,255,255))
		colors_off.append(Color(0,0,0))

	clear()

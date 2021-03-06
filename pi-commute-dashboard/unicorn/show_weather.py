try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
from transport import TrainStatus
import time
from datetime import datetime

from .icons import get as get_icon
from .icons import print_icon

from .digits import get as get_digit
from .digits import print_digit

from weather import WeatherCondition

from .fade import fade_in
from .fade import fade_out

u_width, u_height = unicorn.get_shape()

def show_weather_report(weather_report, is_return):    
    start_y = u_height
    start_x = 3

    if weather_report.type == WeatherCondition.THUNDERSTORM:
        r1, g1, b1 = (32, 32, 32)
        r2, g2, b2 = (96, 96, 96)
        r1, g1, b1 = (255, 255, 0)
        matrix = get_icon('thunderstorm')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if weather_report.type == WeatherCondition.DRIZZLE:
        r1, g1, b1 = (32, 32, 32)
        r2, g2, b2 = (96, 96, 96)
        r3, g3, b3 = (0, 0, 255)
        matrix = get_icon('drizzle')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if weather_report.type == WeatherCondition.RAIN:
        r1, g1, b1 = (32, 32, 32)
        r2, g2, b2 = (96, 96, 96)
        r3, g3, b3 = (0, 0, 255)
        matrix = get_icon('rain')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if weather_report.type == WeatherCondition.SNOW:
        r1, g1, b1 = (255, 255, 255)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('snow')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if weather_report.type == WeatherCondition.CLEAR:
        r1, g1, b1 = (255, 255, 0)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('clear')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if weather_report.type == WeatherCondition.CLOUDS:
        r1, g1, b1 = (32, 32, 32)
        r2, g2, b2 = (96, 96, 96)
        r3, g3, b3 = (192, 192, 192)
        matrix = get_icon('cloud')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if weather_report.type == WeatherCondition.UNKNOWN:
        r1, g1, b1 = (255, 255, 255)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('question')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)

    show_direction(is_return)
    show_temperature(weather_report.temp_c)

    fade_in()
    time.sleep(5)
    fade_out()

def show_direction(is_return):
    start_y = u_height - 10 - 1
    start_x = 1

    if is_return:
        r1, g1, b1 = (0, 0, 255)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('small_arrow_down')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    else:
        r1, g1, b1 = (0, 255, 0)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('small_arrow_up')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)

def show_temperature(temp_c):
    start_y = u_height - 10 - 1
    start_x = 5 + 1 + 1

    r, g, b = (255, 255, 255)

    if temp_c < 10:
        r, g, b = (0, 128, 255)    
    if temp_c < 20:
        r, g, b = (128, 64, 32)
    else: 
        r, g, b = (255, 128, 0)

    for digit in list(str(int(temp_c))):
        matrix = get_digit(digit)
        print_digit(unicorn, matrix, start_x, start_y, r, g, b)
        start_x = start_x + 4
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

import time
import math

from .digits import get
from .digits import print_digit

from .fade import fade_in
from .fade import fade_out

u_width, u_height = unicorn.get_shape()

def show_car_journey(car_journey):
    start_y = u_height - 1
    start_x = 0

    for digit in list(str(math.ceil(car_journey.time_in_seconds / 60))):
        matrix = get(digit)
        print_digit(unicorn, matrix, start_x, start_y, 0, 64, 255)
        start_x = start_x + 4

    fade_in()
    time.sleep(5)
    fade_out()
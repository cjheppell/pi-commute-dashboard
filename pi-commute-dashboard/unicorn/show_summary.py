try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

import time

from .icons import get as get_icon
from .icons import print_icon

from weather import WeatherCondition
from transport import Transport

from .fade import fade_in
from .fade import fade_out

u_width, u_height = unicorn.get_shape()

def show_summary(recommended_transport):
    start_y = u_height - 3
    start_x = 3

    if recommended_transport == Transport.CAR:
        r1, g1, b1 = (32, 32, 32)
        r2, g2, b2 = (0, 255, 255)
        r3, g3, b3 = (255, 255, 0)
        matrix = get_icon('car')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if recommended_transport == Transport.TRAIN:
        r1, g1, b1 = (32, 32, 32)
        r2, g2, b2 = (0, 255, 255)
        r3, g3, b3 = (255, 255, 0)
        matrix = get_icon('train')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if recommended_transport == Transport.HOME:
        r1, g1, b1 = (32, 32, 32)
        r2, g2, b2 = (0, 255, 255)
        r3, g3, b3 = (255, 255, 0)
        matrix = get_icon('question')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    
    fade_in()
    time.sleep(5)
    fade_out()
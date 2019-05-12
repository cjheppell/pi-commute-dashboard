try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
from transport import TrainStatus
import time

from .digits import get as get_digit
from .digits import print_digit
from .icons import get as get_icon
from .icons import print_icon

from .fade import fade_in
from .fade import fade_out

u_width, u_height = unicorn.get_shape()

def show_train_departures(train_departures):
    for departure in train_departures:
        try:
            display_departure_time(departure)
            display_icon(departure.status)
            fade_in()
            time.sleep(5)
            fade_out()
        except Exception as e:
            print(e)
            pass
            
def display_departure_time(departure):
    start_y = u_height - 1
    start_x = 0

    dep_time = departure.departure_time.replace(':', '')

    r, g, b = get_light_colour(departure.status)
    
    for digit in list(dep_time):
        matrix = get_digit(digit)
        print_digit(unicorn, matrix, start_x, start_y, r, g, b)
        start_x = start_x + 4

def display_icon(status):
    start_y = u_height - 5 - 1 - 1
    start_x = 3

    if status == TrainStatus.OK:
        r1, g1, b1 = (0, 255, 0)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('tick')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if status == TrainStatus.LATE:
        r1, g1, b1 = (128, 128, 128)
        r2, g2, b2 = (168, 132, 56)
        r3, g3, b3 = (255, 255, 255)
        matrix = get_icon('hourglass')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if status == TrainStatus.BUS:
        r1, g1, b1 = (255, 0, 0)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('bus')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)
    if status == TrainStatus.CANCELLED:
        r1, g1, b1 = (255, 0, 0)
        r2, g2, b2 = (r1, g1, b1)
        r3, g3, b3 = (r1, g1, b1)
        matrix = get_icon('no_entry')
        print_icon(unicorn, matrix, start_x, start_y, r1, g1, b1, r2, g2, b2, r3, g3, b3)

def get_light_colour(status):
    if status == TrainStatus.OK:
        return (0, 255, 0)
    if status == TrainStatus.LATE or status == TrainStatus.BUS:
        return (255, 128, 128)
    if status == TrainStatus.CANCELLED:
        return (255, 0, 0)
    if status == TrainStatus.UNKNOWN:
        return (255, 255, 255)
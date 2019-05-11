try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
from transport import TrainStatus
import time

from .digits import get
from .digits import print_digit

unicorn.brightness(0.8)
u_width, u_height = unicorn.get_shape()

def show_train_departures(train_departures):
    for departure in train_departures:
        try:
            display_departure_time(departure)
            unicorn.show()
            time.sleep(5)
            unicorn.off()
            time.sleep(1)
        except Exception as e:
            print(e)
            pass
            
def display_departure_time(departure):
    start_y = u_height - 1
    start_x = 0

    dep_time = departure.departure_time.replace(':', '')

    r, g, b = get_light_colour(departure.status)
    
    for digit in list(dep_time):
        matrix = get(digit)
        print_digit(unicorn, matrix, start_x, start_y, r, g, b)
        start_x = start_x + 4

def get_light_colour(status):
    if status == TrainStatus.OK:
        return (0, 255, 0)
    if status == TrainStatus.LATE:
        return (255, 128, 128)
    if status == TrainStatus.CANCELLED:
        return (255, 0, 0)
    if status == TrainStatus.UNKNOWN:
        return (255, 255, 255)
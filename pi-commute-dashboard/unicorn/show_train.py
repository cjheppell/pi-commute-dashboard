try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
from transport import TrainStatus
import time

unicorn.rotation(90)
unicorn.brightness(0.8)
u_width, u_height = unicorn.get_shape()

def show_train_departures(train_departures):
    for departure in train_departures:
        try:
            display_departure(departure)
            time.sleep(5)
            unicorn.off()
            time.sleep(1)
        except:
            pass

def display_departure(departure):
    display_traffic_light(departure)
    display_departure_time(departure)

def display_departure_time(departure):
    pass

def display_traffic_light(departure):
    light_width = 2
    light_height = 2
    (r, g, b) = get_light_colour(departure.status)
    
    start_y = u_height / 2 + 2
    start_x = 0 + light_width

    for x in range (light_width):
        for y in range(light_height):
            unicorn.set_pixel(start_x + x, start_y + y, r, g, b)
    
    unicorn.show()

def get_light_colour(status):
    if status == TrainStatus.OK:
        return (0, 255, 0)
    if status == TrainStatus.LATE:
        return (255, 128, 128)
    if status == TrainStatus.CANCELLED:
        return (255, 0, 0)
    if status == TrainStatus.UNKNOWN:
        return (255, 255, 255)
import time

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

def fade_in():
    brightness = 0.0
    unicorn.brightness(brightness)
    for i in range(1, 11):
        brightness = i / 10
        unicorn.brightness(brightness)
        unicorn.show()
        time.sleep(0.01)

def fade_out():
    for i in range(10, -1, -1):
        brightness = i / 10
        unicorn.brightness(brightness)
        unicorn.show()
        time.sleep(0.01)
    
    unicorn.off()
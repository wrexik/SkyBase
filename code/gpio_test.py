import gpiod
import time
import subprocess

CHIP = "/dev/gpiochip0"
LED_LINE = 115
BUTTON_LINE = 116
RUN_SCRIPT = "/home/radxa/run.sh"

chip = gpiod.Chip(CHIP)
led = chip.get_line(LED_LINE)
button = chip.get_line(BUTTON_LINE)

led.request(consumer="led_blink", type=gpiod.LINE_REQ_DIR_OUT)
button.request(consumer="button", type=gpiod.LINE_REQ_DIR_IN)

print(f"Blinking LED on line {LED_LINE}, waiting for button press on line {BUTTON_LINE}")
print("Press Ctrl+C to exit")

try:
    while True:
        led.set_value(1)
        time.sleep(0.5)
        led.set_value(0)
        time.sleep(0.5)

        if button.get_value() == 1:
            print("Button pressed! Running run.sh...")
            subprocess.run(["bash", RUN_SCRIPT])
            time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    led.release()
    button.release()

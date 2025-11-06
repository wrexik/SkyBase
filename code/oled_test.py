import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

counter = 0
while True:
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    draw.text((0, 0), "Radxa ZERO 3W", font=font, fill=255)
    draw.text((0, 16), f"Count: {counter}", font=font, fill=255)
    oled.image(image)
    oled.show()
    counter += 1
    time.sleep(1)
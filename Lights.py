import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D12, 30)

pixels[0] = (255, 0, 0)
time.sleep(15)
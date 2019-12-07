import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D12, 30)

pixels.fill((0, 255, 0, 255))
time.sleep(15)
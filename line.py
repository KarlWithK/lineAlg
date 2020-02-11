from display import *
from draw import *

s = new_screen()
c = [0, 255, 0]

# octants 1 and 5
draw_line(69, 69, 420, 420, s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')

from example import detect_document
from utilities.io import load_image
from utilities.visualization import show_image
from core.image_handling import get_input

# detect_document('images/base_scan.png')

blank = load_image('images/test.png')
scanned = load_image('images/base_scan.png')

diff = get_input(blank, scanned)
show_image(diff)

show_image(scanned)
show_image(blank, True)

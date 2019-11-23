from utilities.io import load_image
from core.interaction import label_points

# Load image
blank = load_image('images/test.png')

# Open tagging window
label_points(blank)

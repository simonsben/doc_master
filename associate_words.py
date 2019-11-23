from utilities.io import load_image, save_image
from utilities.visualization import bound_words, show_image
from core.image_handling import get_input, perform_ocr
from pandas import DataFrame

blank = load_image('images/test.png')
scanned = load_image('images/base_scan.png')

input_content = get_input(blank, scanned)
save_image(input_content, 'images/input_content.png')

response = perform_ocr('images/input_content.png')

fig = show_image(input_content)
bound_words(fig, response)

data = DataFrame(response, columns=('word', 'x', 'y', 'width', 'height'))
data.to_csv('data/word_bounds.csv')

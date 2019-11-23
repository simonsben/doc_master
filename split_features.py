from pandas import read_csv
from utilities.io import load_image
from utilities.visualization import show_image
from core.associate import associate_input


# word, x, y, width, height
def get_center(bound):
    x_mid = bound[1] + (bound[3] / 2)
    y_mid = bound[2] + (bound[4] / 2)

    return [x_mid, y_mid]


features = read_csv('data/feature_points.csv', index_col=0).values
base = load_image('images/test.png')
bounds = read_csv('data/word_bounds.csv', index_col=0).values

terms = [[bound[0]] + get_center(bound) for bound in bounds]

bla = associate_input(features, terms)
for index, thing in enumerate(bla):
    print(index, bla[thing])

# fig = show_image(base, True)

# for index, feature in enumerate(features):
#     x, y = feature
#     for term, x_mid, y_mid in terms:
#         if x_mid > x and abs(y_mid - y) < 50:
#             print(index, 'candidate', term)

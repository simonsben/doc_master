from pandas import read_csv
from utilities.io import load_image
from utilities.visualization import show_image, bound_words, show, show_association
from core.associate import associate_input, clean_associations
from core.image_handling import get_center


features = read_csv('data/feature_points.csv', index_col=0).values
bounds = read_csv('data/word_bounds.csv', index_col=0).values
base = load_image('images/blank_form.png')

terms = [[bound[0]] + get_center(bound) for bound in bounds]

raw_associations = associate_input(features, terms)
associations = clean_associations(raw_associations)
for index, association in enumerate(associations):
    print(index, association)

fig = show_image(base, False)
bound_words(fig, bounds, False)
show_association(fig, raw_associations)

show()

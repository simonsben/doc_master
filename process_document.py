from pandas import read_csv
from utilities.io import load_image, save_image
from utilities.visualization import show_image, bound_words, show, show_association
from core.associate import associate_input, clean_associations
from core.image_handling import get_center, get_input, perform_ocr

# Import images and data
blank_form = load_image('images/blank_form.png')
complete_form = load_image('images/scanned_document.png')
features = read_csv('data/feature_points.csv', index_col=0).values
print('Document loaded.')

# Get form input/content
form_input = get_input(blank_form, complete_form)
save_image(form_input, 'images/form_input.png')
print('Content isolated.')

# Compute bounds
bounds = perform_ocr('images/form_input.png')
input_content = [[bound[0]] + get_center(bound) for bound in bounds]
print('Content digitized.')

# Associate bounds with form features
raw_associations = associate_input(features[:, 1:], input_content)
associations = clean_associations(raw_associations)

# Output information to console
print('\n%20s %20s' % ('Feature', 'Content'))
for feature, association in zip(features, associations):
    print('%20s %20s' % (feature[0], association))

# Make pretty picture
fig = show_image(complete_form, False)
bound_words(fig, bounds, False)
show_association(fig, raw_associations)

show()

from utilities.io import load_image
from utilities.visualization import show_image
from numpy import asarray
from matplotlib.pyplot import hist

a = load_image('images/blank.png')
b = load_image('images/filled.png')

# show_image(a)
c = asarray(a.convert('LA')).copy()
print(c.shape)

c[c < 128] = 0
c[c > 5] = 255

show_image(c, True)

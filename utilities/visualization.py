from matplotlib.pyplot import imshow, show, figure, Rectangle


def show_image(image, hold=False):
    fig = figure()

    imshow(image, cmap='gray')
    if hold:
        show()

    return fig


def bound_words(fig, bounds):
    ax = fig.gca()

    for bound in bounds:
        poly_bounds = list(bound.bounding_poly.vertices)
        base = poly_bounds[0]
        top = poly_bounds[2]

        width = top.x - base.x
        height = top.y - base.y

        ax.add_artist(Rectangle((base.x, base.y), width, height, fill=False, edgecolor='k'))

    show()
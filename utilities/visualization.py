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
        _, x, y, width, height = bound
        ax.add_artist(Rectangle((x, y), width, height, fill=False, edgecolor='k'))

    show()
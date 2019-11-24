from matplotlib.pyplot import imshow, show, figure, Rectangle, Circle


def show_image(image, hold=False):
    fig = figure()

    imshow(image, cmap='gray')
    if hold:
        show()

    return fig


def bound_words(fig, bounds, hold=True):
    ax = fig.gca()

    for bound in bounds:
        _, x, y, width, height = bound
        ax.add_artist(Rectangle((x, y), width, height, fill=False, edgecolor='k'))

    if hold:
        show()


def show_association(fig, associations):
    ax = fig.gca()
    for association in associations:
        x, y = association[:2]
        ax.add_artist(Circle((x, y), radius=30, alpha=.65))

        for child in association[2:]:
            word, x_mid, y_mid = child
            ax.plot([x, x_mid], [y, y_mid], c='k')

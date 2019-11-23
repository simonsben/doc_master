from matplotlib.pyplot import imshow, show, figure


def show_image(image, hold=False):
    fig = figure()

    imshow(image, cmap='gray')
    if hold:
        show()

    return fig

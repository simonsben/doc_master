from utilities.visualization import show_image, show
from utilities.io import save_points
from matplotlib.pyplot import close, Circle


def label_points(image):
    fig = show_image(image)
    points = []

    def handle_keypress(event):
        print('Key pressed, closing.')
        save_points(points)
        close()

    def handle_click(event):
        x, y = event.xdata, event.ydata
        points.append((x, y))

        print('Point at (%d, %d)' % (x, y))
        ax = fig.gca()
        ax.add_artist(Circle((x, y), radius=50))
        show()

    fig.canvas.mpl_connect('key_press_event', handle_keypress)
    fig.canvas.mpl_connect('button_press_event', handle_click)
    show()


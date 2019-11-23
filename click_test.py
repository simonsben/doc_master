import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
y = x**2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)

coords = []

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print ('x = %d, y = %d'%(
        ix, iy))

    global coords
    coords.append((ix, iy))

    # if len(coords) == 2:
    #     fig.canvas.mpl_disconnect(cid)

    return coords


def press(event):
    print(event.key)
    fig.canvas.mpl_disconnect(cid)


fig.canvas.mpl_connect('key_press_event', press)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
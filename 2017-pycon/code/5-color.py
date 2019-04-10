import numpy as np
import matplotlib
matplotlib.use('tkagg')
matplotlib.rcParams['toolbar'] = 'toolmanager'
import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolToggleBase
from matplotlib import colors
from tkinter.colorchooser import askcolor


class ThatColor(ToolToggleBase):
    description = "Change line color"
    def __init__(self, *args, **kwargs):
        self.pid = None
        ToolToggleBase.__init__(self, *args, **kwargs)
        self.converter = colors.ColorConverter()

    def enable(self, *args, **kwargs):
        self.toolmanager.message_event('enable')
        self.pid = self.figure.canvas.mpl_connect('pick_event', self.onpick)

    def disable(self, *args, **kwargs):
        self.figure.canvas.mpl_disconnect(self.pid)
        self.pid = None

    def onpick(self, event):
        thisline = event.artist
        original = thisline.get_color()
        if original is None:
            original = thisline.get_markerfacecolor()
        original = self.converter.to_rgb(original)
        original = colors.rgb2hex(original)
        color = askcolor(original)[1]
        thisline.set_color(color)
        self.figure.canvas.draw()


x = np.linspace(0, 2 * np.pi, 50)


def get_y(phase):
    y = np.sin(x + phase)
    y2 = y + 0.1 * np.random.normal(size=x.shape)
    return y, y2


fig, ax = plt.subplots()
fig.canvas.manager.toolmanager.add_tool('color', ThatColor)
fig.canvas.manager.toolbar.add_tool('color', 'io')


phases = [0, 1.0, 2.0, 3.0]

for i, phase in enumerate(phases):
    y, y2 = get_y(phase)
    line = ax.plot(x, y, gid=str(i), picker=5, lw=4)
    ax.plot(x, y2, 'o', gid=str(i), picker=5, markersize=8)

plt.show()

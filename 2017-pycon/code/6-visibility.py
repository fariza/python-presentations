import numpy as np
import matplotlib
matplotlib.use('tkagg')
matplotlib.rcParams['toolbar'] = 'toolmanager'
import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolToggleBase


class VisibilityTool(ToolToggleBase):
    description = "Toggle line visivility"
    def __init__(self, *args, **kwargs):
        self._key_press_handler_id = None
        ToolToggleBase.__init__(self, *args, **kwargs)

    def enable(self, *args, **kwargs):
        self.toolmanager.keypresslock(self)
        self._key_press_handler_id = self.canvas.mpl_connect(
            'key_press_event', self.set_lines_visibility)

    def disable(self, *args, **kwargs):
        self.toolmanager.keypresslock.release(self)
        self.canvas.mpl_disconnect(self._key_press_handler_id)

    def set_lines_visibility(self, event):
        if event.key is None:
            return
        for ax in self.figure.get_axes():
            for line in ax.get_lines():
                if line.get_gid() == event.key:
                    state = line.get_visible()
                    line.set_visible(not state)
                    self.toolmanager.message_event("Group %s visibility changed" % event.key)
        self.figure.canvas.draw()


x = np.linspace(0, 2 * np.pi, 50)


def get_y(phase):
    y = np.sin(x + phase)
    y2 = y + 0.1 * np.random.normal(size=x.shape)
    return y, y2


fig, ax = plt.subplots()
fig.canvas.manager.toolmanager.add_tool('vis', VisibilityTool)
fig.canvas.manager.toolbar.add_tool('vis', 'io')


phases = [0, 1.0, 2.0, 3.0]

for i, phase in enumerate(phases):
    y, y2 = get_y(phase)
    line = ax.plot(x, y, gid=str(i), picker=5, lw=4)
    ax.plot(x, y2, 'o', gid=str(i), picker=5, markersize=8)

plt.show()

import matplotlib
matplotlib.use('TkAgg')
matplotlib.rcParams['toolbar'] = 'toolmanager'
import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolToggleBase

class ToggleLegend(ToolToggleBase):
    description = 'Toggle the legend'
    default_toggled = True
    default_keymap = 'l'

    def visibility(self, state):
        for leg in list(self.figure.legends):
            leg.set_visible(state)
        for a in self.figure.get_axes():
            leg = a.get_legend()
            if leg:
                leg.set_visible(state)
        self.figure.canvas.draw_idle()

    def enable(self, event):
        self.visibility(True)

    def disable(self, event):
        self.visibility(False)

fig = plt.figure()
plt.plot([1, 2, 3], label='Super data')
plt.legend()
fig.canvas.manager.toolmanager.add_tool('legend', ToggleLegend)
fig.canvas.manager.toolbar.add_tool('legend', 'io')
plt.show()

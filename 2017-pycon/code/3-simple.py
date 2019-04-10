import matplotlib
matplotlib.use('tkAgg')
matplotlib.rcParams['toolbar'] = 'toolmanager'
import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolBase


class ExtraSimple(ToolBase):
    description = 'Encourage yourself'
    default_keymap = 'C'

    def trigger(self, *args, **kwargs):
        self.toolmanager.message_event("You are doing great!!")

fig = plt.figure()
plt.plot([1, 2, 3])
fig.canvas.manager.toolmanager.add_tool('simple', ExtraSimple)
fig.canvas.manager.toolbar.add_tool('simple', 'navigation')
plt.show()

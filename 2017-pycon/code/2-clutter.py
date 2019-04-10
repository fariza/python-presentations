import matplotlib
matplotlib.use('tkAgg')
matplotlib.rcParams['toolbar'] = 'toolmanager'
import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([1, 2, 3])
fig.canvas.manager.toolbar.remove_toolitem('forward')
fig.canvas.manager.toolbar.add_tool('zoom', 'foo')
fig.canvas.manager.toolmanager.remove_tool('save')
plt.show()

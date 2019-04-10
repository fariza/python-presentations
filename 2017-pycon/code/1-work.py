import matplotlib
# matplotlib.use('GTK3Agg')
matplotlib.use('tkAgg')
matplotlib.rcParams['toolbar'] = 'toolmanager'
import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([1, 2, 3], label='Super data')
plt.show()

import matplotlib.pyplot as plt

figure  = plt.figure()
ax = figure.add_subplot(111)

X = test.temporal['u_y'] - test.temporal['u_ydark']
Y = test.temporal['s2_y'] - test.temporal['s2_ydark']
ax.plot(X, Y, label='Data')
ax.plot(X, test.K * X, linestyle='--', label='Fit')

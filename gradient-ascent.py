import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (5, 3) # (w, h)
plt.rcParams["figure.dpi"] = 200

m = 100
x = 2 * np.random.rand(m)
y = 5 + 2 * x + np.random.randn(m)
plt.scatter(x, y)
plt.show()


from scipy.stats import linregress
slope, intercept = linregress(x, y)[:2]
print(f"slope: {slope:.3f}, intercept: {intercept:.3f}")

# Reward Function

x = np.array([np.ones(m), x]).transpose()
def accuracy(x, y, theta):
    return - 1 / m * np.sum((np.dot(x, theta) - y) ** 2)
# Gradient Function
def gradient(x, y, theta):
    return -1 / m * x.T.dot(np.dot(x, theta) - y)

num_epochs = 500
learning_rate = 0.1

def train(x, y):
    accs = []
    thetas = []
    theta = np.zeros(2)
    for _ in range(num_epochs):
        # keep track of accuracy and theta over time
        acc = accuracy(x, y, theta)
        thetas.append(theta)
        accs.append(acc)
        
        # update theta
        theta = theta + learning_rate * gradient(x, y, theta)
        
    return theta, thetas, accs

theta, thetas, accs = train(x, y)
print(f"slope: {theta[1]:.3f}, intercept: {theta[0]:.3f}")

plt.plot(accs)
plt.xlabel('Epoch Number')
plt.ylabel('Accuracy');
plt.show()

# 3D surface

from mpl_toolkits.mplot3d import Axes3D
i = np.linspace(-10, 20, 50)
j = np.linspace(-10, 20, 50)
i, j = np.meshgrid(i, j)
k = np.array([accuracy(x, y, th) for th in zip(np.ravel(i), np.ravel(j))]).reshape(i.shape)
fig = plt.figure(figsize=(9,6))
ax = fig.gca(projection='3d')
ax.plot_surface(i, j, k, alpha=0.2)
ax.plot([t[0] for t in thetas], [t[1] for t in thetas], accs, marker="o", markersize=3, alpha=0.1);
ax.set_xlabel(r'$\theta_0$'); ax.set_ylabel(r'$\theta_1$')
ax.set_zlabel("Accuracy");

plt.show()
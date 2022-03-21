import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

plt.plot(x, y)
# plt.show()

x = np.linspace(-5, 5, 20)
plt.plot(x,x**2, 'ko')
plt.plot(x, x**3, 'r*')
plt.title('hohoho')
# plt.show()

x = np.arange(11)
y = x**2
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.title('Scatter')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 2, 3)
plt.bar(x, y)
plt.title('Bar')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 2, 4)
plt.loglog(x, y)
plt.title('Loglog')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('img.pdf')

# plt.show()
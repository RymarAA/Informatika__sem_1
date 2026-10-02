import matplotlib.pyplot as plt
import numpy as np

pos = 0
scale = 3
values = np.random.normal(pos, 10, 10)
values1 = np.random.normal(pos, 10, 100)
values2 = np.random.normal(pos, 10, 1000)
values3 = np.random.normal(pos, 10, 10000)


fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)


ax1.hist(values, 20)
ax2.hist(values1, 200)
ax3.hist(values2, 2000)
ax4.hist(values3, 20000)

plt.savefig('barchart.png', dpi=300)
fig.show()
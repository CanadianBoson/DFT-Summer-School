import numpy as np
import matplotlib.pylab as plt

results = {}

#Mval = []
#size = 10
#while size < 300:
#    Mval.append(size)
#    size *= 2.**.5
#Nrepeated = len(Mval)

Mval = []
Mval += [200 * 2**n for n in range(12)]
Mval += [280 * 2**n for n in range(12)]

Mval.sort()

with open('timings.txt') as fd:
    for line in fd:
        token, num = line.split()
        num = float(num)
        results.setdefault(token, []).append(num)

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111)


ax.axvline(354, color='k', ls='-', lw=2)#, label='L2 cache')
ax.text(370, 1.5e-2, 'L2 cache')

ax.grid()
for key in 'ikj kij ijk jik jki kji'.split():
    y  = np.array(results[key])
    #y[:Nrepeated] /= 100.
    N = len(y)
    ax.loglog(Mval[:N], y, 'o-', label=key)

ax.set_xticks(Mval[:N])
sizes = 3 * np.array(Mval[:N])**2 * 8 / 1e6
ax.set_xticklabels(['{}\n{:.1f} MB'.format(M, size)
                    for M, size in zip(Mval[:N], sizes)], rotation=45)
ax.axis(xmin=Mval[0], xmax=Mval[N - 1])

ax.legend(loc='upper left', ncol=3)
ax.set_xlabel('Matrix size & total memory allocation')
ax.set_ylabel('Multiplication time [s]')
fig.subplots_adjust(bottom=0.25, top=.95, right=.95, left=.15)
fig.savefig('timings-matmul.pdf')
plt.show()

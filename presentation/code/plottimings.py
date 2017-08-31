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
ax.text(330, 3e-2, 'L2', rotation=90)

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
ax.axis(xmin=Mval[0], xmax=Mval[N - 1], ymax=1e2)

ax.legend(loc='upper left', ncol=3)
ax.set_xlabel('Matrix size & total memory allocation')
ax.set_ylabel('Multiplication time [s]')
fig.subplots_adjust(bottom=0.25, top=.95, right=.95, left=.15)
fig.savefig('timings-matmul.pdf')

blastimes = """3.303000e-03
8.559000e-03
2.070800e-02
3.444300e-02
6.907800e-02
1.762290e-01
5.264210e-01
1.386151e+00
4.005219e+00
1.092985e+01
3.207603e+01""".split()
blastimes = np.array(blastimes).astype(float)

ax.plot(Mval[:N], blastimes[:N], 'ok-', lw=2, label='OpenBLAS')
ax.axis(ymin=1e-3)
ax.text(Mval[N-4], blastimes[N-4] * 6*2.6, 'dgemm from OpenBLAS', rotation=21)

fig.savefig('timings-matmul-blas.pdf')

plt.show()

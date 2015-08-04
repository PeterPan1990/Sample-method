
# _*_ coding=utf-8 _*_

__author__ = 'young'
__date__ = '2015-8-4'
__doc__ = 'this scipt is a simple implements of rejection sample. use uniform to sample a multiple-gaussian'

from pylab import *
from numpy import *

def qSample():
    return random.rand()*4

def p(x):
    return 0.3*exp(-(x-0.3)**2) + 0.3*exp(-(x-2.)**2/0.3)

def rejection(nsample):
    M = 0.75
    sample = zeros(nsample, dtype=float)
    count = 0

    for i in xrange(nsample):
        accept = False
        while not accept:
            x = qSample()
            u = random.rand() * M
            if u < p(x):
                accept = True
                sample[i] = x
            else:
                count += 1
    print count
    return sample

x = arange(0, 4, 0.01)
x2 = arange(-0.5, 4.5, 0.1)
realdata = 0.3*exp(-(x-0.3)**2) + 0.3*exp(-(x-2.)**2/0.3)
box = ones(len(x2)) * 0.75
box[:5] = 0
box[-5:] = 0

figure("the first")
plot(x, realdata, 'k', lw=2)
plot(x2, box, 'k--', lw=2)
xlabel('x', fontsize=18)
ylabel('p', fontsize=18)


import time
t0 = time.time()
sample = rejection(10000)
t1 = time.time()
print "Time: ", t1 - t0

figure("the second")
hist(sample, 100, normed=1, fc='k')
xlabel('x', fontsize=18)
ylabel('p(x)', fontsize=18)
axis([-0.5, 4.5, 0, 1])
show()

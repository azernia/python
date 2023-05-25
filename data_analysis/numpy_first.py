"""
    random模块的normalvariate(mu,sigma)方法可以生成符合正态分布的随机数，
    其中mu, sigma分别对应公式中的期望值μ, 标准差σ，当mu=0, sigma=1为标准正态分布
"""
import random
import matplotlib.pyplot as plt

walk = []
for i in range(1000):
    walk.append(random.normalvariate(0, 1))

plt.hist(walk, bins=30)
plt.show()
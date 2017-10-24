import fun.basic_pso as bpso
import fun.fit_weight_pso as fwpso
import matplotlib.pyplot as plt
import numpy as np

one_pso = bpso.PSO(pN=30,dim=5,max_iter=100)
one_pso.init_Population()
fitness_1 = one_pso.iterator()
two_pso = fwpso.weight_PSO(pN=30, dim=5, max_iter=100)
two_pso.init_Population()
fitness_2 = two_pso.iterator(1)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_xlabel('iterators')
ax1.set_ylabel('fitness')
ax1.set_title('basic_pso')
fitness_1 = np.array(fitness_1)
t_1 = np.array([t for t in range(0, 100)])
fitness_2 = np.array(fitness_2)
t_2 = np.array([t for t in range(0, 100)])
ax1.plot(t_1, fitness_1, 'r--', t_2, fitness_2, 'b')
plt.show()
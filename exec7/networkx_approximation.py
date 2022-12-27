import networkx as nx
import matplotlib.pyplot as plt
import math


#To solve this question i helped noamya shani and https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
fig, axs = plt.subplots(2, 3, figsize=(10,13))
axs[0, 0].set_title('probability: 0.15')
axs[0, 1].set_title('probability: 0.35')
axs[0, 2].set_title('probability: 0.50')
axs[1, 0].set_title('probability: 0.65')
axs[1, 1].set_title('probability: 0.80')
axs[1, 2].set_title('probability: 0.90')
for ax in axs.flat:
    ax.set(xlabel='num of vertex', ylabel='size of max clique')

exact_solution = []
approx_solution = []
ratio_approx = []
all_plots = [(0,0),(0,1),(0,2), (1,0),(1,1),(1,2)]
loc = 0

for prob in [0.15, 0.35, 0.5, 0.65, 0.8, 0.9]:
    for num_of_vertex in range(1, 50):
        graph = nx.gnp_random_graph(num_of_vertex, prob)
        m = len(nx.algorithms.approximation.max_clique(graph))
        all_cliques = list(nx.find_cliques(graph))
        max_clique_len = len(max(all_cliques, key=len))
        if num_of_vertex != 1:
            ratio = num_of_vertex / (math.log(num_of_vertex) ** 2)
        else:
            ratio = 0
        ratio_approx.append(ratio)
        exact_solution.append(max_clique_len)
        approx_solution.append(m)
    axs[all_plots[loc]].plot(exact_solution, 'blue', approx_solution, 'yellow', ratio_approx, 'green')
    loc = loc + 1
    exact_solution.clear()
    approx_solution.clear()
    ratio_approx.clear()
fig.figure.legend(["real_approx", "real max clique", "approx ratio"])
plt.show()




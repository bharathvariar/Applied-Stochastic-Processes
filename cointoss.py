from turtle import color
from xml.dom import IndexSizeErr
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter


def coin_flip(num_flips=100, probability=0.5):
    '''
    Flip coin num_flips times with probability for each side = 'probability'

    returns: array of size 1 x num_flips with output of each flip
    '''
    result = np.random.binomial(n=1, p=probability, size=(1, num_flips))
    return np.where(result == 1, 'H', 'T')[0]


def longest_heads(results):
    max_heads = 0
    counter = 0
    for i in range(len(results)):
        if (results[i] == 'H'):
            counter += 1
        else:
            if (counter > max_heads):
                max_heads = counter
            counter = 0
    return max_heads


def plot_results(experiment_results):

    average = np.mean(experiment_results)
    max_head_chain = np.max(experiment_results)
    min_head_chain = np.min(experiment_results)
    hist_dict = Counter(experiment_results)
    indices = list(hist_dict.keys())
    values = list(hist_dict.values())
    fig, ax = plt.subplots()
    bars = ax.bar(indices, values, width=0.5, color='purple')
    ax.bar_label(bars)
    plt.xlabel("Longest Head Chain")
    plt.text(
        9, 2300, f'Average Longest Head Chain: {average}\nLongest Head Chain: {max_head_chain}\nShortest Head Chain: {min_head_chain}')
    plt.xticks(np.arange(0, max_head_chain + 2, step=1))
    plt.ylabel("Frequency")
    plt.title("Longest chain of heads in 10,000 experiments of 100 flips")
    plt.show()
    return


experiment_results = []
for i in range(10000):
    experiment_results.append(longest_heads(coin_flip()))

plot_results(experiment_results=experiment_results)
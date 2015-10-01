import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

runs = 3

def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

for i in range(1, runs+1):
    max_fitnesses = []
    num_species = []
    num_genes = []
    gens = 0

    with open("run"+str(i)+"/averages", 'r') as f:
        for line in f:
            ind_fit = line.find("Max fitness of generation")
            if ind_fit != -1:
                gens += 1
                max_fitnesses.append(float(line[ind_fit:].split(':')[-1].rstrip()))
            ind_spec = line.find("Number of species in generation")
            if ind_spec != -1:
                num_species.append(float(line[ind_spec:].split(':')[-1].rstrip()))
            ind_gen = line.find("Number of genes in generation for best individual")
            if ind_gen != -1:
                num_genes.append(float(line[ind_gen:].split(':')[-1].rstrip()))

    generations = list(xrange(gens))
    plt.clf()
    yMA = movingaverage(max_fitnesses, 3)
    plt.plot(generations[len(generations)-len(yMA):],yMA, label='Moving Averages')
    plt.plot(generations, max_fitnesses, label='Max fitness')
    plt.xlabel('Generations')
    plt.ylabel('Max Fitness over generations')
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('max_fitnesses_over_generations_run_'+str(i))
    
    plt.clf()
    yMA = movingaverage(num_species, 3)
    plt.plot(generations[len(generations)-len(yMA):],yMA, label='Moving Averages')
    plt.plot(generations, num_species, label='Number of species')
    plt.xlabel('Generations')
    plt.ylabel('Number of species over generations')
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('number_of_species_over_generations_run_'+str(i))
    
    plt.clf()
    yMA = movingaverage(num_genes, 3)
    plt.plot(generations[len(generations)-len(yMA):],yMA, label='Moving Averages')
    plt.plot(generations, num_genes, label='Number of genes')
    plt.xlabel('Generations')
    plt.ylabel('Number of genes from best individual over generations')
    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('number_of_genes_over_generations_run_'+str(i))
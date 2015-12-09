""" 2-input XOR example """
from neat import population, visualize
from neat import nn

INPUTS = [[0, 0], [0, 1], [1, 0], [1, 1]]
OUTPUTS = [0, 1, 1, 0]


def eval_fitness(genomes):
    for g in genomes:
        net = nn.create_feed_forward_phenotype(g)

        error = 0.0
        for inputs, expected in zip(INPUTS, OUTPUTS):
            # Serial activation propagates the inputs through the entire network.
            output = net.serial_activate(inputs)
            error += (output[0] - expected) ** 2

        # When the output matches expected for all inputs, fitness will reach
        # its maximum value of 1.0.
        g.fitness = 1 - error


def run():
    pop = population.Population('xor2_config')
    pop.epoch(eval_fitness, 300)

    winner = pop.most_fit_genomes[-1]
    print 'Number of evaluations: %d' % winner.ID

    # Verify network output against training data.
    print '\nBest network output:'
    net = nn.create_feed_forward_phenotype(winner)
    for inputs, expected in zip(INPUTS, OUTPUTS):
        output = net.serial_activate(inputs)
        print "expected %1.5f got %1.5f" % (expected, output[0])

    print nn.create_feed_forward_function(winner)

    # Visualize the winner network and plot statistics.
    visualize.plot_stats(pop.most_fit_genomes, pop.avg_fitness_scores)
    visualize.plot_species(pop.species_log)
    visualize.draw_net(winner, view=True)


if __name__ == '__main__':
    run()
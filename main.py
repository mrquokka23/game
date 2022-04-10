# import the pygame module, so you can use it
import pygame
from racer import Car
import math
import os
import neat
import pickle
import gzip
import random
from main_menu import mainMenu
from game import main

# define a main function

from variables import options as opt

def save_checkpoint(self, config, population, species_set, generation):
    filename_prefix = 'neat-checkpoint-'
    """ Save the current simulation state. """
    filename = '{0}{1}'.format(filename_prefix, generation)
    print("Saving checkpoint to {0}".format(filename))

    with gzip.open(filename, 'w', compresslevel=5) as f:
        data = (generation, config, population, species_set, random.getstate())
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
def run(config_path, noOfLoops, noOfGenerations, resolution):

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)


    winner = p.run(main,noOfGenerations)
    with open("nets/winner2.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()



if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config")
    returned = mainMenu(config_path)
    if returned[0] == 1:
        run(config_path, returned[1][0], returned[1][1], returned[1][2])

    #run(config_path)
    # call the main function






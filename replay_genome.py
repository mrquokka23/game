import neat
import pickle
from game import main

def replay_genome(config_path, genome_path="winner.pkl", optionsReturned=(1000, 50, (960, 540))):
    # Load requried NEAT config
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Unpickle saved winner
    with open(genome_path, "rb") as f:
        genome = pickle.load(f)

    # Convert loaded genome into required data structure
    genomes = [(1, genome)]

    # Call game with only the loaded genome
    main(genomes, config, optionsReturned[0], optionsReturned[2])

# import the pygame module, so you can use it
import pygame
from racer import Car
import math
import os
import neat
import pickle
import gzip
import random

# define a main function
def main(genomes, config):
    nets = []
    ge = []
    racers = []

    car = pygame.transform.scale(pygame.image.load("resources/481-4811196_scratch-car-top-down-png.png"), (50, 25))
    carsel = pygame.transform.scale(pygame.image.load("resources/image.png"), (50, 25))

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        racers.append(Car(car, 1030, 200))
        g.fitness = 0
        ge.append(g)

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    bgimg = pygame.image.load("resources/track.jpg")

    line = pygame.image.load("resources/line.png")
    pygame.display.set_icon(car)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1920, 1080))
    class Map(pygame.sprite.Sprite):
        def __init__(self, img, resolution):
            self.image = pygame.transform.scale(img, resolution)
            self.mask = pygame.mask.from_threshold(self.image, (255, 255, 255, 255), (255, 255, 255, 255))
            self.rect = self.image.get_rect()
            self.checkpoints = [[(1297,160), (1214, 332)], [(1571,268),(1432,407)], [(1763,639),(1510,590)], [(1500,910),(1378,697)], [(1189,998),(1152,762)], [(884,1013),(899,774)], [(631,980),(720,753)], [(342,847),(490,673)], [(235,739),(423,610)], [(197,451),(409,496)], [(384,260),(489,413)], [(601,174),(657,339)], [(807,130),(834,307)], [(980,120),(980,300)]]


    class Checkpoint(pygame.sprite.Sprite):
        def __init__(self, positions, index, screen):

            self.startPos = positions[0]
            self.endPos = positions[1]
            self.index = index
            self.image = pygame.Surface((1920,1080))
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            #self.rect = self.image.get_rect()
            #self.rect.x = self.startPos[0]
            #self.rect.y = self.startPos[1]
            self.image.fill(0)
            pygame.draw.line(self.image, (255, 255, 0), self.startPos, self.endPos, 2)
            self.mask = pygame.mask.from_surface(self.image)
            self.angle = 0

        def update(self, screen):
            vec = round(math.cos(self.angle * math.pi / 180) * 100), round(math.sin(self.angle * math.pi / 180) * 100)
            pygame.draw.line(self.image, (255, 255, 0), self.startPos, self.endPos, 5)
            self.mask = pygame.mask.from_surface(self.image)




            # self.forwardLine = pygame.draw.line(screen, (255, 0, 0), self.position, (self.position[0] + (math.cos(self.carHeading) * 400), self.position[1] + (math.sin(self.carHeading) * 400)), 1)

    # define a variable to control the main loop
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    deltaT = 0
    running = True

    bg = Map(bgimg, (1920, 1080))
    #Car.update(racer, deltaT, screen, bgimg)
    checkpoints = []
    n = 1
    for checkpoint in bg.checkpoints:
        checkpoints.append(Checkpoint(checkpoint,n,screen))
        n += 1


    # main loop
    while running:

        if deltaT >= 1000:
            running = False
        test = pygame.key.get_pressed()
        # screen.blit(bg.image, (0,0))
        screen.blit(bg.mask.to_surface(), (0, 0))


        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
                quit()





        for racer in racers:
            screen.blit(checkpoints[racer.currentCheckpoint].image, (0, 0))

        if len(racers) <=0:
            running = False
            break


        for x, racer in enumerate(racers):
            if pygame.sprite.collide_mask(checkpoints[racer.currentCheckpoint], racer):
                if racer.currentCheckpoint+1 < checkpoints.__len__():
                    racer.currentCheckpoint+=1
                else:
                    racer.currentCheckpoint = 0
                ge[x].fitness += 20

            output = nets[x].activate((racer.distances[0],racer.distances[1],racer.distances[2],racer.distances[3],racer.distances[4], racer.velocity, racer.steerAngle, racer.acceleration))
            if abs(racer.lastSteerangle-output[0]) > 0.5:
                ge[x].fitness -= 0.5
                if x == 0:
                    print(abs(racer.lastSteerangle-output[0]))


            racer.update(deltaT, screen, bgimg, output[0], output[1], output[2], True)

            if x == 0:
                racer.image = carsel

            if deltaT > 300 and racer.currentCheckpoint == 0:
                ge[x].fitness -= 1000

            if racer.position != racer.lastPosition:
                ge[x].fitness += 0.01
                racer.lastPosition = racer.position
            if racer.acceleration <= 0 or racer.velocity <= 0:
                ge[x].fitness -= 0.1


            if pygame.sprite.collide_mask(racer, bg):
                ge[x].fitness -= 1
                racers.pop(x)
                nets.pop(x)
                ge.pop(x)





        bg.update(screen)




        pygame.display.flip()


        deltaT += 1

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
def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50)
    with open("winner.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config")
    run(config_path)
    # call the main function





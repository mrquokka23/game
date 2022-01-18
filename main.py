# import the pygame module, so you can use it
import pygame
from racer import Car


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    bgimg = pygame.image.load("resources/track.jpg")
    car = pygame.transform.scale(pygame.image.load("resources/481-4811196_scratch-car-top-down-png.png"), (50, 25))
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
            pygame.draw.line(screen, (0, 255, 0), self.startPos, self.endPos, 1)

        def update(self, screen):
            pygame.draw.line(screen, (0, 255, 0), self.startPos, self.endPos, 1)




            # self.forwardLine = pygame.draw.line(screen, (255, 0, 0), self.position, (self.position[0] + (math.cos(self.carHeading) * 400), self.position[1] + (math.sin(self.carHeading) * 400)), 1)

    # define a variable to control the main loop
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    deltaT = 0
    running = True
    racer = Car(car, 1030, 200)
    bg = Map(bgimg, (1920, 1080))
    Car.update(racer, deltaT, screen, bgimg)
    checkpoints = []
    n = 0
    for checkpoint in bg.checkpoints:
        checkpoints.append(Checkpoint(checkpoint,n,screen))


    # main loop
    while running:
        text = myfont.render(str(racer.velocity), False, (255, 255, 255))
        if deltaT >= 1000000:
            running = False
        test = pygame.key.get_pressed()
        # screen.blit(bg.image, (0,0))
        screen.blit(bg.mask.to_surface(), (0, 0))
        screen.blit(text, (0, 0))

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        racer.update(deltaT, screen, bgimg)


        if pygame.sprite.collide_mask(racer, bg):
            screen.blit(myfont.render(str("collided"), False, (0, 0, 0)),(100,100))

        bg.update(screen)
        pygame.display.flip()
        print(pygame.mouse.get_pos())
        deltaT += 1


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

import pygame
from PIL import Image, ImageFilter
from replay_selector import replaySelector
from options import options as optionsmenu
import variables

variables.options = (1000, 50, (960, 540))


def mainMenu(config_path):
    bgimg = pygame.transform.scale(pygame.image.load("resources/menu.jpg"), (1280, 720))
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")
    screen.blit(bgimg , (0, 0))
    font = pygame.font.Font("resources/font.ttf", 20)
    start = font.render("Start a new training", True, (0, 0, 0))
    options = font.render("Options", True, (0, 0, 0))
    replay = font.render("Replay neural nets", True, (0, 0, 0))
    quit = font.render("Quit", True, (0, 0, 0))
    xfont = font.render("X", True, (0, 0, 0))
    screen.blit(start, (50, 50))
    screen.blit(options, (50, 100))
    screen.blit(replay, (50, 150))
    screen.blit(quit, (50, 200))
    pygame.display.flip()
    running = True
    havereplay = False
    replayParams = []

    while running:
        if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + start.get_rect().width and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 50 + start.get_rect().height:
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + start.get_rect().height + 2),
                             (50 + start.get_rect().width, 50 + start.get_rect().height + 2), 3)
        elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + options.get_rect().width and pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 100 + options.get_rect().height:
            pygame.draw.line(screen, (0, 0, 0), (50, 100 + options.get_rect().height + 2),
                             (50 + options.get_rect().width, 100 + options.get_rect().height + 2), 3)
        elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + replay.get_rect().width and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 150 + replay.get_rect().height:
            pygame.draw.line(screen, (0, 0, 0), (50, 150 + replay.get_rect().height + 2),
                             (50 + replay.get_rect().width, 150 + replay.get_rect().height + 2), 3)
        elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + quit.get_rect().width and pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 200 + quit.get_rect().height:
            pygame.draw.line(screen, (0, 0, 0), (50, 200 + quit.get_rect().height + 2),
                             (50 + quit.get_rect().width, 200 + quit.get_rect().height + 2), 3)
        else:
            screen.blit(bgimg, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RETURN:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + start.get_rect().width and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 50 + start.get_rect().height:
                    return 1, variables.options
                elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + options.get_rect().width and pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 100 + options.get_rect().height:
                    counter = 0
                    surf = pygame.image.save(screen, "resources/screenshot.png")
                    img = Image.open("resources/screenshot.png")
                    surfBlurred = img.filter(ImageFilter.GaussianBlur(radius=6))
                    surfBlurred.save("resources/screenshot.png")
                    screen.blit(pygame.image.load("resources/screenshot.png"), (0, 0))
                    while True:
                        if counter >= 400:
                            break
                        counter += 1
                        pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() - counter * 2, 0, 400, 720))
                        pygame.display.flip()
                    optionsmenu(screen, xfont)
                elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + replay.get_rect().width and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 150 + replay.get_rect().height:
                    counter = 0
                    surf = pygame.image.save(screen, "resources/screenshot.png")
                    img = Image.open("resources/screenshot.png")
                    surfBlurred = img.filter(ImageFilter.GaussianBlur(radius=6))
                    surfBlurred.save("resources/screenshot.png")
                    screen.blit(pygame.image.load("resources/screenshot.png"), (0, 0))
                    while True:
                        if counter >= 200:
                            break
                        counter += 1
                        pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()-counter*2, 0, 400, 720))
                        pygame.display.flip()
                    replaySelector(screen, xfont, config_path, variables.options)





                elif pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 50 + quit.get_rect().width and pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 200 + quit.get_rect().height:
                    pygame.quit()




        screen.blit(start, (50, 50))
        screen.blit(options, (50, 100))
        screen.blit(replay, (50, 150))
        screen.blit(quit, (50, 200))
        pygame.display.flip()


    pygame.quit()
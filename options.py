import pygame
import variables


def options(screen, xfont):
    pygame.init()
    font = pygame.font.Font("resources/font.ttf", 15)
    noOfLoops = variables.options[0]
    noOfGenerations = variables.options[1]
    screenResolution = variables.options[2]

    check = True
    while check:
        time = font.render("Training and replaying length: ", True, (0, 0, 0))
        resolution = font.render("Screen resolution: ", True, (0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() - 400 * 2, 0, 800, 720))

        minus = font.render("-", True, (0, 0, 0))
        plus = font.render("+", True, (0, 0, 0))
        numberofloops = font.render(str(noOfLoops), True, (0, 0, 0))
        numberofgenerations = font.render(str(noOfGenerations), True, (0, 0, 0))
        training = font.render("Training No. of generations: ", True, (0, 0, 0))
        screenresolution = font.render(str(screenResolution[0]) + "x" + str(screenResolution[1]), True, (0, 0, 0))
        screen.blit(time, (screen.get_width() - 400 * 2 + 50, 50))
        screen.blit(training, (screen.get_width() - 400 * 2 + 50, 100))
        screen.blit(resolution, (screen.get_width() - 400 * 2 + 50, 150))
        screen.blit(minus, (screen.get_width() - 400 * 2 + 50 + time.get_width() + 10, 50))
        screen.blit(numberofloops,
                    (screen.get_width() - 400 * 2 + 50 + time.get_width() + 10 + minus.get_width() + 10, 50))
        screen.blit(plus, (
            screen.get_width() - 400 * 2 + 50 + time.get_width() + 10 + minus.get_width() + 10 + minus.get_width() + 10 + numberofloops.get_width(),
            50))
        screen.blit(minus, (screen.get_width() - 400 * 2 + 50 + training.get_width() + 10, 100))
        screen.blit(numberofgenerations,
                    (screen.get_width() - 400 * 2 + 50 + training.get_width() + 10 + minus.get_width() + 10, 100))
        screen.blit(plus, (
            screen.get_width() - 400 * 2 + 50 + training.get_width() + 10 + minus.get_width() + 10 + minus.get_width() + 10 + numberofgenerations.get_width(),
            100))
        screen.blit(minus, (screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 10, 150))
        screen.blit(screenresolution,
                    (screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 10 + minus.get_width() + 10, 150))
        screen.blit(plus, (
            screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 10 + minus.get_width() + 10 + minus.get_width() + 10 + screenresolution.get_width(),
            150))
        pygame.draw.rect(screen, (0, 0, 0), (
            screen.get_width() - 400 * 2 + 50 + time.get_width() + 5, 45, minus.get_width() + 10,
            minus.get_height() + 10), 1)
        pygame.draw.rect(screen, (0, 0, 0), (
            screen.get_width() - 400 * 2 + 50 + time.get_width() + 10 + minus.get_width() + 10 + numberofloops.get_width() + 20,
            45, plus.get_width() + 10, plus.get_height() + 10), 1)
        pygame.draw.rect(screen, (0, 0, 0), (
            screen.get_width() - 400 * 2 + 50 + training.get_width() + 5, 95, minus.get_width() + 10,
            minus.get_height() + 10),
                         1)
        pygame.draw.rect(screen, (0, 0, 0), (
            screen.get_width() - 400 * 2 + 50 + training.get_width() + 10 + minus.get_width() + 10 + numberofgenerations.get_width() + 20,
            95, plus.get_width() + 10, plus.get_height() + 10), 1)
        pygame.draw.rect(screen, (0, 0, 0), (
            screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 5, 145, minus.get_width() + 10,
            minus.get_height() + 10), 1)
        pygame.draw.rect(screen, (0, 0, 0), (
            screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 10 + minus.get_width() + 10 + screenresolution.get_width() + 20,
            145, plus.get_width() + 10, plus.get_height() + 10), 1)
        screen.blit(xfont, (screen.get_width() - xfont.get_width(), 0))
        if pygame.mouse.get_pos()[0] > screen.get_width() - xfont.get_width() and pygame.mouse.get_pos()[1] < xfont.get_height():
            pygame.draw.line(screen, (0, 0, 0), (screen.get_width() - xfont.get_width(), xfont.get_height() + 2), (screen.get_width() - 3, xfont.get_height() + 2), 2)
            if pygame.mouse.get_pressed()[0]:
                counter = 400
                while counter > 0:
                    screen.blit(pygame.image.load("resources/screenshot.png"), (0, 0))
                    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() - counter * 2, 0, 800, 720))
                    pygame.display.flip()
                    counter -= 7
                check = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    counter = 400
                    while counter > 0:
                        screen.blit(pygame.image.load("resources/screenshot.png"), (0, 0))
                        pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() - counter * 2, 0, 800, 720))
                        pygame.display.flip()
                        counter -= 7
                    variables.options = [noOfLoops, noOfGenerations, screenResolution]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (
                        pygame.mouse.get_pos()[0] > screen.get_width() - 400 * 2 + 50 + time.get_width() + 5) and pygame.mouse.get_pos()[0] < (
                        screen.get_width() - 400 * 2 + 50 + time.get_width() + 10 + minus.get_width() + 10) and 45 < \
                        pygame.mouse.get_pos()[1] < (
                        45 + minus.get_height() + 10):
                    if noOfLoops > 500:
                        noOfLoops -= 500
                        variables.options = [noOfLoops, noOfGenerations, screenResolution]
                if (
                        pygame.mouse.get_pos()[0] > screen.get_width() - 400 * 2 + 50 + time.get_width() + 10 + minus.get_width() + 10 + numberofloops.get_width() + 20) and pygame.mouse.get_pos()[0] < (
                        screen.get_width() - 400 * 2 + 50 + time.get_width() + 10 + minus.get_width() + 10 + numberofloops.get_width() + 20 + plus.get_width() + 10) and 45 < \
                        pygame.mouse.get_pos()[1] < (
                        45 + plus.get_height() + 10):
                    if noOfLoops < 20000:
                        noOfLoops += 500
                        variables.options = [noOfLoops, noOfGenerations, screenResolution]
                if (
                        pygame.mouse.get_pos()[0] > screen.get_width() - 400 * 2 + 50 + training.get_width() + 5) and pygame.mouse.get_pos()[0] < (
                        screen.get_width() - 400 * 2 + 50 + training.get_width() + 10 + minus.get_width() + 10) and 95 < \
                        pygame.mouse.get_pos()[1] < (
                        95 + minus.get_height() + 10):
                    if noOfGenerations > 10:
                        noOfGenerations -= 10
                        variables.options = [noOfLoops, noOfGenerations, screenResolution]
                if (
                        pygame.mouse.get_pos()[0] > screen.get_width() - 400 * 2 + 50 + training.get_width() + 10 + minus.get_width() + 10 + numberofgenerations.get_width() + 20) and pygame.mouse.get_pos()[0] < (
                        screen.get_width() - 400 * 2 + 50 + training.get_width() + 10 + minus.get_width() + 10 + numberofgenerations.get_width() + 20 + plus.get_width() + 10) and 95 < \
                        pygame.mouse.get_pos()[1] < (
                        95 + plus.get_height() + 10):
                    if noOfGenerations < 300:
                        noOfGenerations += 10
                        variables.options = [noOfLoops, noOfGenerations, screenResolution]
                if (
                        pygame.mouse.get_pos()[0] > screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 5) and pygame.mouse.get_pos()[0] < (
                        screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 10 + minus.get_width() + 10) and 145 < \
                        pygame.mouse.get_pos()[1] < (
                        145 + minus.get_height() + 10):
                    if screenResolution != (960, 540):
                        screenResolution = (960, 540)
                        variables.options = [noOfLoops, noOfGenerations, screenResolution]
                if (
                        pygame.mouse.get_pos()[0] > screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 10 + minus.get_width() + 10 + screenresolution.get_width() + 20) and pygame.mouse.get_pos()[0] < (
                        screen.get_width() - 400 * 2 + 50 + resolution.get_width() + 10 + minus.get_width() + 10 + screenresolution.get_width() + 20 + plus.get_width() + 10) and 145 < \
                        pygame.mouse.get_pos()[1] < (
                        145 + plus.get_height() + 10):
                    if screenResolution != (1920, 1080):
                        screenResolution = (1920, 1080)
                        variables.options = [noOfLoops, noOfGenerations, screenResolution]

        pygame.display.flip()

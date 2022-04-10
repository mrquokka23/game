import pygame
import os
from replay_genome import replay_genome

def replaySelector(screen, xfont, config_path, optionsReturned):
    font = pygame.font.Font("resources/font.ttf", 15)
    check = True
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    counter = 200
                    while counter > 0:
                        screen.blit(pygame.image.load("resources/screenshot.png"), (0, 0))
                        pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()-counter*2, 0, 400, 720))
                        pygame.display.flip()
                        counter -= 3
                    check = False
        folder = "nets/"
        files = os.listdir(folder)
        listFiles = []
        for file in files:
            if file.endswith(".pkl"):
                if not file in listFiles:
                    listFiles.append(font.render(file, True, (0, 0, 0)))
        pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() - 200 * 2, 0, 400, 720))

        for x,file in enumerate(listFiles):
            screen.blit(file, (screen.get_width() - 350, x*50 + 50))

            if pygame.mouse.get_pos()[0] > screen.get_width() - 350 and pygame.mouse.get_pos()[0] < screen.get_width() - 350 + file.get_rect().width and pygame.mouse.get_pos()[1] > x*50 + 50 and pygame.mouse.get_pos()[1] < x*50 + 50 + file.get_rect().height:
                pygame.draw.line(screen, (0, 0, 0), (screen.get_width() - 350, x*50 + 50 + file.get_rect().height + 2), (screen.get_width() - 350 + file.get_rect().width, x*50 + 50 + file.get_rect().height + 2), 2)
                if pygame.mouse.get_pressed()[0]:
                    return replay_genome(config_path, folder + files[x], optionsReturned)



        screen.blit(xfont, (screen.get_width() - xfont.get_width(), 0))
        if pygame.mouse.get_pos()[0] > screen.get_width() - xfont.get_width() and pygame.mouse.get_pos()[0] < screen.get_width() and pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < xfont.get_height():
            pygame.draw.line(screen, (0, 0, 0), (screen.get_width() - xfont.get_width(), xfont.get_height() + 2), (screen.get_width() - 4, xfont.get_height() + 2), 2)
            if pygame.mouse.get_pressed()[0]:
                counter = 200
                while counter > 0:
                    screen.blit(pygame.image.load("resources/screenshot.png"), (0, 0))
                    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()-counter*2, 0, 400, 720))
                    pygame.display.flip()
                    counter -= 3
                check = False

        pygame.display.flip()



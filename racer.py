import pygame
import math
import numpy

class Car(pygame.sprite.Sprite):
    def __init__(self, img, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.position = (xpos, ypos)
        self.image = img
        self.rotImage = self.image
        self.rect = self.image.get_rect()
        self.velocity = 0  # pixels per loop
        self.lastVelocity = 0  # pixels per loop
        self.acceleration = 0.01  # pixels per loop suared
        self.deceleration = 0.005
        self.brakingforce = 0.02  # pixels per loop suared(negative acceleration)
        self.steeringSpeed = 0.002  # pixels per loop
        self.maxSpeed = 2  # pixels per loop
        self.steeringAngle = 0  # percent (positive is left and negative is right)
        self.maxTurningDegrees = 45  # degrees
        self.angle = 0  # degrees (0 degrees = nose pointing east)
        self.accelerationTstamp = 0
        self.decelerationTstamp = 0
        self.brakingTstamp = 0
        self.steeringTstampR = 0
        self.steeringTstampL = 0
        self.steerbackTstamp = 0
        self.startVelocity = 0

        self.carLocation = pygame.math.Vector2(xpos, ypos)
        self.carHeading = 0
        self.carSpeed = 0
        self.steerAngle = 0
        self.wheelBase = self.rect.width * 0.6
        self.frontWheel = pygame.math.Vector2(
            self.carLocation + self.wheelBase / 2 * pygame.math.Vector2(math.cos(self.carHeading),
                                                                        math.sin(self.carHeading)))
        self.backWheel = pygame.math.Vector2(
            self.carLocation - self.wheelBase / 2 * pygame.math.Vector2(math.cos(self.carHeading),
                                                                        math.sin(self.carHeading)))
        self.startSteerAngle = 0
        self.mask = pygame.mask.from_surface(self.rotImage)
        self.radars = [[(0, 0), 0, (-math.pi) / 2], [(0, 0), 0, (-math.pi) / 4], [(0, 0), 0, 0],
                       [(0, 0), 0, math.pi / 4], [(0, 0), 0, math.pi / 2]]

        self.distances = []
        for distance in self.radars:
            position, dist, angle = distance
            self.distances.append(dist)

        # self.forwardLine = pygame.draw.line(screen,(255,0,0),self.rect.center,(math.cos(math.radians(self.carHeading))*400,math.sin(math.radians(self.carHeading))*400),1)

    def checkRadars(self, radars, bgimg):
        i = 0
        for radar in radars:
            pos, dist, angle = radar
            len = 0
            x = int(self.rect.center[0] + math.cos(2 * math.pi + (self.carHeading + angle)) * len)
            y = int(self.rect.center[1] + math.sin(2 * math.pi + (self.carHeading + angle)) * len)
            while not bgimg.get_at((x, y)) == (255, 255, 255) and len < 400:
                len += 1
                x = int(self.rect.center[0] + math.cos(2 * math.pi + (self.carHeading + angle)) * len)
                y = int(self.rect.center[1] + math.sin(2 * math.pi + (self.carHeading + angle)) * len)

            dist = math.sqrt(math.pow(x - self.rect.center[0], 2) + math.pow(y - self.rect.center[1], 2))
            self.radars[i] = ([(x, y), dist, angle])
            i += 1

    def draw(self, screen):
        screen.blit(self.rotImage, self.rect)
        for radar in self.radars:
            pos, dist, angle = radar
            pygame.draw.line(screen, (255, 0, 0), self.rect.center, pos, 1)

    def update(self, deltaT, screen, bgimg):

        pygame.sprite.Sprite.update(self)

        self.frontWheel = pygame.math.Vector2(
            self.carLocation + self.wheelBase / 2 * pygame.math.Vector2(math.cos(self.carHeading),
                                                                        math.sin(self.carHeading)))
        self.backWheel = pygame.math.Vector2(
            self.carLocation - self.wheelBase / 2 * pygame.math.Vector2(math.cos(self.carHeading),
                                                                        math.sin(self.carHeading)))

        # self.position = (self.position[0], self.position[1])
        if pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s]:
            if self.accelerationTstamp == 0:
                self.accelerationTstamp = deltaT
                self.decelerationTstamp = 0
                self.startVelocity = self.velocity
            self.lastVelocity = self.velocity
            if self.lastVelocity < 0:
                self.velocity = self.startVelocity + (self.brakingforce * (deltaT - self.accelerationTstamp))
            else:
                self.velocity = self.startVelocity + (self.acceleration * (deltaT - self.accelerationTstamp))
        if self.accelerationTstamp != 0 and not pygame.key.get_pressed()[pygame.K_w]:
            self.accelerationTstamp = 0

        if pygame.key.get_pressed()[pygame.K_s] and not pygame.key.get_pressed()[pygame.K_w]:
            if self.brakingTstamp == 0:
                self.brakingTstamp = deltaT
                self.decelerationTstamp = 0
                self.startVelocity = self.velocity
            self.lastVelocity = self.velocity
            if self.lastVelocity > 0:
                self.velocity = self.startVelocity + (-self.brakingforce * (deltaT - self.brakingTstamp))
            else:
                self.velocity = self.startVelocity + (-self.acceleration * (deltaT - self.brakingTstamp))
        if self.brakingTstamp != 0 and not pygame.key.get_pressed()[pygame.K_s]:
            self.brakingTstamp = 0

        # if pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]:
        # self.steeringAngle =

        if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s]:
            if self.decelerationTstamp == 0 and self.velocity != 0:
                self.decelerationTstamp = deltaT
                self.startVelocity = self.velocity
            if self.lastVelocity > 0:
                if self.velocity + (-self.deceleration * (deltaT - self.decelerationTstamp)) <= 0:
                    self.velocity = 0
                    self.decelerationTstamp = 0
                else:
                    self.velocity = self.startVelocity + (-self.deceleration * (deltaT - self.decelerationTstamp))
            elif self.lastVelocity < 0:
                if self.velocity + (self.deceleration * (deltaT - self.decelerationTstamp)) >= 0:
                    self.velocity = 0
                    self.decelerationTstamp = 0
                else:
                    self.velocity = self.startVelocity + (self.deceleration * (deltaT - self.decelerationTstamp))
            self.lastVelocity = self.velocity
        if self.velocity == 0:
            self.decelerationTstamp = 0

        if not pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]:
            self.steerAngle = 0

        if pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]:
            if self.steeringTstampL == 0:
                self.steeringTstampL = deltaT
                self.startSteerAngle = self.steerAngle
            if self.startSteerAngle - (self.steeringSpeed * (deltaT - self.steeringTstampL)) < -0.785398:
                self.startSteerAngle = -0.785398
            else:
                self.steerAngle = self.startSteerAngle - (self.steeringSpeed * (deltaT - self.steeringTstampL))
        if self.steeringTstampL != 0 and not pygame.key.get_pressed()[pygame.K_a]:
            self.steeringTstampL = 0

        if pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]:
            if self.steeringTstampR == 0:
                self.steeringTstampR = deltaT
                self.startSteerAngle = self.steerAngle
            if self.startSteerAngle + (self.steeringSpeed * (deltaT - self.steeringTstampR)) > 0.785398:
                self.steerAngle = 0.785398
            else:
                self.steerAngle = self.startSteerAngle + (self.steeringSpeed * (deltaT - self.steeringTstampR))
        if self.steeringTstampR != 0 and not pygame.key.get_pressed()[pygame.K_d]:
            self.steeringTstampR = 0

        if (not pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]) or (
                pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_d]):
            if self.steerbackTstamp == 0:
                self.steerbackTstamp = deltaT
                self.startSteerAngle = self.steerAngle

            if self.startSteerAngle > 0:
                if self.startSteerAngle - (self.steeringSpeed * (deltaT - self.steerbackTstamp)) < 0:
                    self.steeringAngle = 0
                    self.steerbackTstamp = 0
                else:
                    self.steerAngle = self.startSteerAngle - (self.steeringSpeed * (deltaT - self.steerbackTstamp))
            elif self.steeringAngle < 0:
                if self.startSteerAngle + (self.steeringSpeed * (deltaT - self.steerbackTstamp)) < 0:
                    self.steeringAngle = 0
                    self.steerbackTstamp = 0
                else:
                    self.steerAngle = self.startSteerAngle + (self.steeringSpeed * (deltaT - self.steerbackTstamp))
            if (self.steerAngle == 0) or (
                    pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]) or (
                    pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a]):
                self.steerbackTstamp = 0

        if self.velocity > self.maxSpeed:
            self.velocity = self.maxSpeed
        elif self.velocity < -self.maxSpeed:
            self.velocity = -self.maxSpeed

        self.carSpeed = self.velocity

        self.backWheel += self.carSpeed * pygame.math.Vector2(math.cos(self.carHeading), math.sin(self.carHeading))
        self.frontWheel += self.carSpeed * pygame.math.Vector2(math.cos(self.carHeading + self.steerAngle),
                                                               math.sin(self.carHeading + self.steerAngle))
        self.carLocation = (self.frontWheel + self.backWheel) / 2
        self.carHeading = math.atan2(self.frontWheel.y - self.backWheel.y, self.frontWheel.x - self.backWheel.x)

        self.angle = numpy.interp(self.carHeading, [-numpy.pi, numpy.pi], [180, -180])

        self.position = self.carLocation
        # self.position = (self.position[0] + self.velocity, self.position[1])
        self.rotImage = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotImage.get_rect()
        self.rect.center = self.position
        self.mask = pygame.mask.from_surface(self.rotImage)
        self.checkRadars(self.radars, bgimg)
        self.distances = []
        for distance in self.radars:
            position, dist, angle = distance
            self.distances.append(dist)
        self.draw(screen)
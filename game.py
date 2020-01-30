import math
import random
import time

import pygame

RESOLUTION = (800, 600)  # разрешение окна и игрового поля

screen = pygame.display.set_mode(RESOLUTION)
running = 1  # означает что игра запущена

timestamp = time.time()  # используется для подсчета времени
DT = 0  # время между циклами обработки
bot = False  # управляет активацией бота


class Acteroid:
    pos = [0, 0]  # позиция астеройда
    speed = [0, 0]  # скорость астеройда
    head = 180  # его направление
    rotation = 0  # скорость вращения
    radius = 5  # радиус
    decay = 5  # стадия распада
    dt = 0.016  # стандартная шкала времени
    created = 0  # время когд был создан

    def __init__(self, speed):  # задаем значение переменных
        self.pos = [random.randrange(0, RESOLUTION[0]), random.randrange(0, RESOLUTION[1])]
        self.head = random.randrange(-180, 180)
        self.rotation = random.randrange(-300, 300) * 0.1
        self.speed = speed
        self.created = time.time()

    def draw(self, surface, offset):  # функция отрисовки
        color = (200, 200, 250)  # цвет фона астеройда
        pos = (int(self.pos[0] + offset[0]), int(self.pos[1] + offset[1]))
        pygame.draw.circle(surface, color, pos, self.radius * self.decay, 0)  # отрисовка астеройда
        dent_pos = [0, 0]
        color = (55, 50, 55)
        dent_pos[0] = int(pos[0] + (4 * self.decay) * math.sin(math.radians(self.head - 120)))
        dent_pos[1] = int(pos[1] + (4 * self.decay) * math.cos(math.radians(self.head - 120)))
        pygame.draw.circle(surface, color, dent_pos, int(0.8 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (2.8 * self.decay) * math.sin(math.radians(self.head - 45)))
        dent_pos[1] = int(pos[1] + (2.8 * self.decay) * math.cos(math.radians(self.head - 45)))
        pygame.draw.circle(surface, color, dent_pos, int(0.8 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (3.9 * self.decay) * math.sin(math.radians(self.head - 30)))
        dent_pos[1] = int(pos[1] + (3.9 * self.decay) * math.cos(math.radians(self.head - 30)))
        pygame.draw.circle(surface, color, dent_pos, int(0.8 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (1.7 * self.decay) * math.sin(math.radians(self.head - 30)))
        dent_pos[1] = int(pos[1] + (1.7 * self.decay) * math.cos(math.radians(self.head - 30)))
        pygame.draw.circle(surface, color, dent_pos, int(0.8 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (2.8 * self.decay) * math.sin(math.radians(self.head + 15)))
        dent_pos[1] = int(pos[1] + (2.8 * self.decay) * math.cos(math.radians(self.head + 15)))
        pygame.draw.circle(surface, color, dent_pos, int(1 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (3.7 * self.decay) * math.sin(math.radians(self.head + 45)))
        dent_pos[1] = int(pos[1] + (3.7 * self.decay) * math.cos(math.radians(self.head + 45)))
        pygame.draw.circle(surface, color, dent_pos, int(0.5 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (2.5 * self.decay) * math.sin(math.radians(self.head + 100)))
        dent_pos[1] = int(pos[1] + (2.5 * self.decay) * math.cos(math.radians(self.head + 100)))
        pygame.draw.circle(surface, color, dent_pos, int(2 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (3.9 * self.decay) * math.sin(math.radians(self.head + 150)))
        dent_pos[1] = int(pos[1] + (3.9 * self.decay) * math.cos(math.radians(self.head + 150)))
        pygame.draw.circle(surface, color, dent_pos, int(0.8 * self.decay), 0)

        dent_pos[0] = int(pos[0] + (3 * self.decay) * math.sin(math.radians(self.head + 180)))
        dent_pos[1] = int(pos[1] + (3 * self.decay) * math.cos(math.radians(self.head + 180)))
        pygame.draw.circle(surface, color, dent_pos, int(0.8 * self.decay), 0)

    def calculate(self):  # расчет положения и позиции
        self.head += self.rotation * self.dt
        self.pos[0] = self.pos[0] % RESOLUTION[0]
        self.pos[1] = self.pos[1] % RESOLUTION[1]
        self.pos = [self.pos[0] + self.speed[0] * self.dt, self.pos[1] + self.speed[1] * self.dt]

    def get_future_pos(self, projectile_speed, distance):  # узнать позицию через время
        time_of_flight = distance / projectile_speed
        pos = [self.pos[0] + self.speed[0] * time_of_flight, self.pos[1] + self.speed[1] * time_of_flight]
        return pos


class Projectile:  # класс лазера которым стреляет корабль
    pos = [0, 0]
    head = 180
    scale = 7  # длина лазерного луча
    speed = [0, 0]
    relative_speed = 0  # скорость относительно корабля
    created = 0
    halflife = 0  # время "жизни" луча
    dt = 0.016

    def __init__(self, pos, head, speed):  # задаем значения переменным
        self.pos = pos
        self.speed = speed
        self.head = head + random.randrange(-2, 2)
        self.created = time.time()
        self.halflife = self.created + 5 + random.randrange(-1, 1)
        self.relative_speed = 250 + random.randrange(-10, 10)
        self.speed[0] = self.speed[0] + self.relative_speed * math.sin(math.radians(self.head))
        self.speed[1] = self.speed[1] + self.relative_speed * math.cos(math.radians(self.head))

    def draw(self, surface, offset):  # отрисовка луча
        color = (50, 250, 50)
        spos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
        pos = (self.pos[0] + offset[0] + self.scale * math.sin(math.radians(self.head)),
               self.pos[1] + offset[1] + self.scale * math.cos(math.radians(self.head)))
        pygame.draw.line(surface, color, spos, pos, 3)

    def calculate(self):  # расчет положения в пространстве
        self.pos[0] = self.pos[0] % RESOLUTION[0]
        self.pos[1] = self.pos[1] % RESOLUTION[1]
        dv = self.speed[0] * self.dt
        dh = self.speed[1] * self.dt
        self.pos[0] += dv
        self.pos[1] += dh


class Player:  # класс игрока/корабля
    pos = [RESOLUTION[0] / 2, RESOLUTION[1] / 2]
    head = 180
    scale = 10
    speed = [0, 0]
    max_speed = scale * 1000  # максимальная скорость
    # установлено значение в ~7000 пикселей в секунду, по факту скорость не превышает 300 пикселей в секунду
    acceleration = scale * 30  # ускорение корабля
    propelling = True  # корабль ускоряется
    dt = 0.016
    speed_decay = scale / 10  # коэффициент трения
    last_shot = 0  # когда был произведен последний выстрел

    projectiles = []  # храним тут все лазерные лучи
    asteroids = []  # храним тут все астеройды

    score = 0  # счет игрока

    def __init__(self):
        self.last_shot = time.time()  # устанавливаем значения
        pass

    def draw(self, surface, offset):  # отрисовка корабля
        color = (255, 255, 255)

        front = (self.pos[0] + offset[0] + self.scale * math.sin(math.radians(self.head)),
                 self.pos[1] + offset[1] + self.scale * math.cos(math.radians(self.head)))

        left = (self.pos[0] + offset[0] + self.scale * math.sin(math.radians(self.head - 135)),
                self.pos[1] + offset[1] + self.scale * math.cos(math.radians(self.head - 135)))

        right = (self.pos[0] + offset[0] + self.scale * math.sin(math.radians(self.head + 135)),
                 self.pos[1] + offset[1] + self.scale * math.cos(math.radians(self.head + 135)))

        back = (self.pos[0] + offset[0] + self.scale / 3 * math.sin(math.radians(self.head + 180)),
                self.pos[1] + offset[1] + self.scale / 3 * math.cos(math.radians(self.head + 180)))

        pygame.draw.polygon(surface, color, (left, front, right, back))

        if self.propelling:  # если корабль ускоряется, рисуем огонь
            color = (255, 100, 100)
            left = (self.pos[0] + offset[0] + self.scale / 1.6 * math.sin(math.radians(self.head - 150)),
                    self.pos[1] + offset[1] + self.scale / 1.6 * math.cos(math.radians(self.head - 150)))

            right = (self.pos[0] + offset[0] + self.scale / 1.6 * math.sin(math.radians(self.head + 150)),
                     self.pos[1] + offset[1] + self.scale / 1.6 * math.cos(math.radians(self.head + 150)))

            wobble = random.randrange(-int(self.scale / 8), int(self.scale / 8))  # чтобы выглядел как настоящий
            ang_wobble = random.randrange(-8, 8)

            front = (self.pos[0] + offset[0] + (self.scale * 1.2 + wobble) * math.sin(
                math.radians(self.head + 180 + ang_wobble)),
                     self.pos[1] + offset[1] + (self.scale * 1.2 + wobble) * math.cos(
                         math.radians(self.head + 180 + ang_wobble)))
            pygame.draw.polygon(surface, color, (left, front, right, back))

    def hypotenuse(self, pos1, pos2):  # функция нахождения гипотенузы, используется для обработки столкновений
        delta_pos = (pos2[0] - pos1[0], pos2[1] - pos1[1])
        hypotenuse = (delta_pos[0] ** 2 + delta_pos[1] ** 2) ** 0.5
        return hypotenuse

    def calculate(self):  # расчет положения и не только

        self.pos[0] = self.pos[0] % RESOLUTION[0]
        self.pos[1] = self.pos[1] % RESOLUTION[1]

        scalar_speed = math.sqrt(self.speed[0] ** 2 + self.speed[1] ** 2)
        if scalar_speed < self.max_speed and self.propelling:  # обработка ускорений
            ds = self.acceleration * self.dt
            self.speed[0] += ds * math.sin(math.radians(self.head))
            self.speed[1] += ds * math.cos(math.radians(self.head))

        dv = self.speed[0] * self.dt
        dh = self.speed[1] * self.dt
        self.pos[0] += dv
        self.pos[1] += dh
        ds = self.speed_decay * self.dt
        self.speed[0] -= self.speed[0] * ds
        self.speed[1] -= self.speed[1] * ds

        for i in range(len(self.projectiles)):  # удаляем лучи которые "умерли"
            if self.projectiles[i].halflife < time.time():
                self.projectiles.pop(i)
                break

        pattern = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        # используется для "бесконечной отрисовки"

        popped = False  # если удален лазер или астеройд нам нужно пропустить цикл, иначе ошибка

        for i in range(len(self.asteroids)):
            for j in range(len(self.projectiles)):
                r1 = self.asteroids[i].radius * self.asteroids[i].decay  # находим радиусы обьектов
                r2 = self.projectiles[j].scale
                for multiplier in pattern:
                    proj_pos = (self.projectiles[j].pos[0] + (RESOLUTION[0] * multiplier[0]),
                                self.projectiles[j].pos[1] + (RESOLUTION[1] * multiplier[1]))
                    hyp = self.hypotenuse(self.asteroids[i].pos, proj_pos)  # расстояние между обьектами
                    if hyp < r1 + r2:
                        if self.asteroids[i].decay > 3:  # раскалываем астеройд если можно
                            astra = Acteroid((random.randrange(-100, 100), random.randrange(-100, 100)))
                            astra.decay = self.asteroids[i].decay - 1
                            astra.pos = self.asteroids[i].pos
                            astra1 = Acteroid((random.randrange(-100, 100), random.randrange(-100, 100)))
                            astra1.decay = self.asteroids[i].decay - 1
                            astra1.pos = self.asteroids[i].pos
                            self.asteroids.append(astra)
                            self.asteroids.append(astra1)

                        self.asteroids.pop(i)  # удаляем старый астеройд и лазер
                        self.projectiles.pop(j)
                        self.score += 1

                        popped = True
                    if popped:
                        break
                if popped:
                    break
            if popped:
                break

        for i in range(len(self.asteroids)):  # проверяем столкновения астеройдов с кораблем
            r1 = self.asteroids[i].radius * self.asteroids[i].decay
            r2 = self.scale
            for multiplier in pattern:
                player_pos = (self.pos[0] + (RESOLUTION[0] * multiplier[0]),
                              self.pos[1] + (RESOLUTION[1] * multiplier[1]))
                hyp = self.hypotenuse(self.asteroids[i].pos, player_pos)
                if hyp < r1 + r2:
                    if time.time() - self.asteroids[i].created < 1:
                        # фикс бага с астеройдом который появляется и сразу убивает игрока
                        self.asteroids.pop(i)
                        self.asteroids.append(Acteroid((random.randrange(-100, 100), random.randrange(-100, 100))))
                    else:
                        player.pos = [random.randrange(0, RESOLUTION[0]), random.randrange(0, RESOLUTION[1])]
                        player.score = 0
                        popped = True

                if popped:
                    break
            if popped:
                break

    def infinite_draw(self, surface):  # бесконечная отрисовка

        pattern = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        def super_draw(surface, object, pattern):  # time упрощение отрисовки + обработка всех обьектов
            object.calculate()

            for multiplier in pattern:
                object.dt = DT
                object.draw(surface, (RESOLUTION[0] * multiplier[0], RESOLUTION[1] * multiplier[1]))

        for asteroid in self.asteroids:  # отрисовка астеройдов
            super_draw(surface, asteroid, pattern)

        for projectile in self.projectiles:  # отрисовка лазеров
            super_draw(surface, projectile, pattern)

        super_draw(surface, self, pattern)  # отрисовка кораблей (их 9)

    def pew(self):  # выстрел лазером
        if (time.time() - self.last_shot > 0.15):
            self.last_shot = time.time()
            projectile = Projectile([float(self.pos[0]), float(self.pos[1])],
                                    float(self.head),
                                    [float(self.speed[0]), float(self.speed[1])])
            self.projectiles.append(projectile)

    def auto(self):  # функция отвечающая за работу бота
        shortest = RESOLUTION[0] * RESOLUTION[1]
        closest_pos = [0, 0]
        for asteroid in self.asteroids:
            hyp = self.hypotenuse(self.pos, asteroid.pos)
            hyp = self.hypotenuse(self.pos, asteroid.get_future_pos(250, hyp))  # реализация стрельбы на опережение
            if hyp < shortest:  # находит ближайший астеройд и стреляет в него
                closest_pos = asteroid.get_future_pos(250, hyp)
                shortest = hyp
        delta_pos = (closest_pos[0] - self.pos[0], closest_pos[1] - self.pos[1])
        angle = math.atan2(delta_pos[0], delta_pos[1]) / math.pi * 180
        if angle < 0:
            angle += 360

        if abs(self.head - angle) > 180:  # помогает избегать некоторые развороты на угол более 180 градусов
            angle = angle - 360

        if self.head < angle:
            self.head += 240 * DT  # поворачивает прям как игрок
        else:
            self.head -= 240 * DT

        if abs(self.head - angle) < 7: # не стреляет пока не будет наведен на цель
            self.pew()  # стреляет
            speed_limit = 40
        else:
            speed_limit = 100

        scalar_speed = math.sqrt(self.speed[0] ** 2 + self.speed[1] ** 2)
        if scalar_speed < speed_limit:  # поддерживает свою скорость низкой
            self.propelling = True
        else:
            self.propelling = False


class HUD:  # класс таблицы со счетом
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Bauhaus 93', 24)  # определяем шрифт

    high_score = 0
    score = 0

    def draw_and_update(self, surface, score):  # рисуем на экране и обновляем значения
        if score < self.score and self.score > self.high_score:
            self.high_score = self.score
        self.score = score
        score_string = "Score: " + str(self.score)
        score_surface = self.font.render(score_string, True, (255, 255, 255))

        high_score_string = "High score: " + str(self.high_score)
        high_score_surface = self.font.render(high_score_string, True, (255, 255, 255))

        surface.blit(high_score_surface, (20, 20))
        surface.blit(score_surface, (20, RESOLUTION[1] - 44))


player = Player()

hud = HUD()
while running:

    DT = time.time() - timestamp  # time узнаем время между отрисовками
    timestamp = time.time()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:  # ускорение корабля
        player.propelling = True
    else:
        player.propelling = False

    if keys[pygame.K_LEFT]:  # поворот корабля
        player.head += 240 * DT
    if keys[pygame.K_RIGHT]:
        player.head -= 240 * DT

    if keys[pygame.K_SPACE]:  # стрельба лазером
        player.pew()

    if event.type == pygame.KEYDOWN:  # включение бота
        if event.key == pygame.K_a:
            bot = not bot

    if bot:
        player.auto()

    screen.fill((0, 0, 0))
    player.infinite_draw(screen)
    if len(player.asteroids) < 5:
        player.asteroids.append(Acteroid((random.randrange(-100, 100), random.randrange(-100, 100))))

    hud.draw_and_update(screen, player.score)

    pygame.display.flip()  # обновление экрана

from time import sleep

import pygame

circle_positions = []
lines_positions = []
l_tree_pool = ["6"]
n_tree_pool = ["11"]
m_tree_pool = ["9", "8"]
r_tree_pool = ["14", "16"]


def init():
    pygame.init()
    display = (1500, 1100)
    screen = pygame.display.set_mode(display)

    return screen


def draw_lines(screen: pygame.Surface):
    for line in lines_positions:
        pygame.draw.line(screen, (255, 255, 255), (line[0], line[1]), (line[2], line[3]))

    return


def draw_circle_positions(screen: pygame.Surface):
    for pos in circle_positions:
        if pos[0] in l_tree_pool:
            draw_circle_with_text(pos[0], int(pos[1]), int(pos[2]), screen, (0, 0, 255))
            continue
        if pos[0] in m_tree_pool:
            draw_circle_with_text(pos[0], int(pos[1]), int(pos[2]), screen, (255, 0, 0))
            continue
        if pos[0] in r_tree_pool:
            draw_circle_with_text(pos[0], int(pos[1]), int(pos[2]), screen, (0, 255, 0))
            continue
        if pos[0] in n_tree_pool:
            draw_circle_with_text(pos[0], int(pos[1]), int(pos[2]), screen, (255, 255, 0))
            continue
        draw_circle_with_text(pos[0], int(pos[1]), int(pos[2]), screen)

    return


def draw_circle_with_text(textInCircle: str, x: int, y: int, screen: pygame.Surface, color=None):
    if color is None:
        color = (255, 255, 255)
    font = pygame.font.Font(None, 36)

    pygame.draw.circle(screen, color, (x, y), 50, 1)

    text = font.render(textInCircle, True, (255, 255, 255))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

    return


def draw_first(screen: pygame.Surface, clock: pygame.time.Clock):
    running = True
    circle_pos_1 = ["7", 200, 100]
    speed_x_1 = 3

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)

        draw_lines(screen)

        circle_pos_1[1] += speed_x_1

        if circle_pos_1[1] > 750:
            circle_positions.append(circle_pos_1)
            return

        draw_circle_with_text(circle_pos_1[0], int(circle_pos_1[1]), int(circle_pos_1[2]), screen)

        pygame.display.flip()
        clock.tick(60)


def draw_second(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["12", 200, 100]
    speed_x_1 = 3
    speed_y_1 = 2
    running = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 500:
            speed_y_1 = 0
        if circle_pos[1] > 900:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[0][1]) + 35, int(circle_positions[0][2]) + 35),
                             (int(circle_pos[1]) - 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[0][1]) + 35, int(circle_positions[0][2]) + 35,
                                    int(circle_pos[1]) - 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen)

        pygame.display.flip()
        clock.tick(60)


def draw_third(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["6", 200, 100]
    speed_x_1 = 3
    speed_y_1 = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 500:
            speed_y_1 = 0
        if circle_pos[1] > 600:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[0][1]) - 35, int(circle_positions[0][2]) + 35),
                             (int(circle_pos[1]) + 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[0][1]) - 35, int(circle_positions[0][2]) + 35,
                                    int(circle_pos[1]) + 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen, (0, 0, 255))

        pygame.display.flip()
        clock.tick(60)


def draw_fourth(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["14", 200, 100]
    speed_x_1 = 2
    speed_y_1 = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 600:
            speed_y_1 = 0

        if circle_pos[1] > 1050:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[1][1]) + 35, int(circle_positions[1][2]) + 35),
                             (int(circle_pos[1]) - 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[1][1]) + 35, int(circle_positions[1][2]) + 35,
                                    int(circle_pos[1]) - 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen, (0, 255, 0))

        pygame.display.flip()
        clock.tick(60)


def draw_fifth(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["16", 200, 100]
    speed_x_1 = 2
    speed_y_1 = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 800:
            speed_y_1 = 0

        if circle_pos[1] > 1200:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[3][1]) + 35, int(circle_positions[3][2]) + 35),
                             (int(circle_pos[1]) - 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[3][1]) + 35, int(circle_positions[3][2]) + 35,
                                    int(circle_pos[1]) - 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen, (0, 255, 0))

        pygame.display.flip()
        clock.tick(60)


def draw_sixth(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["10", 200, 100]
    speed_x_1 = 2
    speed_y_1 = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 600:
            speed_y_1 = 0

        if circle_pos[1] > 750:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[1][1]) - 35, int(circle_positions[1][2]) + 35),
                             (int(circle_pos[1]) + 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[1][1]) - 35, int(circle_positions[1][2]) + 35,
                                    int(circle_pos[1]) + 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen)

        pygame.display.flip()
        clock.tick(60)


def draw_seventh(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["11", 200, 100]
    speed_x_1 = 2
    speed_y_1 = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 800:
            speed_y_1 = 0

        if circle_pos[1] > 900:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[5][1]) + 35, int(circle_positions[5][2]) + 35),
                             (int(circle_pos[1]) - 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[5][1]) + 35, int(circle_positions[5][2]) + 35,
                                    int(circle_pos[1]) - 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen, (255, 255, 0))

        pygame.display.flip()
        clock.tick(60)


def draw_eighth(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["9", 200, 100]
    speed_x_1 = 2
    speed_y_1 = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 600:
            speed_x_1 = 0

        if circle_pos[2] > 700:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[5][1]) - 35, int(circle_positions[5][2]) + 35),
                             (int(circle_pos[1]) + 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[5][1]) - 35, int(circle_positions[5][2]) + 35,
                                    int(circle_pos[1]) + 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen, (255, 0, 0))

        pygame.display.flip()
        clock.tick(60)


def draw_ninth(screen: pygame.Surface, clock: pygame.time.Clock):
    circle_pos = ["8", 200, 100]
    speed_x_1 = 2
    speed_y_1 = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)
        circle_pos[1] += speed_x_1
        circle_pos[2] += speed_y_1

        if circle_pos[1] > 450:
            speed_x_1 = 0

        if circle_pos[2] > 900:
            circle_positions.append(circle_pos)
            pygame.draw.line(screen, (255, 255, 255),
                             (int(circle_positions[7][1]) - 35, int(circle_positions[7][2]) + 35),
                             (int(circle_pos[1]) + 35, int(circle_pos[2]) - 35), 1)
            lines_positions.append([int(circle_positions[7][1]) - 35, int(circle_positions[7][2]) + 35,
                                    int(circle_pos[1]) + 35, int(circle_pos[2]) - 35])
            return
        draw_circle_with_text(circle_pos[0], int(circle_pos[1]), int(circle_pos[2]), screen, (255, 0, 0))

        pygame.display.flip()
        clock.tick(60)


def wait(screen: pygame.Surface, clock: pygame.time.Clock):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)

        pygame.display.flip()
        clock.tick(60)
        sleep(10)
        return


def play_sound():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('SmallLeftRotate.wav')
    sound.play()
    return


def small_right_rotate(screen: pygame.Surface, clock: pygame.time.Clock):
    running = True
    speed = 3

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)

        circle_positions[1][2] += speed
        circle_positions[3][2] += speed
        circle_positions[4][2] += speed

        lines_positions[2][1] += speed
        lines_positions[2][3] += speed
        lines_positions[3][1] += speed
        lines_positions[3][3] += speed

        lines_positions[0][3] += speed
        lines_positions[4][1] += speed

        if circle_positions[1][2] > 500:
            speed = 0
            lines_positions[0][2] = circle_positions[5][1] - 35
            lines_positions[0][3] = circle_positions[5][2] - 35

            lines_positions[5][0] = circle_positions[1][1] - 35
            lines_positions[5][1] = circle_positions[1][2] + 35

            lines_positions[4][1] -= 70
            lines_positions[4][3] += 70
            while True:
                if circle_positions[6][1] < 750:
                    lines_positions[5][2] += 75
                    break
                screen.fill((0, 0, 0))

                draw_circle_positions(screen)
                draw_lines(screen)

                speed_x = 3
                circle_positions[6][1] -= speed_x
                lines_positions[5][2] -= speed_x

                pygame.display.flip()
                clock.tick(60)

            speed_x_1 = 2
            speed_y_1 = 3
            while True:

                screen.fill((0, 0, 0))

                draw_circle_positions(screen)
                draw_lines(screen)

                circle_positions[5][1] += speed_x_1
                circle_positions[7][1] += speed_x_1
                circle_positions[8][1] += speed_x_1
                circle_positions[5][2] -= speed_y_1
                circle_positions[7][2] -= speed_y_1
                circle_positions[8][2] -= speed_y_1

                lines_positions[6][0] += speed_x_1
                lines_positions[7][0] += speed_x_1
                lines_positions[6][1] -= speed_y_1
                lines_positions[7][1] -= speed_y_1
                lines_positions[6][2] += speed_x_1
                lines_positions[7][2] += speed_x_1
                lines_positions[6][3] -= speed_y_1
                lines_positions[7][3] -= speed_y_1

                lines_positions[0][2] += speed_x_1
                lines_positions[0][3] -= speed_y_1
                lines_positions[4][2] += speed_x_1
                lines_positions[4][3] -= speed_y_1

                if circle_positions[5][1] > 900:
                    speed_x_1 = 0
                if circle_positions[5][2] < 300:
                    speed_y_1 = 0
                if circle_positions[5][1] > 900 and circle_positions[5][2] < 300:
                    break

                pygame.display.flip()
                clock.tick(60)

            speed_x_2 = 2
            while True:
                if circle_positions[1][1] > 1050:
                    break

                circle_positions[1][1] += speed_x_2
                circle_positions[3][1] += speed_x_2
                circle_positions[4][1] += speed_x_2
                circle_positions[6][1] += speed_x_2

                lines_positions[2][0] += speed_x_2
                lines_positions[2][2] += speed_x_2

                lines_positions[3][0] += speed_x_2
                lines_positions[3][2] += speed_x_2

                lines_positions[4][0] += speed_x_2

                lines_positions[5][0] += speed_x_2
                lines_positions[5][2] += speed_x_2

                screen.fill((0, 0, 0))

                draw_circle_positions(screen)
                draw_lines(screen)

                pygame.display.flip()
                clock.tick(60)
            return

        pygame.display.flip()
        clock.tick(60)


def small_left_rotate(screen: pygame.Surface, clock: pygame.time.Clock):
    running = True
    speed = 3

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        speed_x_2 = 2
        while True:
            if circle_positions[1][1] > 1050:
                break

            circle_positions[1][1] += speed_x_2
            circle_positions[3][1] += speed_x_2
            circle_positions[4][1] += speed_x_2
            circle_positions[6][1] += speed_x_2

            lines_positions[2][0] += speed_x_2
            lines_positions[2][2] += speed_x_2

            lines_positions[3][0] += speed_x_2
            lines_positions[3][2] += speed_x_2

            lines_positions[4][0] += speed_x_2

            lines_positions[5][0] += speed_x_2
            lines_positions[5][2] += speed_x_2

            screen.fill((0, 0, 0))

            draw_circle_positions(screen)
            draw_lines(screen)

            pygame.display.flip()
            clock.tick(60)

        speed_y_2 = 2
        while True:
            circle_positions[0][2] += speed_y_2
            lines_positions[1][1] += speed_y_2
            lines_positions[1][3] += speed_y_2
            circle_positions[2][2] += speed_y_2
            lines_positions[0][1] += speed_y_2
            if circle_positions[0][2] > 300:
                lines_positions[0][1] -= 70
                lines_positions[0][3] += 70
                lines_positions[6][0] = circle_positions[0][1] + 35
                lines_positions[6][1] = circle_positions[0][2] + 35
                lines_positions[6][2] -= 70
                break

            screen.fill((0, 0, 0))

            draw_circle_positions(screen)
            draw_lines(screen)

            pygame.display.flip()
            clock.tick(60)

        speed_y_2 = 2
        speed_x_2 = 1.5
        while True:
            circle_positions[0][2] += speed_y_2
            lines_positions[1][1] += speed_y_2
            lines_positions[1][3] += speed_y_2
            circle_positions[2][2] += speed_y_2
            lines_positions[0][1] += speed_y_2
            lines_positions[6][1] += speed_y_2

            circle_positions[7][1] += speed_x_2
            circle_positions[8][1] += speed_x_2
            lines_positions[7][0] += speed_x_2
            lines_positions[7][2] += speed_x_2
            lines_positions[6][2] += speed_x_2

            circle_positions[7][2] += speed_y_2
            circle_positions[8][2] += speed_y_2
            lines_positions[7][1] += speed_y_2
            lines_positions[7][3] += speed_y_2
            lines_positions[6][3] += speed_y_2

            if circle_positions[0][2] > 500:
                break

            screen.fill((0, 0, 0))

            draw_circle_positions(screen)
            draw_lines(screen)

            pygame.display.flip()
            clock.tick(60)

        speed_1 = 2
        while True:
            for pos in circle_positions:
                pos[2] -= speed_1

            for line in lines_positions:
                line[1] -= speed_1
                line[3] -= speed_1

            draw_circle_positions(screen)
            draw_lines(screen)

            if circle_positions[5][2] == 100:
                break

            screen.fill((0, 0, 0))

            draw_circle_positions(screen)
            draw_lines(screen)

            pygame.display.flip()
            clock.tick(60)

        screen.fill((0, 0, 0))

        draw_circle_positions(screen)
        draw_lines(screen)

        pygame.display.flip()
        clock.tick(60)
        return


def move(screen: pygame.Surface, clock: pygame.time.Clock):
    running = True
    speed = 2

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))


        for pos in circle_positions:
            pos[1] -= speed

        for line in lines_positions:
            line[0] -= speed
            line[2] -= speed

        draw_circle_positions(screen)
        draw_lines(screen)

        if circle_positions[0][1] == 600:
            return

        pygame.display.flip()
        clock.tick(60)


def big_left_rotate():
    screen = init()
    sleep(0.5)
    clock = pygame.time.Clock()
    # play_sound()
    draw_first(screen, clock)
    draw_second(screen, clock)
    draw_third(screen, clock)
    draw_fourth(screen, clock)
    draw_fifth(screen, clock)
    draw_sixth(screen, clock)
    draw_seventh(screen, clock)
    draw_eighth(screen, clock)
    draw_ninth(screen, clock)
    small_right_rotate(screen, clock)
    move(screen, clock)
    small_left_rotate(screen, clock)
    wait(screen, clock)
    pygame.quit()


if __name__ == "__main__":
    big_left_rotate()
    
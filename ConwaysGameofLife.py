import numpy as np
import time
import pygame

# Dimensiones de la pantalla
WIDTH, HEIGHT = 500, 500
n_x, n_y = 50, 50
x_size = WIDTH / n_x
y_size = HEIGHT / n_y

pygame.init()  # Inicializar PyGame

# Establecer tamaño de la pantalla
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Colores
BG_COLOR = (10, 10, 10)  # Color de fondo
LIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (128, 128, 128)

# Celdas vivas = 1; Celdas muertas = 0
status = np.zeros((n_x, n_y))  # Inicializar estado de las células

pause_run = False

running = True
while running:

    new_status = np.copy(status)  # Copiar estado

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pause_run = not pause_run

        mouse_click = pygame.mouse.get_pressed()
        if sum(mouse_click) > 0:
            pos_x, pos_y = pygame.mouse.get_pos()
            x, y = int(np.floor(pos_x / x_size)), int(np.floor(pos_y / y_size))
            new_status[x, y] = not mouse_click[2]

    screen.fill(BG_COLOR)  # Limpiar fondo

    for x in range(0, n_x):
        for y in range(0, n_y):

            if not pause_run:
                # Número de vecinos
                n_neigh = (
                    status[(x - 1) % n_x, (y - 1) % n_y]
                    + status[(x) % n_x, (y - 1) % n_y]
                    + status[(x + 1) % n_x, (y - 1) % n_y]
                    + status[(x - 1) % n_x, (y) % n_y]
                    + status[(x + 1) % n_x, (y) % n_y]
                    + status[(x - 1) % n_x, (y + 1) % n_y]
                    + status[(x) % n_x, (y + 1) % n_y]
                    + status[(x + 1) % n_x, (y + 1) % n_y]
                )

                # Regla 1: Una célula muerta con 3 vecinas revive
                if status[x, y] == 0 and n_neigh == 3:
                    new_status[x, y] = 1

                # Regla 2: Una célula viva con más de 3 vecinos o menos de 2 muere
                elif status[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    new_status[x, y] = 0

            poly = [
                (x * x_size, y * y_size),
                ((x + 1) * x_size, y * y_size),
                ((x + 1) * x_size, (y + 1) * y_size),
                (x * x_size, (y + 1) * y_size),
            ]
            if new_status[x, y] == 1:
                pygame.draw.polygon(screen, LIVE_COLOR, poly, 0)
            else:
                pygame.draw.polygon(screen, DEAD_COLOR, poly, 1)

    status = np.copy(new_status)  # Actualizar estado de las células
    time.sleep(0.05)
    pygame.display.flip()


pygame.quit()

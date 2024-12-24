import pygame
import pygame.time

# Inicializamos Pygame
pygame.init()

# Dimensiones de la ventana
ancho_pantalla = 640
alto_pantalla = 480
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Cargamos la imagen del sprite
sprite_sheet = pygame.image.load("GandalfHardcore fox.png")

# Obtenemos las dimensiones de una imagen individual
ancho_imagen, alto_imagen = 32, 32

# Creamos una lista para almacenar las imágenes individuales
imagenes = []
for fila in range(2):
    for columna in range(6):
        imagen_recortada = sprite_sheet.subsurface(columna * ancho_imagen, fila * alto_imagen, ancho_imagen - 1, alto_imagen - 1)
        imagenes.append(imagen_recortada)

# Variables para controlar la animación y el movimiento
indice_imagen = 0
velocidad_animacion = 10
x, y = 0, 0  # Posición inicial del zorro
velocidad_x = 5  # Velocidad de movimiento horizontal
velocidad_y = 0  # Velocidad de movimiento vertical
filas = 2  # Número de filas en la animación
columnas = 8  # Número de columnas en la animación

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizamos la imagen a mostrar
    indice_imagen += 1
    if indice_imagen >= len(imagenes):
        indice_imagen = 0

    # Actualizamos la posición del zorro
    x += velocidad_x
    if x >= ancho_pantalla - ancho_imagen:
        x = 0
        y += alto_imagen
        if y >= alto_pantalla:
            y = 0

    # Dibujamos la imagen en la pantalla
    pantalla.fill((0, 0, 0))
    pantalla.blit(imagenes[indice_imagen], (x, y))

    # Actualizamos la pantalla
    pygame.display.flip()
    clock = pygame.time.Clock()
    # Limitamos los FPS
    clock.tick(velocidad_animacion)

# Salimos de Pygame
pygame.quit()
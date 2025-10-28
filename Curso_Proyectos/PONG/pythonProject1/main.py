import pygame as pg


#configurar el ancho y el ato de la pantalla
#MAYUSCULAS SIGNIFICAN QUE ESTAS VARIABLES SE MANTENDRAN CONSTANTES
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 600
pantalla = pg.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
#Titulo e icono
pg.display.set_caption("Pong")
ruta_icono = "C:/Users/EDMG0/Documents/Proyectos_python/Curso_Proyectos/PONG/pythonProject1/pong.png"
icono = pg.image.load("pong.png")
pg.display.set_icon(icono)
#variables de inicializacion
ejecutando = True
mi_reloj = pg.time.Clock()


#Paleta de colores
BLANCO = (255, 255 ,255)
COLOR_FONDO = (150, 200 ,170)
AZUL = (70, 130, 180)
ROJO = (200, 70, 90)
NEGRO = (0,0,0)
# Definir sonidos
pg.mixer.init()
sonido_golpe_paleta = pg.mixer.Sound("golpe_paleta.mp3")
sonido_golpe_pared = pg.mixer.Sound("golpe_pared.mp3")
sonido_punto =pg.mixer.Sound("punto.mp3")
sonido_golpe_paleta.set_volume(.5)
sonido_punto.set_volume(.5)
sonido_golpe_pared.set_volume(.5)


# Coordenadas y tamaños de jugadores
j1_x = 50
j1_y = 250
j2_x = 820
j2_y = 250
ANCHO_PALETA = 30
ALTO_PALETA = 100

#Coordenadas y dimensiones de la pelota
pelota_x = 450
pelota_y = 300
ANCHO_PELOTA = 10
ALTO_PELOTA = 10
pelota_diferencia_x = 4
pelota_diferencia_y = 4
#puntajes iniciales
puntos_j1=0
puntos_j2=0
#Definir las fuentes
pg.font.init()
comic_sands_25 = pg.font.SysFont("Comic Sans MS", 25)

comic_sands_35 = pg.font.SysFont("Comic Sans MS", 35)
comic_sands_120 = pg.font.SysFont(("Comic Sans MS"), 120)
#Crear elementos del juego
paleta_j1 = pg.Rect(j1_x,j1_y,ANCHO_PALETA,ALTO_PALETA)
paleta_j2 = pg.Rect(j2_x,j2_y,ANCHO_PALETA,ALTO_PALETA)
pelota = pg.Rect(pelota_x,pelota_y,ANCHO_PELOTA,ALTO_PELOTA)

def mostrar_menu_inicial():
    pantalla.fill(NEGRO)
    titulo = comic_sands_120.render("PONG", True, BLANCO)
    icono_escalado = pg.transform.scale(icono, (titulo.get_height(),titulo.get_height()))
    pantalla.blit(titulo, (ANCHO_PANTALLA//2-titulo.get_width()//2 , ALTO_PANTALLA//2 - 300 ))
    pantalla.blit(icono_escalado, (ANCHO_PANTALLA // 2 + titulo.get_width() //2 + 10 , ALTO_PANTALLA // 2 - 300))
    mensaje_inicio = comic_sands_35.render("A cuántos puntos jugamos esta partida?", True , BLANCO)
    pantalla.blit(mensaje_inicio, (ANCHO_PANTALLA//2-mensaje_inicio.get_width()//2 , ALTO_PANTALLA//2 - 100 ))

    opcion_5 = comic_sands_25.render("5(1)", True, BLANCO)
    pantalla.blit(opcion_5, (ANCHO_PANTALLA // 2 - 200 // 2, ALTO_PANTALLA // 2 - 40))
    opcion_10 = comic_sands_25.render("10(2)", True, BLANCO)
    pantalla.blit(opcion_10, (ANCHO_PANTALLA // 2 - 200 // 2, ALTO_PANTALLA // 2 ))
    opcion_15 = comic_sands_25.render("15(3)", True, BLANCO)
    pantalla.blit(opcion_15, (ANCHO_PANTALLA // 2 - 200 // 2, ALTO_PANTALLA // 2 + 40))

    pg.display.flip()
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_1:
                    return 5
                elif e.key == pg.K_2:
                    return 10
                elif e.key == pg.K_3:
                    return 15

        mi_reloj.tick(10)
def dibujar_pantalla():
    pantalla.fill(COLOR_FONDO)
    pg.draw.rect(pantalla,AZUL,paleta_j1)
    pg.draw.rect(pantalla,ROJO,paleta_j2)
    pg.draw.rect(pantalla,BLANCO,pelota)
    texto_puntos_j1 = comic_sands_35.render("PUNTOS J1:" + str(puntos_j1), True, AZUL)
    texto_puntos_j2 = comic_sands_35.render("PUNTOS J2:" + str(puntos_j2), True, ROJO)
    pantalla.blit(texto_puntos_j1, (130,20))
    pantalla.blit(texto_puntos_j2, (620, 20))

def verificar_ganador():
    if puntos_j1 >= puntos_para_ganar:
        return "Jugador 1"
    elif puntos_j2 >= puntos_para_ganar:
        return "Jugador 2"
    return None

def mostrar_ganador():
    pantalla.fill(NEGRO)
    mensaje = comic_sands_35.render("HA GANADO " + ganador , True, BLANCO)
    pantalla.blit(mensaje,(ANCHO_PANTALLA//2 - mensaje.get_width()//2,ALTO_PANTALLA//2))

    mensaje_reinicio = comic_sands_35.render("Quieres volver a jugar?", True, BLANCO)
    pantalla.blit(mensaje_reinicio,(ANCHO_PANTALLA//2 - mensaje_reinicio.get_width()//2,ALTO_PANTALLA//2+100))

    mensaje_si = comic_sands_35.render("Si", True, BLANCO)
    pantalla.blit(mensaje_si,(ANCHO_PANTALLA//2-50 - mensaje_si.get_width()//2,ALTO_PANTALLA//2+200))

    mensaje_no = comic_sands_35.render("No", True, BLANCO)
    pantalla.blit(mensaje_no,(ANCHO_PANTALLA//2+50- mensaje_no.get_width()//2,ALTO_PANTALLA//2+200))
    pg.display.flip()
    while True :
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            if e.type ==pg.KEYDOWN:
                if e.key == pg.K_s:
                    return True
            if e.key == pg.K_n:
                return False
        mi_reloj.tick(10)

def resetear_pelota_y_paletas():
    global pelota_x, pelota_y , pelota_diferencia_x , pelota_diferencia_y, j1_y , j2_y
    pelota_x = 450
    pelota_y = 300
    pelota_diferencia_x = 4
    pelota_diferencia_y = 4
    j1_y = 250
    j2_y = 250



    # Loop principal
while ejecutando:

    #Mostrar el menu inicial
    puntos_para_ganar = mostrar_menu_inicial()
    jugando = True
    while jugando:

        #Verificar cierre del juego
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                ejecutando = False
                jugando = False
                break
        if not ejecutando :
            break
        # Definir evento presionar teclas
        teclas = pg.key.get_pressed()
        # Actualizar posiciones de elementos
        paleta_j1.y = j1_y
        paleta_j2.y = j2_y
        pelota.x = pelota_x
        pelota.y = pelota_y
        #redefinir coordernadas de las paletas
        if teclas[pg.K_w] and j1_y >0:
            j1_y -= 5
        elif teclas[pg.K_s] and j1_y + ALTO_PALETA < ALTO_PANTALLA:
            j1_y += 5

        if teclas[pg.K_UP] and j2_y >0:
            j2_y -= 5
        elif teclas[pg.K_DOWN] and j2_y + ALTO_PALETA < ALTO_PANTALLA:
            j2_y += 5

        # Redefinir coordenadas de la pelota
        pelota_x += pelota_diferencia_x
        pelota_y += pelota_diferencia_y

        #verificar colisiones en cada movimiento
        if pelota.colliderect(paleta_j1):
            sonido_golpe_paleta.play()
            pelota_diferencia_x = abs(pelota_diferencia_x)
        elif pelota.colliderect(paleta_j2):
            pelota_diferencia_x = abs(pelota_diferencia_x)*-1
            sonido_golpe_paleta.play()
        elif pelota_y <= 0 :
            pelota_diferencia_y = abs(pelota_diferencia_y)
            sonido_golpe_pared.play()
        elif pelota_y >=ALTO_PANTALLA:
            pelota_diferencia_y = abs(pelota_diferencia_y)*-1
            sonido_golpe_pared.play()
        elif pelota_x <=0 or pelota_x >= ANCHO_PANTALLA :
            sonido_punto.play()
            if pelota_x >=ANCHO_PANTALLA:
                puntos_j1 +=1
            elif pelota_x<= 0:
                puntos_j2 +=1
            resetear_pelota_y_paletas()
            # Verificar si hay un ganador antes de resetear la pantalla
            ganador = verificar_ganador()
            if ganador:
                #preguntar si quieren volver a jugar
                # si ganador regresa con False se cierra el juego
                if not mostrar_ganador():
                    ejecutando = False
                    jugando = False
                    break
                # si "ganador regresa con True
                else:
                    # si decide volver a jugar reiniciar puntos y continuar
                    puntos_j1= 0
                    puntos_j2= 0
                    resetear_pelota_y_paletas()
                    break
            resetear_pelota_y_paletas()




        dibujar_pantalla()
        pg.display.flip()
        mi_reloj.tick(60)
# PARA CERRAR EL PROGRAMA
pg.quit()
quit()


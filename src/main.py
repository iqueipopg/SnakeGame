import pygame
from pygame import Vector2
import random
import funciones as f
import objetos as ob

if __name__ == '__main__':

    pygame.init()
    VENTANA = f.pantalla()

    ### objetos
    serpiente = ob.serp()
    manzana_roja = ob.fruta()
    manzana_morada = ob.fruta()
    manzana_azul = ob.fruta()  # num_random 0
    manzana_azul.posicion = Vector2(1000, 1000)
    manzana_naranja = ob.fruta()  # nun_random 2
    manzana_naranja.posicion = Vector2(1000, 1000)
    manzana_rosa = ob.fruta()
    manzana_rosa.posicion = Vector2(1000, 1000)

    ### listas
    lista_manzanas_moradas = [manzana_morada]   # lista de objetos con todas las manzanas moradas

    ### contadores
    cont_marcador = 0
    cont_morado = 0
    cont_azul = 3
    cont_azul_pantalla = 0
    cont_naranja = 1
    cont_rosa = 1
    num_random = random.randint(0, 2)

    # booleanos
    running = True   # me controla todos los power ups
    game_over = False
    win = False
    pausa = False
    started = False
    instrucciones = False

    # sonidos
    pygame.mixer.music.load('extras\sonidos\pack.mp3')
    pygame.mixer.music.play(-1)
    s_comer = pygame.mixer.Sound('extras\sonidos\comer.mp3')
    s_game_over = pygame.mixer.Sound('extras\sonidos\game_over.mp3')
    s_victoria = pygame.mixer.Sound('extras\sonidos\win.mp3')
    s_silencio = pygame.mixer.Sound('extras\sonidos\silencio.mp3')
    s_power_up = pygame.mixer.Sound('extras\sonidos\power_up.mp3')
    s_power_up.set_volume(0.15)   # bajo el volumen xq es muy alto
    s_victoria.set_volume(0.2)

    ### otros
    fps = pygame.time.Clock()
    marcador_final = 50
    marcador = pygame.font.SysFont('Russo one', 20)

    ### bucle principal
    while True:
        if not started and not instrucciones:   # no ha empezado y no quiere instrucciones
            f.pantalla_inicio(VENTANA)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        started = True
                    if event.key == pygame.K_RETURN:
                        instrucciones = not instrucciones
        elif not started and instrucciones:   # no ha empezado y quiere instrucciones
            f.pantalla_instrucciones(VENTANA)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        instrucciones = not instrucciones

        elif pausa:   # ha pausado
            pygame.time.wait(1)   # detiene el juego un milisegundo hasta que presione espacio
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pausa = not pausa
        
        elif started:   # ha empezado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN and serpiente.dir.y != 10:   
                    if event.key == pygame.K_UP:
                        serpiente.arriba()
                if event.type == pygame.KEYDOWN and serpiente.dir.y != -10:
                    if event.key == pygame.K_DOWN:
                        serpiente.abajo()
                if event.type == pygame.KEYDOWN and serpiente.dir.x != -10:
                    if event.key == pygame.K_RIGHT:
                        serpiente.derecha()
                if event.type == pygame.KEYDOWN and serpiente.dir.x != 10:
                    if event.key == pygame.K_LEFT:
                        serpiente.izquierda()
                # los != 10 son para la logística del juego, de manera que la serpiente no se pueda desplazar al lado del que viene
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if game_over or win:    # resetea el juego gane o pierda
                            ### objetos
                            serpiente = ob.serp()
                            manzana_roja = ob.fruta()
                            manzana_morada = ob.fruta()
                            manzana_azul = ob.fruta()  # num_random 0
                            manzana_azul.posicion = Vector2(1000, 1000)
                            manzana_naranja = ob.fruta()  # nun_random 1
                            manzana_naranja.posicion = Vector2(1000, 1000)
                            manzana_rosa = ob.fruta()  # num random 2
                            manzana_rosa.posicion = Vector2(1000, 1000)

                            ### listas
                            lista_manzanas_moradas = [manzana_morada]   # lista de objetos con todas las manzanas moradas
                            
                            ### contadores
                            cont_marcador = 0
                            cont_morado = 0
                            cont_azul = 3
                            cont_naranja = 1
                            cont_rosa = 1
                            num_random = random.randint(0, 2)

                            ### booleanos
                            running = True
                            game_over = False
                            win = False

                            s_game_over = pygame.mixer.Sound('extras\sonidos\game_over.mp3')
                            s_victoria = pygame.mixer.Sound('extras\sonidos\win.mp3')
                            pygame.mixer.music.play(-1)
                        
                        else:
                            pausa = not pausa
            
            f.draw_cuadricula(VENTANA)

            #### zona de dibujo
            serpiente.dibujar()
            manzana_roja.dibujar_rojo()
            manzana_azul.dibujar_azul()
            manzana_naranja.dibujar_naranja()
            manzana_rosa. dibujar_rosa()
            for manzana in lista_manzanas_moradas:
                manzana.dibujar_morado()
            
            #### lógica del juego
            if win or game_over:
                pygame.mixer.music.stop()
                f.fin(game_over, win, s_victoria, s_game_over, VENTANA)
                s_game_over = s_silencio
                s_victoria = s_silencio
            
            serpiente.mover()

            if serpiente.morir():
                game_over = True

            if manzana_roja.comer(serpiente):   # lo que ocurre cuando una manzana roja es comida
                if cont_marcador < (marcador_final - 1):
                    s_comer.play()
                cont_marcador += 1
                cont_morado += 1
                cont_azul += 1
                cont_rosa += 1
                cont_naranja += 1
                num_random = random.randint(0, 5)
                manzana_roja.aparecer()
                f.check_objwserp(serpiente, manzana_roja) 


            for manzana1 in lista_manzanas_moradas:
                if manzana1.comer(serpiente):
                    game_over = True
                f.check_objwobj(manzana1, manzana_roja)    # no aparezca manzana roja en morada
                for manzana2 in lista_manzanas_moradas:
                    if manzana1 != manzana2:   # no aparezca 2 manzanas moradas en el mismo sitio
                        f.check_objwobj(manzana1, manzana2)
            
            if cont_azul > 2 and cont_naranja > 0 and cont_rosa > 0 and running:  # para que no entre en caso de que algún power up esté en curso
                for manzana in lista_manzanas_moradas:
                    if num_random == 0:
                        manzana_azul = ob.fruta()
                        f.check_objwobj(manzana, manzana_azul)   # no aparezca manzana en morada
                        f.check_objwobj(manzana_roja, manzana_azul)
                        f.check_objwserp(serpiente, manzana_azul)
                        running = False
                    elif num_random == 1:
                        manzana_naranja = ob.fruta()
                        f.check_objwobj(manzana, manzana_naranja)   # no aparezca manzana en morada
                        f.check_objwobj(manzana_roja, manzana_naranja)
                        f.check_objwserp(serpiente, manzana_naranja)
                        running = False
                    elif num_random == 2 and len(lista_manzanas_moradas) > 1:
                        manzana_rosa = ob.fruta()
                        f.check_objwobj(manzana, manzana_rosa)   # no aparezca manzana en morada
                        f.check_objwobj(manzana_roja, manzana_naranja) 
                        f.check_objwserp(serpiente, manzana_rosa)
                        running = False
                num_random = -1
                # running = False no puede estar fuera porque en caso de no tocar un power_up, no tocará nunca más

            if manzana_azul.comer(serpiente):
                s_power_up.play()
                cont_azul = 0
                manzana_azul.posicion = Vector2(1000, 1000)
                running = True
            
            if manzana_naranja.comer(serpiente):
                if cont_marcador < (marcador_final - 4):   
                    s_power_up.play()
                cont_marcador += 3
                cont_naranja = 0
                manzana_naranja.posicion = Vector2(1000, 1000)
                running = True
            
            if manzana_rosa.comer(serpiente):
                s_power_up.play()
                lista_manzanas_moradas = f.pop_rosa(lista_manzanas_moradas)
                cont_rosa = 0
                manzana_rosa.posicion = Vector2(1000, 1000)
                running = True

            f.power_up_azul(cont_azul, fps)

            if cont_morado == 3:
                cont_morado = 0
                lista_manzanas_moradas = f.lista_morado(lista_manzanas_moradas, serpiente)
            
            ### condicion para ganar
            if cont_marcador >= marcador_final: 
                win = True
        
            #### actualización de pantalla
            if cont_azul > 2:
                cont_azul_pantalla = 3
            else:
                cont_azul_pantalla = cont_azul
            texto_marcador = marcador.render('Score: {}'.format(cont_marcador), 1, (30, 33, 27))
            texto_cont_azul = marcador.render('End p_up: {}'.format(3-cont_azul_pantalla), 1, (30, 33, 27))
            VENTANA.blit(texto_marcador, (700-texto_marcador.get_width()-10, 10))
            VENTANA.blit(texto_cont_azul, (620-texto_cont_azul.get_width()-10, 10))

            pygame.display.update()
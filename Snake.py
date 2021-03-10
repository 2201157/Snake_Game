import pygame
import pygame_widgets as pw
import random


#--------- INICIO ---------#

largura = 1000
altura = 600
fps = 120

branco = (255,255,255)
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("SNAKE") # TITULO DO JOGO
clock = pygame.time.Clock()

#--------- INICIO ---------#





# ------------------------------- CLASSES -------------------------------------#

class Jogador (pygame.sprite.Sprite):



    def __init__(self):

        super(Jogador, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('jogo/img/snake/snake_esquerda_1.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_esquerda_0.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_esquerda_2.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_esquerda_0.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_direita_1.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_direita_0.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_direita_2.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_direita_0.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_cima_0.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_cima_1.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_cima_2.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_baixo_0.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_baixo_1.png'))
        self.images.append(pygame.image.load('jogo/img/snake/snake_baixo_2.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(500,300, 30, 30)
        self.y_speed = 0
        self.x_speed = 0
        self.score = 0
        self.intervalo = 100
        self.ultimo_update = 0

    def update(self):


        keys = pygame.key.get_pressed()

        self.image = self.images[self.index]
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed


        if  keys[pygame.K_UP] or keys[pygame.K_w]:




            if self.index + 1 > 10 or self.index < 8:
                self.index = 8

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:

                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()

            self.y_speed = -2
            self.x_speed = 0


        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:

            if self.index + 1 > 13 or self.index < 11:
                self.index = 11

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:
                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()

            self.y_speed = 2
            self.x_speed = 0
            pygame.display.update()

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            if self.index + 1 > 7 or self.index < 4:
                self.index = 4

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:

                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()

            self.x_speed = 2
            self.y_speed = 0


        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:

            if self.index + 1 > 3 or self.index > 3:
                self.index = 0

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:

                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()

            self.y_speed = 0
            self.x_speed = -2



class Maca(pygame.sprite.Sprite):

        def __init__(self):

            pygame.sprite.Sprite.__init__(self)
            self.pegar =  pygame.mixer.Sound('jogo/img/sound_effect/pegar_maca.wav')
            self.pegar_inimigo = pygame.mixer.Sound('jogo/img/sound_effect/pegar_maca_inimigo.wav')
            self.image = pygame.image.load('jogo/img/maca_sprite.png')
            self.image = pygame.transform.scale(self.image,(30,30))
            self.rect = self.image.get_rect()
            self.rect.center = (round(random.randrange(30,largura - jogador.rect.x)/10)*10,round(random.randrange(30,altura - jogador.rect.y)/10)*10)

        def checkCollision(self, sprite1, sprite2):

            col = pygame.sprite.collide_rect(sprite1, sprite2)

            if col == True:
                pygame.mixer.Sound.play(self.pegar)
                pygame.mixer.music.stop()
                jogador.score += 5


                self.rect.center = (round(random.randrange(30, largura - jogador.rect.x) / 10) * 10,
                                    round(random.randrange(30, altura - jogador.rect.y) / 10) * 10)

        def checkCollision_inimigo(self, sprite1, sprite2):

            col = pygame.sprite.collide_rect(sprite1, sprite2)

            if col == True:

                pygame.mixer.Sound.play(self.pegar_inimigo)
                pygame.mixer.music.stop()

                jogador.score -= 15


                self.rect.center = (round(random.randrange(10, largura - jogador.rect.x) / 10) * 10,
                                    round(random.randrange(10, altura - jogador.rect.y) / 10) * 10)



class Inimigo(pygame.sprite.Sprite):


    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.hit_sound = pygame.mixer.Sound('jogo/img/sound_effect/inimigo_hit.wav')

        self.images = []
        self.images.append(pygame.image.load('jogo/enemy/human_down_1.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_down_2.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_up_1.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_up_2.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_left_1.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_left_2.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_left_1.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_right_1.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_right_2.png'))
        self.images.append(pygame.image.load('jogo/enemy/human_right_1.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(100, 200, 25, 32)
        self.ultimo_x = 0
        self.ultimo_y = 0
        self.intervalo = 100
        self.ultimo_update = 0
        self.speed = 2


    def update(self):

        self.image = self.images[self.index]
        self.ultimo_x = self.rect.x
        self.ultimo_y = self.rect.y



        # a var "vetor2" recebe uma tuple com a diferenca de x e y entre o jogador e o inimigo
        vetor2 =    pygame.math.Vector2 (jogador.rect.x - self.rect.x,
                                         jogador.rect.y - self.rect.y)




        vetor2.normalize() # retorna um vetor com o mesmo tamanho só que com o tamanho de 1



        vetor2.scale_to_length(self.speed) #faz com que o inimigo avance até as coordenadas armazenadas no vetor2

        self.rect.move_ip(vetor2)

        if self.ultimo_x > self.rect.x:

            if self.index + 1 > 7 or self.index < 5:
                self.index = 5

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:
                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()


            pygame.display.update()

        elif self.ultimo_x < self.rect.x:

            if self.index + 1 > 9 or self.index < 7:
                self.index = 7

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:
                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()


            pygame.display.update()


        elif self.ultimo_y < self.rect.y:

            if self.index + 1 > 1 :
                self.index = 0

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:
                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()


            pygame.display.update()

        elif self.ultimo_y > self.rect.y:

            if self.index + 1 > 3 or self.index < 2 :
                self.index = 2

            if pygame.time.get_ticks() - self.ultimo_update > self.intervalo:
                self.index += 1
                self.ultimo_update = pygame.time.get_ticks()


            pygame.display.update()








# ------------------------------- CLASSES -------------------------------------#





# -------------------- VARIAVEIS ---------------------#

todos_os_sprites = pygame.sprite.Group()
sprites_inimigos = pygame.sprite.Group()

human = Inimigo()
jogador = Jogador()
maca = Maca()
sprites_inimigos.add(human)
todos_os_sprites.add(jogador)
todos_os_sprites.add(maca)



preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

background = pygame.image.load('jogo/img/foto_fundo_inicio.jpg').convert()
background = pygame.transform.scale(background,(largura,altura))

background_nivel_1 = pygame.image.load('jogo/img/bg_lv_1.jpg').convert()
background_nivel_1 = pygame.transform.scale(background_nivel_1,(largura,altura))


snake_logo = pygame.image.load('jogo/img/snake_logo.png')
snake_logo = pygame.transform.scale(snake_logo,(150,100))


titulo = pygame.font.SysFont('Corbel',100)
texto = pygame.font.SysFont('Corbel',15)

titulo = titulo.render('S N A K E ', True,preto) # TITULO
creator = texto.render('Made by Masamune', True,preto) #Creditos

# -------------------- VARIAVEIS ---------------------#



# -------------------- FUNÇÕES -----------------------#


def condicoes_de_derrota():


    if pygame.sprite.collide_rect(human, jogador) == 1:

        pygame.mixer.Sound.play(human.hit_sound)
        pygame.mixer.music.stop()

        human.rect.x = 50
        human.rect.y = 200
        jogador.rect.x = 500
        jogador.rect.y = 300
        jogador.score = 0
        jogador.y_speed = 0
        jogador.x_speed = 0

        GAMEOVER = True

        return GAMEOVER

    if (jogador.rect.x >= 1000 or jogador.rect.x <= 0) or (jogador.rect.y >= 600 or jogador.rect.y <= 0):

        pygame.mixer.Sound.play(human.hit_sound)
        pygame.mixer.music.stop()

        jogador.rect.x = 500
        jogador.rect.y = 300
        jogador.score = 0
        jogador.y_speed = 0
        jogador.x_speed = 0

        GAMEOVER = True

        return GAMEOVER


    if jogador.score < 0:

        pygame.mixer.Sound.play(human.hit_sound)
        pygame.mixer.music.stop()

        jogador.rect.x = 500
        jogador.rect.y = 300
        jogador.score = 0
        jogador.y_speed = 0
        jogador.x_speed = 0

        GAMEOVER = True

        return GAMEOVER







def carregar_tela_jogar():

    pygame.mixer.Sound.play(botao_sound)
    pygame.mixer.music.stop()

    GAMEOVER = False



    while GAMEOVER != True:


        screen.blit(background_nivel_1, [0, 0])

        score = texto.render(f'Pontuação  {jogador.score}', True, preto)  # pontuação

        screen.blit(score, [5, 10])

        todos_os_sprites.draw(screen)

        sprites_inimigos.draw(screen)

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                GAMEOVER = True


        if condicoes_de_derrota() == True:

            GAMEOVER = True

        maca.checkCollision(jogador,maca)
        maca.checkCollision_inimigo(human,maca)

        todos_os_sprites.update()
        sprites_inimigos.update()

        clock.tick(fps)
        pygame.display.flip()

    return 0



# -------------------- FUNÇÕES -----------------------#




# -------------------- BOTÕES -----------------------#

botao_sound = pygame.mixer.Sound('jogo/img/sound_effect/menu_botao.wav')

botao_de_quit = pw.Button(
                          screen,425,475,130,70,text='Sair',
                          fontSize=50,textColour=(0, 0, 0),
                          margin=20,inactiveColour=(150,150,150),
                          pressedColour=(0,255,0),radius=20,onClick=lambda:pygame.quit()
                          )

botao_de_jogar = pw.Button(
                          screen,420,375,140,70,text='Jogar',
                          fontSize=50,textColour=(0, 0, 0),
                          margin=20,inactiveColour=(150,150,150),
                          pressedColour=(0,255,0),radius=20,onClick=lambda:carregar_tela_jogar()
                          )

# -------------------- BOTÕES -----------------------#







# ------------------- LOOP DO JOGO ---------------------------#

running = True


while running:



    screen.blit(background, [0, 0])
    screen.blit(snake_logo, [120, 50])
    screen.blit(titulo, [310, 50])
    screen.blit(creator, [870, 580])
    botao_de_quit.draw()
    botao_de_jogar.draw()


    clock.tick(fps)

    for eventos in pygame.event.get():

        if eventos.type == pygame.QUIT:

            running = False




    botao_de_quit.listen(eventos)
    botao_de_jogar.listen(eventos)



    pygame.display.flip()

pygame.quit()


# ------------------- LOOP DO JOGO ---------------------------#

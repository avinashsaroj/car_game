import pygame,time,random,sys,os
from pygame.locals import *
pygame.init()

width=390
height=600
clk=pygame.time.Clock()
window=pygame.display.set_mode((width,height))
pygame.display.set_caption('Baby Avinash driving')
backgroundcolor=(255,255,255)
textcolor=(0,0,0)
'''background_image = pygame.image.load("background.png").convert()
window.blit(background_image, [0, 0])'''
'''background_image = pygame.image.load("car3.png").convert()
window.blit(background_image, [0, 0])'''

playerimage=pygame.image.load('me.png')
oppositeimage=pygame.image.load('opp.png')
playerrect=playerimage.get_rect()
#pygame.mouse.set_visible(False)
FPS=40
pygame.display.update()
oppositeminspeed=10
oppositemaxspeed=10
oppositeminsize=10
oppositemaxsize=40
oppositerate=5
playermoverate=10
count=3
fon=pygame.font.SysFont(None,40)
sample=[oppositeimage]
#pygame.mixer.Sound('music.wav')
def collision(playerrect,opposite):
    for b in opposite:
        if playerrect.colliderect(b['rect']):
            return True
    return False

def highscore(text,fon,window,x,y):
    textobj=fon.render(text,1,textcolor)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    window.blit(textobj,textrect)


def loop():
    close = False
    bads=[]
    score=0
    #gameover = False
    playerrect.topleft=(width/2,height-50)
    left=right=False
    reversecheat=slowcheat=False
    oppositeaddcounter=0
    #pygame.mixer.music.play(-1, 0.0)

    while not close:
        score+=1

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True

            if  event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    left=True
                    right=False
                if event.key==pygame.K_RIGHT:
                    right=True
                    left=False

            if event.type== pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    left=False
                if event.key==pygame.K_RIGHT:
                    right=False




        if not reversecheat and not slowcheat:
            oppositeaddcounter+=1
        if oppositeaddcounter==oppositerate:
            oppositeaddcounter=0


            oppositesize=30
            newopposite={'rect':pygame.Rect(random.randint(5,370),oppositesize,20,50),'speed':random.randint(oppositeminspeed,oppositemaxspeed),'surface':pygame.transform.scale(random.choice(sample),(20,50)),}
            bads.append(newopposite)

        if left and playerrect.left>0:
            playerrect.move_ip(-1*playermoverate,0)
        if right and playerrect.right<width:
            playerrect.move_ip(playermoverate,0)

        for b in bads:
            if not reversecheat and not slowcheat:
                b['rect'].move_ip(0,b['speed'])
            elif reversecheat:
                b['rect'].move_ip(0,-5)
            elif slowcheat:
                b['rect'].move_ip(0,1)

        for b in bads[:]:
            if b['rect'].top>height:
                bads.remove(b)
        window.fill(backgroundcolor)
        highscore('Score: %s' % (score), fon, window, 128, 0)
        window.blit(playerimage,playerrect)

        for b in bads:
            window.blit(b['surface'],b['rect'])

        pygame.display.update()


        if collision(playerrect,bads):
            break






        clk.tick(20)
    #pygame.mixer.music.stop()

    time.sleep(1)

    pygame.quit()
    quit()
loop()

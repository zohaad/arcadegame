import pygame, pixelperfect, time
from pygame.locals import *
from pixelperfect import *
 
def load_image(name, colorkey=None, alpha=False):
    """loads an image into memory"""
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if alpha:image = image.convert_alpha()
    else:image=image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
 
class my_object(object):
    def __init__(self, image,colorkey=None,alpha=None):
        self.image, self.rect=load_image(image,colorkey=colorkey, alpha=alpha)
        if colorkey and alpha:
            self.hitmask=get_colorkey_and_alpha_hitmask(self.image, self.rect,
                                                        colorkey, alpha)
        elif colorkey:
            self.hitmask=get_colorkey_hitmask(self.image, self.rect,
                                              colorkey)
        elif alpha:
            self.hitmask=get_alpha_hitmask(self.image, self.rect,
                                           alpha)
        else:
            self.hitmask=get_full_hitmask(self.image, self.rect)
 
pygame.init()
screen = pygame.display.set_mode([200,200])
screen.fill([255,255,255])
 
 
a=my_object('carrots.png',-1,None)
a.rect.center=(25,25)
 
b=my_object('carrots.png',None,True)
b.rect.center=(50,50)
 
screen.blit(a.image, a.rect)
screen.blit(b.image, b.rect)
pygame.display.flip()
 
def main():
    av=0
    for i in xrange(999):
        st_time=time.clock()
        check_collision(a, b)
        av+=time.clock()-st_time
 
    print "time:", av, check_collision(a, b)
 
main()
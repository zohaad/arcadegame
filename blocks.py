from constants import *
from pixelperfect import *

class Block(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height, mask=False):
        """ Block constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super(Block, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

class MaskedBlock(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height, mask, background):
        """ Block constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super(MaskedBlock, self).__init__()

        face = pygame.image.load(background).convert_alpha()

        self.image = pygame.Surface([width, height]).convert_alpha()
        self.image.fill((205, 210, 218))
        self.image.blit(face, (0,0))
        self.rect = self.image.get_rect()

        self.maskSurface = pygame.Surface([width, height])
        self.maskSurface.set_colorkey((255,0,255))
        self.maskSurface.blit(pygame.image.load(mask), (0,0))
        self.mask = pygame.mask.from_surface(self.maskSurface)
        #self.mask = get_colorkey_hitmask(pygame.image.load(mask), self.rect, (0,0,0))
        
        
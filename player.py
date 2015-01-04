from spritesheetanim import SpriteStripAnim
from constants import *

class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super(Player, self).__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.width = 45
        self.height = 39

        self.leftanim = SpriteStripAnim('entities/sheep_left.png', (0,0,45,39), 4, (255,0,255), True, FRAME_RATE/8)
        self.rightanim = SpriteStripAnim('entities/sheep_right.png', (0,0,45,39), 4, (255,0,255), True, FRAME_RATE/8)

        self.dir = 1
        self.jumping = 0

        self.image = self.rightanim.next()
        #self.image.blit(pygame.image.load("entities/Sheep_Walking_Right.gif"), (0,0))
        
        # Set a referance to the image rect.
        self.rect = pygame.Rect(0,0,45,39)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        if self.change_x > 0:
            self.image = self.rightanim.next()
            self.dir = 1
        elif self.change_x < 0:
            self.image = self.leftanim.next()
            self.dir = -1
        else:
            if self.dir == 1:
                self.image = self.rightanim.reset()
            else:
                self.image = self.leftanim.reset()
            
        # Move up/down
        self.rect.y += self.change_y
        self.rect.x += self.change_x

        # Check and see if we hit anything
        # block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False, pygame.sprite.collide_mask)
        # for block in block_hit_list:

        #     # Reset our position based on the top/bottom of the object.
        #     if self.change_y > 0:
        #         self.rect.bottom = block.rect.top
        #     elif self.change_y < 0:
        #         self.rect.top = block.rect.bottom

        #     # Stop our vertical movement
        #     self.change_y = 0

        for block in self.level.platform_list:
            # TODO: first check with self.rect.colliderect(block.rect) if not main platform
            if self.rect.colliderect(block.rect):

                # if self.dir == 1:
                #     offset_x = self.rect.x + self.width/4*3 - block.rect.x
                # else:
                #     offset_x = self.rect.x - block.rect.x
                # offset_y = self.rect.y + self.height - block.rect.y
                # #print("Block ", block, offset_x, offset_y)

                offset_x = self.rect.x - block.rect.x
                offset_y = self.rect.y - block.rect.y
                

                if block.mask.overlap(self.mask, (offset_x, offset_y)):
                    if self.change_y == 1:
                        self.rect.y -= 8
                    else:
                        self.rect.y -= self.change_y
                        self.change_y = 0
                    self.rect.x -= self.change_x
                    print("Overlap");

                # if block.mask.get_at((offset_x, offset_y)):
                #     # print("Collides with block ", block, offset_x, offset_y)
                #     if self.change_y == 1:
                #         self.rect.y -= 8
                #     else:
                #         self.rect.y -= self.change_y
                #         self.change_y = 0
                #     self.rect.x -= self.change_x
                # elif block.mask.get_at((offset_x, offset_y-self.height)):
                #     if self.change_y == 1:
                #         self.rect.y += 8
                #     else:
                #         self.rect.y -= self.change_y
                #         self.change_y = 0
        

        
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
            self.jumping = 0
        else:
            self.change_y += GRAVITY_VALUE

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            print("Resetting to screen height")
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        if self.jumping == 1:
            return False

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -JUMP_HEIGHT
            self.jumping = 1

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

from level import *

# Level 1
class Level_01(Level):

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = (205, 210, 218)

        self.level_limit = -9600

        # Array with width, height, x, and y of platform
        level = [
            [9600, 600, 150, 0, "level1/mask.png", "level1/base.png"]
        ]


        # Go through the array above and add platforms
        for platform in level:
            if platform[5]:
                block = MaskedBlock(platform[0], platform[1], platform[4], platform[5])
            else:
                block = Block(platform[0], platform[1])

            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
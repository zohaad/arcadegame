from level import *

# Level 1
class Level_01(Level):

    def __init__(self, player):
        Level.__init__(self, player)

        self.background = (205, 210, 218)

        self.level_limit = -1000

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]


        # Go through the array above and add platforms
        for platform in level:
            block = Block(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
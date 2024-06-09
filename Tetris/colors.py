class Colors:
    dark_grey = (64, 64, 64)
    green = (0, 128, 0)
    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)
    purple = (128, 0, 128)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]

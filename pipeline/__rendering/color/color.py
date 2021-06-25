derek_blue = (144.0 / 255, 210.0 / 255, 236.0 / 255, 1)
coral_red = (250.0 / 255, 114.0 / 255, 104.0 / 255, 1)
igl_green = (153.0 / 255, 203.0 / 255, 67.0 / 255, 1)
caltech_orange = (255.0 / 255, 108.0 / 255, 12.0 / 255, 1)
royal_blue = (0 / 255, 35 / 255, 102 / 255, 1)
royal_yellow = (250.0 / 255, 218.0 / 255, 94.0 / 255, 1)
antique_gold = (207.0 / 255, 181.0 / 255, 59.0 / 255, 1)
deco_silver = (73.0 / 255, 73.0 / 255, 73.0 / 255, 1)
white = (1, 1, 1, 1)
black = (0, 0, 0, 1)

# color palette for color blindness (source: http://mkweb.bcgsc.ca/colorblind)
cb_black = (0 / 255.0, 0 / 255.0, 236 / 255.0, 1)
cb_orange = (230 / 255.0, 159 / 255.0, 0 / 255.0, 1)
cb_skyblue = (86 / 255.0, 180 / 255.0, 233 / 255.0, 1)
cb_green = (0 / 255.0, 158 / 255.0, 115 / 255.0, 1)
cb_yellow = (240 / 255.0, 228 / 255.0, 66 / 255.0, 1)
cb_blue = (0 / 255.0, 114 / 255.0, 178 / 255.0, 1)
cb_vermillion = (213 / 255.0, 94 / 255.0, 0 / 255.0, 1)
cb_purple = (204 / 255.0, 121 / 255.0, 167 / 255.0, 1)


class Color:
    def __init__(self, rgba=derek_blue, h=0.5, s=1.0, v=1.0, b=0.0, c=0.0):
        self.h = h  # hue
        self.s = s  # saturation
        self.v = v  # value
        self.rgba = rgba  # rgba
        self.b = b  # brightness
        self.c = c  # contrast

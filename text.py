import pygame
from constants import DEFAULT_FONT
from constants import DEFAULT_FONT_SIZE
from constants import DEFAULT_TEXT_COLOR
from constants import DEFAULT_SCREEN_COLOR
class Text(pygame.sprite.Sprite):
    
    def __init__(
                self, x, y,
                string, 
                size = DEFAULT_FONT_SIZE,
                bold = False,
                italic = False,
                color = DEFAULT_TEXT_COLOR,
                background = None
                ):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
# attribute for annimation
        self.visible = True
# attributes caching for the properties defined below
        self._font = DEFAULT_FONT
        self._size = size
        self._bold = bold
        self._italic = italic
        self._string = string
        self._antialias = False
        self._color = color
        self._background = background
# attributes for the draw method of the Sprite class
        self.position = pygame.Vector2(x,y)
        self.rect = None
# flags for when properties change
        self._dirty_font = True
        self._dirty_surface = True
        self.update(0)
# font object parameters with dirty flag
    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        if value != self._font:
            self._font = value
            self._dirty_font = True
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value != self._size:
            self._size = value
            self._dirty_font = True

    @property
    def bold(self):
        return self._bold

    @bold.setter
    def bold(self, value):
        if value != self._bold:
            self._bold = value
            self._dirty_font = True

    @property
    def italic(self):
        return self._italic

    @italic.setter
    def italic(self, value):
        if value != self._italic:
            self._italic = value
            self._dirty_font = True

# surface object parameters with dirty flag
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        if value != self._string:
            self._string = value
            self._dirty_surface = True

    @property
    def antialias(self):
        return self._antialias

    @antialias.setter
    def antialias(self, value):
        if value != self._antialias:
            self._antialias = value
            self._dirty_surface = True

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value != self._color:
            self._color = value
            self._dirty_surface = True

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        if value != self._background:
            self._background = value
            self._dirty_surface = True
    #read-only properties
    @property
    def width(self):
        return self.rect.width
    @property
    def height(self):
        return self.rect.height


# update based on flags
    def update(self, dt):
        if self._dirty_font:

            self._font_object = pygame.font.SysFont(
                                self.font,
                                self.size,
                                self.bold,
                                self.italic
                                )

            self._dirty_font = False
            self._dirty_surface = True

        if self._dirty_surface:
            self.image = self._font_object.render(
                                            self.string, 
                                            self.antialias, 
                                            self.color, 
                                            self.background
                                            )

            self._dirty_surface = False

        if self.rect is None:
            self.rect = self.image.get_rect()

        self.rect.center = self.position

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)

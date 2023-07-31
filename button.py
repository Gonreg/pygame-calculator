import pygame
import operands


class Button:
    color = None
    colorHover = None
    text = None
    width = None
    height = None
    bounds = None
    x = None
    y = None

    def __init__(self, color, colorHover, text, width, height, bounds, x, y):
        self.color = color
        self.colorHover = colorHover
        self.text = text
        self.width = width
        self.height = height
        self.bounds = bounds
        self.x = x
        self.y = y

    def draw_text(self, screen):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, 45)
        text_image = font.render(self.text, True, '#FFFFFF')
        text_rect = text_image.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        screen.blit(text_image, text_rect)

    def draw(self, screen, isClicked):
        mousePos = pygame.mouse.get_pos()
        if self.x + self.width > mousePos[0] > self.x and self.y + self.height > mousePos[1] > self.y:
            color = self.colorHover
        else:
            color = self.color

        pygame.draw.rect(screen, '#FFFFFF', (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        self.draw_text(screen)
        if isClicked:
            return self.click()

    def click(self):
        mousePos = pygame.mouse.get_pos()
        if self.x + self.width > mousePos[0] > self.x \
                and self.y + self.height > mousePos[1] > self.y \
                and pygame.mouse.get_pressed()[0]:
            if operands.getTypeCommand(self.text) == 'number':
                return self.text
            elif operands.getTypeCommand(self.text) == 'operand':
                return ['operand', self.text]
            else:
                return ['method', self.text]


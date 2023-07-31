import pygame
import button

pygame.init()

bounds = (360, 640)
screen = pygame.display.set_mode(bounds)

pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

buttons = ['0', ',', '=', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', 'x', 'AC', '+/-', '%', '÷']
buttonsObjects = []

mainText = ''

operatorA = 0
operatorB = 0
operand = ''
result = 0


def draw_text(screen, bounds, text):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, 65)
    text_image = font.render(text, True, '#FFFFFF')
    text_rect = text_image.get_rect()
    text_rect.right = bounds[0] - 15
    text_rect.top = bounds[1] - 575
    screen.blit(text_image, text_rect)


i = 1
height = 90
width = 360
for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
    buttonsObjects.append(button.Button('#000000', '#696969', btn, 180 if i == 1 else 90, 90, bounds, bounds[0] - width,
                                        bounds[1] - height))
    width -= 180 if i == 1 else 90
    i += 1

run = True
while run:
    clock.tick(60)

    isClicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            isClicked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            isClicked = True

    screen.fill('#000000')
    for btn in buttonsObjects:
        text = btn.draw(screen, isClicked, mainText)
        if text and text[0] == 'operand':
            if text[1] != '=':
                operand = text[1]
                if not operatorA:
                    operatorA = mainText
                    mainText = ''
                else:
                    operatorB = mainText
                    mainText = ''
            else:
                if not operatorB:
                    operatorB = mainText
                if operand == '+':
                    mainText = str(int(operatorA) + int(operatorB))
                elif operand == '-':
                    mainText = str(int(operatorA) - int(operatorB))
                elif operand == 'x':
                    mainText = str(int(operatorA) * int(operatorB))
                elif operand == '÷':
                    mainText = str(int(operatorA) / int(operatorB))
                elif operand == '%':
                    mainText = str(int(operatorA) / 100)
                operand = '='
        elif text and text[0] == 'method':
            if text[1] == 'AC':
                mainText = ''
                operatorA = 0
                operatorB = 0
                operand = ''
                result = 0
            elif text[1] == '+/-':
                if len(mainText) != 0:
                    if mainText[0] != '-':
                        mainText = '-' + mainText
                    else:
                        mainText = mainText.replace('-', '')
                else:
                    mainText = '-'
            elif text[1] == ',':
                print(',')
        elif text:
            if operand == '=':
                mainText = ''
                operatorA = 0
                operatorB = 0
                operand = ''
                result = 0
            mainText += text

    draw_text(screen, bounds, mainText)

    pygame.display.flip()

pygame.quit()

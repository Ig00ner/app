import pygame
import random

pygame.init()

# Задаем константы - размеры окна, цвет окна
#WIGHT = 500
HIGHT = 600
FRAME_COLOR = (0, 255, 204) # цвет окна
RECT_COLOR = (255, 255, 255) #цвет квадрата
OTHER_RECT_COLOR = (204, 255, 255)
SIZE_RECT = 20 # размер квадрата
COUNT_RECTS = 20 # количество квадратов в каждом ряду
RETURN = 1
WIGHT = SIZE_RECT * COUNT_RECTS + 2 * SIZE_RECT + RETURN * SIZE_RECT
HEADER_RECT = 70
HEADER_COLOR = (0, 230, 204)
COLOR_SNAKE = (0, 102, 0)
FOOD_COLOR = (255, 0, 0)

# иницианализируем звуковой модуль
pygame.mixer.init()

# загружаем музыку
#pygame.mixer.music.load("1.mp3")

#Рисуем окно
app = pygame.display.set_mode((WIGHT, HIGHT))

# Заголовок программы
pygame.display.set_caption('Hangry Snake')

# для того, тобы окно не закрывалось, создаем игровой цикл
game_over = False
is_game_started = False

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inside (self):
        return 0 <= self.x < COUNT_RECTS and 0 <= self.y < COUNT_RECTS
    
    def __eq__(self, other):
        return isinstance(other, Snake) and self.x == other.x and self.y == other.y


def draw_rect(color,row, column):
    pygame.draw.rect(app, color, [SIZE_RECT+column*SIZE_RECT+RETURN*(column+1), 
                                             HEADER_RECT+SIZE_RECT+row*SIZE_RECT+RETURN*(row+1), SIZE_RECT, SIZE_RECT])


def random_food_block():
    x = random.randint(0, COUNT_RECTS - 1)
    y = random.randint(0, COUNT_RECTS - 1)

    food_block = Snake(x, y)

    while food_block in snake_rect:
        food_block.x = random.randint(0, COUNT_RECTS - 1)
        food_block.y = random.randint(0, COUNT_RECTS - 1)

    return food_block

def end_game():
    is_game_started = False
    game_over = True

    font_gamover = pygame.font.SysFont('monaco',72)
    text_gamover = font_gamover.render('GAME OVER :(', True, (255, 0, 0))
    app.blit(text_gamover, (60, HIGHT // 2))
    text_totalscore = font_gamover.render(f'Score: {result}', True, (255, 0, 255))
    app.blit(text_totalscore, (120, HIGHT // 2 + 50))
    game_over = True
    pygame.display.flip()
    if event.type == pygame.QUIT:
        pygame.quit()


snake_rect = [Snake(9, 9)]
food = random_food_block()
x_row = 0
y_col = 1
result = 0

time = pygame.time.Clock()
text = pygame.font.SysFont('monaco', 36)

# проигрывание музыки
#pygame.mixer.music.play(-1)

while not game_over:
    #обрабатываем событие - закрытие окна, нажатие на крестик (Х)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True    
        elif event.type == pygame.KEYDOWN:
            if not is_game_started:
                is_game_started = True
            elif event.key == pygame.K_UP and y_col !=0:
                x_row = -1
                y_col = 0
            elif event.key == pygame.K_DOWN and y_col !=0:
                x_row = 1
                y_col = 0
            elif event.key == pygame.K_RIGHT and x_row !=0:
                x_row = 0
                y_col = 1
            elif event.key == pygame.K_LEFT and x_row !=0:
                x_row = 0
                y_col = -1

    app.fill (FRAME_COLOR)

    if not is_game_started:
        text_menu = text.render('For start press any key', 4, RECT_COLOR)
        app.blit(text_menu, (100, HIGHT // 2))
    else:
        pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIGHT, HEADER_RECT])

        for row in range(COUNT_RECTS):
            for column in range(COUNT_RECTS):
                if (row + column) % 2 ==0:
                    color = RECT_COLOR              
                else:
                    color = OTHER_RECT_COLOR

                draw_rect(color, row, column)        

        draw_rect(FOOD_COLOR, food.x, food.y)    

        for rect in snake_rect:
            draw_rect(COLOR_SNAKE, rect.x, rect.y)   
    
        head = snake_rect[-1]

        if food == head:
            result += 1
            snake_rect.append(food)
            food = random_food_block()

        if not head.inside():
            end_game()

        new_head = Snake(head.x + x_row, head.y + y_col)
        snake_rect.append(new_head)
        snake_rect.pop(0)

        text_result = text.render(f'Очки: {result}', True, (255,255,255))
        app.blit(text_result, (SIZE_RECT, SIZE_RECT))
    
    pygame.display.update()
    time.tick(5)

# прекращаем проигрывание музыки, освобождаем ресурсы
pygame.mixer.music.stop()
pygame.mixer.music.unload()    
pygame.quit()

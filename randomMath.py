from cProfile import run
from imghdr import tests
import random
import pygame
from sys import exit
pygame.font.init()
pygame.init()


width, height = 1000, 500
display = pygame.display.set_mode((width, height))
user_text = ''
user_answer = 0
correct = False
incorrect = False
operations = ['+', '*']
timer = pygame.USEREVENT + 1

correct_answers = 0

class Font:
    def __init__(self, name, color, size, message, location) -> None:
        self.name = name
        self.color = color
        self.size = size
        self.message = message
        self.location = location
    def render(self):
        self.font = pygame.font.SysFont(self.name, self.size)
        self.render_name = self.font.render(self.message, True, self.color)
        display.blit(self.render_name, self.location)



class Test:
    def __init__(self,random_number, random_number_2, random_number_3, answers):
        self.random_number = random_number
        self.random_number_2 = random_number_2
        self.answers = answers
        self.random_number_3 = random_number_3

run = True
clock = pygame.time.Clock()
random_numberv, random_number_2v, random_number_3v = random.randint(1, 20), random.randint(1, 20), operations[random.randint(0, 1)]
test = Test(random_numberv, random_number_2v, random_number_3v, user_text) 


active = True



while run:
    if test.random_number_3 == '+':
        answer = test.random_number + test.random_number_2
        f2 = Font(None, (255, 255, 255), 32, f'{test.random_number} + {test.random_number_2} = ', (width//2 - 72, height//2))
    elif test.random_number_3 == '*':
        answer = test.random_number * test.random_number_2
        f2 = Font(None, (255, 255, 255), 32, f'{test.random_number} * {test.random_number_2} = ', (width//2 - 72, height//2))
    f3 = Font(None, (255, 255, 255), 32, 'Correct!', (200, 250))
    f4 = Font(None, (255, 255, 255), 32, 'Incorrect!', (200, 250))   
    f5 = Font(None, (255, 255, 255), 20, f'Correct answers: {correct_answers}', (800, 480)) 
    print(test.random_number_3)
    print(answer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                elif event.key == pygame.K_KP_ENTER:
                    for i in user_text:
                        if i.isdigit():
                            pass
                        else:
                            user_text = user_text[0:-1]
                    user_answer += int(user_text)
                    pygame.time.set_timer(timer, 2000)
                    if user_answer == answer:
                        correct = True
                        correct_answers += 1
                        active = False
                    else:
                        incorrect = True
                        active = False

                else:
                    user_text += event.unicode
            else:
                if event.key == pygame.K_SPACE:
                    active = True
                    correct = False
                    incorrect = False

        if event.type == timer and active is not True:
            active = True

    if active:
        display.fill((0, 0, 0))
        correct = False
        incorrect = False
        f1 = Font(None, (255, 255, 255), 32, user_text, (width//2 + 32, height//2))
        f1.render()
        f2.render()
        f5.render()
    else:
        display.fill((0, 0, 0))
        user_text = ''
        user_answer = 0
        test.random_number = random.randint(1, 20)
        test.random_number_2 = random.randint(1, 20)
        test.random_number_3 = operations[random.randint(0, 1)]

        if correct:
            f3.render()
        if incorrect:
            f4.render()
    pygame.display.flip()
    clock.tick(60)







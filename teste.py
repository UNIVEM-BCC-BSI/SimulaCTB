import pygame
import sys
import random as randint

pygame.init()
BLACK = (0, 0, 0)
YELLOW = (255, 255, 55)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_caption("SimulaCTB")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu():
    while True:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        title_font = pygame.font.Font(None, 60)
        draw_text("SimulaCTB", title_font, YELLOW, screen, SCREEN_WIDTH // 2, 100)

        option_font = pygame.font.Font(None, 40)
        draw_text("Iniciar Jogo", option_font, YELLOW, screen, SCREEN_WIDTH // 2, 270)
        draw_text("Configurações", option_font, YELLOW, screen, SCREEN_WIDTH // 2, 320)
        draw_text("Sair", option_font, YELLOW, screen, SCREEN_WIDTH // 2, 370)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 250 <= mouse_pos[1] <= 275:
                    print("Iniciar Jogo")

                def main():
                    question_index = 0
                    questions = ["Quem é o mais pika do Grupo?", "Tem Certeza?", "Quanto é 2 + 2?"]
                    answers = [["Matheus", "Matheus", "Matheus"], ["Sim", "Óbvio", "Com certeza"],
                               ["3", "4", "5"]]
                    selected_answer = 0

                    running = True
                    while running:
                        screen.fill(WHITE)
                        current_question = questions[question_index]
                        draw_text(current_question, font, BLACK, screen, 170, 60)

                        for i, answer in enumerate(answers[question_index]):
                            color = BLACK if i == selected_answer else GRAY
                            draw_text(answer, font, color, screen, 100, 150 + i * 50)

                        pygame.display.flip()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    if question_index < len(answers):
                                        correct_answer = answers[question_index][
                                            0]
                                        selected_answer_text = answers[question_index][selected_answer]
                                        if selected_answer_text == correct_answer:
                                            print("Resposta correta!")
                                            question_index += 1
                                            selected_answer = 0
                                        else:
                                            print("Resposta incorreta!")
                                    else:
                                        print("Fim do jogo!")
                                        running = False
                                elif event.key == pygame.K_UP:
                                    selected_answer = (selected_answer - 1) % len(answers[question_index])
                                elif event.key == pygame.K_DOWN:
                                    selected_answer = (selected_answer + 1) % len(answers[question_index])
                if __name__ == "__main__":
                    main()
                elif 300 <= mouse_pos[1] <= 325:
                    print("Configurações")
                elif 350 <= mouse_pos[1] <= 375:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main_menu()
import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
        screen.fill(WHITE)

        title_font = pygame.font.Font(None, 60)
        draw_text("SimulaCTB", title_font, BLACK, screen, SCREEN_WIDTH // 2, 100)

        option_font = pygame.font.Font(None, 40)
        draw_text("Iniciar Jogo", option_font, BLACK, screen, SCREEN_WIDTH // 2, 250)
        draw_text("Configurações", option_font, BLACK, screen, SCREEN_WIDTH // 2, 300)
        draw_text("Sair", option_font, BLACK, screen, SCREEN_WIDTH // 2, 350)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 250 <= mouse_pos[1] <= 275:
                    print("Iniciar Jogo")
                elif 300 <= mouse_pos[1] <= 325:
                    print("Configurações")
                elif 350 <= mouse_pos[1] <= 375:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()

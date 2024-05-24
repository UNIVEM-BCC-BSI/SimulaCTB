import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 55)
T_BLACK = (0, 0, 0, 28)

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SimulaCTB")

background_image = pygame.transform.scale(pygame.image.load("C:/Users/mathe/Downloads/cenario.jpg"), (WIDTH, HEIGHT)).convert()  # Redimensionar a imagem do cenário
car_image = pygame.transform.scale(pygame.image.load("C:/Users/mathe/Downloads/carro.png"), (160, 140))  # Ajuste do tamanho do carro
car_rect = car_image.get_rect()
car_rect.center = (100, 545)

car_speed = 5
background_scroll_speed = 2

questions = [
    {"question": "A atual legislação de trânsito intitula-se:", "answer": "C) Código de Trânsito Brasileiro.", "alternatives": ["A) Código Nacional de Trânsito.", "B) Código de Trânsito.", "C) Código de Trânsito Brasileiro.", "D) Código Brasileiro de Trânsito."]},
    {"question": "O Licenciamento Anual do Veículo vincula-se ao:", "answer": "C) Pagamento de IPVA, Seguro Obrigatório e ausência de multas de trânsito.", "alternatives": ["A) Pagamento de exames de avaliação psicológica e aptidão física.", "B) Pagamento do seguro total e DPVAT.", "C) Pagamento de IPVA, Seguro Obrigatório e ausência de multas de trânsito.", "D) Pagamento de IPVA e Seguro Obrigatório."]},
    {"question": "O ciclomotor é veículo classificado como:", "answer": "B) Tração.", "alternatives": ["A) Misto.", "B) Tração.", "C) Especial.", "D) Passageiros."]},
    {"question": "São dispensados da placa dianteira, os veículos de:", "answer": "C) Duas ou três rodas.", "alternatives": ["A) Quatro rodas.", "B) Mais de quatro rodas.", "C) Duas ou três rodas.", "D) Todos os veículos são obrigados a ter placa dianteira."]},
    {"question": "Ao registrar o veículo automotor, o órgão executivo de trânsito expedirá o documento:", "answer": "C) Certificado de Registro de Veículo.", "alternatives": ["A) Certificado.", "B) Certificado de Segurança Veicular.", "C) Certificado de Registro de Veículo.", "D) Certificado de Registro e Licenciamento de Veículo."]},
    {"question": "Constitui documento de porte obrigatório:", "answer": "A) Certificado de Registro de Veículo.", "alternatives": ["A) Certificado de Registro de Veículo.", "B) Autorização, Permissão para Dirigir ou Carteira Nacional de Habilitação.", "C) Comprovante do pagamento do Seguro Obrigatório.", "D) Comprovante do pagamento atualizado do IPVA."]},
    {"question": "A expedição de novo Certificado de Registro de Veículo, dar-se-á quando:", "answer": "A) Houver transferência de propriedade.", "alternatives": ["A) Houver transferência de propriedade.", "B) Houver mudanças nos equipamentos obrigatórios.", "C) De doze em doze meses.", "D) Após o pagamento do IPVA."]},
    {"question": "No caso de transferência de propriedade, o prazo para o proprietário adotar as providências necessárias à efetivação da expedição de novo Certificado de Registro de Veículo é de:", "answer": "C) 30 dias.", "alternatives": ["A) 15 dias.", "B) De imediato.", "C) 30 dias.", "D) A qualquer tempo."]},
    {"question": "A expedição de novo Certificado de Registro de Veículo é obrigatória quando:", "answer": "B) Houver mudança de categoria.", "alternatives": ["A) O proprietário mudar de endereço no mesmo Município.", "B) Houver mudança de categoria.", "C) O veículo circular acoplado a semirreboque.", "D) O veículo for importado por membro de missão diplomática."]},
    {"question": "O proprietário de veículo irrecuperável ou definitivamente desmontado deverá requerer a baixa do registro, sendo vedada à remontagem do veículo sobre o mesmo ______________, de forma a manter o registro anterior.", "answer": "A) Chassi.", "alternatives": ["A) Chassi.", "B) Agregados.", "C) Monobloco.", "D) Número de Registro."]}
]

current_question_index = 0
selected_alternative_index = 0

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

def display_question():
    question_text = font.render(questions[current_question_index]["question"], True, (0, 0, 0))
    question_rect = question_text.get_rect(center=(WIDTH // 2, 50))
    window.blit(question_text, question_rect)

    alternatives = questions[current_question_index]["alternatives"]
    for i, alt in enumerate(alternatives):
        alt_text = small_font.render(alt, True, (0, 0, 0))
        alt_rect = alt_text.get_rect(center=(WIDTH // 2, 150 + i * 50))
        window.blit(alt_text, alt_rect)

        if i == selected_alternative_index:
            pygame.draw.rect(window, (0, 0, 0), (alt_rect.x - 10, alt_rect.y - 5, alt_rect.width + 20, alt_rect.height + 10), 2)

def display_menu():
    while True:
        window.fill(BLACK)

        title_font = pygame.font.Font(None, 60)
        draw_text("SimulaCTB", title_font, (255, 255, 55), window, WIDTH // 2, 100)

        option_font = pygame.font.Font(None, 40)
        draw_text("Iniciar Jogo", option_font, (255, 255, 55), window, WIDTH // 2, 270)
        draw_text("Configurações", option_font, (255, 255, 55), window, WIDTH // 2, 320)
        draw_text("Sair", option_font, (255, 255, 55), window, WIDTH // 2, 370)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 250 <= mouse_pos[1] <= 275:
                    print("Iniciar Jogo")
                    main()  # Chamar a função main quando o jogo for iniciado
                elif 300 <= mouse_pos[1] <= 325:
                    print("Configurações")
                elif 350 <= mouse_pos[1] <= 375:
                    pygame.quit()
                    sys.exit()

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def display_question():
    pygame.draw.rect(window, T_BLACK, (80, 40, 650, 250))  # Ajuste as coordenadas e o tamanho conforme necessário

    question_text = font.render(questions[current_question_index]["question"], True, YELLOW)
    question_rect = question_text.get_rect(center=(WIDTH // 2, 100))
    window.blit(question_text, question_rect)

    alternatives = questions[current_question_index]["alternatives"]
    for i, alt in enumerate(alternatives):
        alt_text = small_font.render(alt, True, YELLOW)
        alt_rect = alt_text.get_rect(center=(WIDTH // 2, 160 + i * 25))
        window.blit(alt_text, alt_rect)

        if i == selected_alternative_index:
            pygame.draw.rect(window, YELLOW, (alt_rect.x - 10, alt_rect.y - 5, alt_rect.width + 20, alt_rect.height + 10), 2)

def main():
    global current_question_index
    global selected_alternative_index

    running = True
    clock = pygame.time.Clock()

    background_images = [background_image.copy() for _ in range(3)]
    total_background_width = background_image.get_width() * len(background_images)

    background_scroll = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_alternative_index = (selected_alternative_index + 1) % len(questions[current_question_index]["alternatives"])
                elif event.key == pygame.K_UP:
                    selected_alternative_index = (selected_alternative_index - 1) % len(questions[current_question_index]["alternatives"])
                elif event.key == pygame.K_RETURN:
                    selected_alternative = questions[current_question_index]["alternatives"][selected_alternative_index]
                    if selected_alternative == questions[current_question_index]["answer"]:
                        current_question_index += 1
                        car_rect.y = 475
                        background_scroll -= 100
                        if background_scroll <= -total_background_width + WIDTH:
                            background_scroll = 0

        window.fill(WHITE)
        for i, bg_image in enumerate(background_images):
            window.blit(bg_image, (background_scroll + i * background_image.get_width(), 0))  # Desenhar o cenário
        display_question()
        window.blit(car_image, car_rect)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    display_menu()

import pygame
import sys

# 1. Inicialização
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
# 2. Configurações da Janela
LARGURA = 800
ALTURA = 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Planilha de Treino - Tech Theme")

# 4. Carregamento do Som
try:
    
    som_clique = pygame.mixer.Sound("clique.wav2.mp3")
    som_clique.set_volume(1.0)
except Exception as e:
    print(f"Aviso: Arquivo de som não encontrado, continuando sem áudio. ({e})")
    som_clique = None

# 3. Carregamento de Imagem
try:
    
    fundo_original = pygame.image.load("image_9de040.jpg").convert()
    fundo = pygame.transform.scale(fundo_original, (LARGURA, ALTURA))

    
    # tom da imagem de referência
    overlay = pygame.Surface((LARGURA, ALTURA))
    overlay.set_alpha(200) 
    overlay.fill((5, 5, 10))
except Exception as e:
    print(f"Erro ao carregar imagem: {e}")
    fundo = None


ROSA_TECH = (235, 20, 76)  
FUNDO_CARD = (15, 15, 20, 210) 
COR_BRANCO = (255, 255, 255)
COR_CINZA = (170, 170, 170) 
COR_TEXTO_BOTAO = (10, 10, 10) 

fonte_titulo = pygame.font.SysFont("arial", 36, bold=True)
fonte_dia = pygame.font.SysFont("arial", 22, bold=True)
fonte_exercicio = pygame.font.SysFont("arial", 18)
fonte_legenda = pygame.font.SysFont("arial", 14, italic=True)

# 5. Dados dos Treinos
planilha_detalhada = {
    "SEGUNDA: PEITO": [
        ("Supino Reto", "4x10", "60s"),
        ("Supino Inclinado", "3x12", "60s"),
        ("Crucifixo Máquina", "3x15", "45s"),
        ("Cross Over", "4x12", "45s"),
        ("Flexão de Braços", "3xFalha", "60s")
    ],
    "TERÇA: COSTAS": [
        ("Puxada Pulley", "4x12", "60s"),
        ("Remada Curvada", "4x10", "60s"),
        ("Remada Baixa", "3x12", "45s"),
        ("Pull Down", "3x15", "45s"),
        ("Levantamento Terra", "3x8", "90s")
    ],
    "QUARTA: CARDIO": [
        ("Corrida Moderada", "20 min", "---"),
        ("Polichinelos", "4x50", "30s"),
        ("Corda", "5x2 min", "45s"),
        ("Burpees", "3x15", "60s"),
        ("Caminhada Rápida", "15 min", "---")
    ],
    "QUINTA: PERNA": [
        ("Agachamento Livre", "4x10", "90s"),
        ("Leg Press 45", "4x12", "60s"),
        ("Extensora", "3x15", "45s"),
        ("Flexora", "3x15", "45s"),
        ("Panturrilha em Pé", "4x20", "45s")
    ],
    "SEXTA: OMBRO": [
        ("Desenvolvimento", "4x10", "60s"),
        ("Elevação Lateral", "4x12", "45s"),
        ("Elevação Frontal", "3x12", "45s"),
        ("Crucifixo Inverso", "3x15", "45s"),
        ("Encolhimento", "4x15", "60s")
    ]
}

estado = "menu"
botao_jogar = pygame.Rect(300, 320, 200, 50)
botao_config = pygame.Rect(300, 320, 200, 50)
botao_voltar = pygame.Rect(300, 630, 200, 45)

clock = pygame.time.Clock()

def desenhar_fundo():
    if fundo:
        tela.blit(fundo, (0, 0))
        tela.blit(overlay, (0, 0))
    else:
        tela.fill((10, 10, 15))

while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado == "menu" and botao_jogar.collidepoint(mouse_pos):
                if som_clique: som_clique.play()
                estado = "jogo"
            elif estado == "jogo" and botao_config.collidepoint(mouse_pos):
                if som_clique: som_clique.play()
                estado = "opcoes"
            elif estado == "opcoes" and botao_voltar.collidepoint(mouse_pos):
                if som_clique: som_clique.play()
                estado = "jogo"

    desenhar_fundo()

    if estado == "menu":
        # Título  
        txt1 = fonte_titulo.render("APP DE TREINO", True, COR_BRANCO)
        txt2 = fonte_titulo.render("TECH", True, ROSA_TECH)
        tela.blit(txt1, txt1.get_rect(center=(400, 100)))
        tela.blit(txt2, txt2.get_rect(center=(400, 150)))
        
        # Botão 
        pygame.draw.rect(tela, ROSA_TECH, botao_jogar) # bordas arredondadas para ficar mais "tech"
        btn_txt = fonte_dia.render("JOGAR", True, COR_TEXTO_BOTAO) 
        tela.blit(btn_txt, btn_txt.get_rect(center=botao_jogar.center))

    elif estado == "jogo":
        txt = fonte_titulo.render("ÁREA DO ALUNO", True, COR_BRANCO)
        tela.blit(txt, txt.get_rect(center=(400, 250)))
        
        # Botão secundário mais discreto (como os links secundários da imagem)
        pygame.draw.rect(tela, (30, 30, 35), botao_config)
        pygame.draw.rect(tela, ROSA_TECH, botao_config, 2) # Borda rosa
        btn_txt = fonte_dia.render("VER PLANILHA", True, COR_BRANCO)
        tela.blit(btn_txt, btn_txt.get_rect(center=botao_config.center))

    elif estado == "opcoes":
        titulo1 = fonte_titulo.render("PLANILHA", True, COR_BRANCO)
        titulo2 = fonte_titulo.render("SEMANAL", True, ROSA_TECH)
        tela.blit(titulo1, (LARGURA//2 - (titulo1.get_width() + titulo2.get_width() + 10)//2, 20))
        tela.blit(titulo2, (LARGURA//2 - (titulo1.get_width() + titulo2.get_width() + 10)//2 + titulo1.get_width() + 10, 20))

        x_pos = [50, 420]
        y_inicial = 80
        
        for i, (dia, lista_ex) in enumerate(planilha_detalhada.items()):
            col = i % 2
            lin = i // 2
            curr_x = x_pos[col]
            curr_y = y_inicial + (lin * 180)

            # Card de treino
            s = pygame.Surface((350, 165), pygame.SRCALPHA)
            pygame.draw.rect(s, FUNDO_CARD, (0, 0, 350, 165)) 
            
            # Linha decorativa rosa no card 
            pygame.draw.line(s, ROSA_TECH, (0, 0), (0, 165), 4)
            tela.blit(s, (curr_x - 5, curr_y - 5))

            # Nome da semana em Rosa
            txt_dia = fonte_dia.render(dia, True, ROSA_TECH)
            tela.blit(txt_dia, (curr_x + 10, curr_y))
            
            header = fonte_legenda.render("Exercício                 |  Séries  | Desc.", True, COR_CINZA)
            tela.blit(header, (curr_x + 10, curr_y + 30))

            for idx, ex in enumerate(lista_ex):
                linha_y = curr_y + 50 + (idx * 21)
                nome = ex[0][:18] 
                tela.blit(fonte_exercicio.render(nome, True, COR_BRANCO), (curr_x + 10, linha_y))
                tela.blit(fonte_exercicio.render(ex[1], True, COR_BRANCO), (curr_x + 200, linha_y))
                tela.blit(fonte_exercicio.render(ex[2], True, COR_BRANCO), (curr_x + 285, linha_y))

        # Botão Voltar (Rosa Sólido)
        pygame.draw.rect(tela, ROSA_TECH, botao_voltar)
        tela.blit(fonte_dia.render("VOLTAR", True, COR_TEXTO_BOTAO), fonte_dia.render("VOLTAR", True, COR_TEXTO_BOTAO).get_rect(center=botao_voltar.center))

    pygame.display.flip()
    clock.tick(60)
import arcade
import random

CORES = [
    (  7,  7,  7), ( 31,  7,  7), ( 47, 15,  7), ( 71, 15,  7), ( 87, 23,  7), (103, 31,  7), (119, 31,  7), (143, 39,  7),
    (159, 47,  7), (175, 63,  7), (191, 71,  7), (199, 71,  7), (223, 79,  7), (223, 87,  7), (223, 87,  7), (215, 95,  7),
    (215, 95,  7), (215,103, 15), (207,111, 15), (207,119, 15), (207,127, 15), (207,135, 23), (199,135, 23), (199,143, 23),
    (199,151, 31), (191,159, 31), (191,159, 31), (191,167, 39), (191,167, 39), (191,175, 47), (183,175, 47), (183,183, 47),
    (183,183, 55), (207,207,111), (223,223,159), (239,239,199), (255,255,255)
]

LARGURA = 1200
ALTURA = 800
TITULO = "DOOM FIRE"

LARGURA_BLOCO = 5
ALTURA_BLOCO = 5 
TOTAL_BLOCOS_LINHA = 30
TOTAL_BLOCOS_COLUNA = 240
TOTAL_BLOCOS = TOTAL_BLOCOS_LINHA * TOTAL_BLOCOS_COLUNA
mapa = [0] * TOTAL_BLOCOS

def criar_origem_fogo():
    for i in range(0, TOTAL_BLOCOS_COLUNA):
        mapa[i] = 36

def desenhar():
    criar_origem_fogo()
    for linha in range(0, TOTAL_BLOCOS_LINHA):
        for coluna in range(0, TOTAL_BLOCOS_COLUNA):
            indice = linha * TOTAL_BLOCOS_COLUNA + coluna
            arcade.draw_rectangle_filled(                
                coluna * LARGURA_BLOCO, 
                linha * ALTURA_BLOCO, 
                LARGURA_BLOCO,
                ALTURA_BLOCO,
                CORES[mapa[indice]]
            )                        
            # texto = str(mapa[indice])
            # arcade.draw_text(
            #     texto,
            #     coluna * LARGURA_BLOCO,
            #     linha * ALTURA_BLOCO,
            #     arcade.color.WHITE,
            #     7                
            # )

def atualizar():
    for linha in range(1, TOTAL_BLOCOS_LINHA):
        for coluna in range(0, TOTAL_BLOCOS_COLUNA):            
            indice = linha * TOTAL_BLOCOS_COLUNA + coluna
            indice_anterior = (linha - 1) * TOTAL_BLOCOS_COLUNA + (coluna + random.randint(-1, 1))
            mapa[indice] = mapa[indice_anterior] - random.randint(1, 3)
            if mapa[indice] < 0:
                mapa[indice] = 0






















class DoomFire(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_update_rate(1/20)

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        self.clear()
        desenhar()

    def on_update(self, delta_time):
        atualizar()

def main():
    """ Main function """
    game = DoomFire(LARGURA, ALTURA, TITULO)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

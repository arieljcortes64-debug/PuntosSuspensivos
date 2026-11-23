choise = input("<Jugar | Salir>: ").strip().capitalize()

while choise != "Salir" and choise != "Jugar":
    choise = (
        input("Input incorrecta, intentelo de nuevo\n<Jugar | Salir>: ")
        .strip()
        .capitalize()
    )

while choise != "Salir":
    player1_ID = 0
    player1_Lifes = 3
    player1_Pos = (0, 0)
    player1_Shoot = True
    player2_ID = 0
    player2_Lifes = 3
    player2_Pos = (0, 0)
    player2_Shoot = True
    print("Batalla de Tanques Inicia!")

    while player1_Lifes > 0 and player2_Lifes > 0:
        player1_Shoot = (
            input("El player 1 dispara, ¿Este impacto con el jugador 2? \n <Si | No>: ")
            .strip()
            .capitalize()
        )

        while player1_Shoot != "Si" and player1_Shoot != "No":
            player1_Shoot = (
                input(
                    "Entrada incorrecta!\nEl player 1 dispara, ¿Este impacto con el jugador 2? \n <Si | No>: "
                )
                .strip()
                .capitalize()
            )

        if player1_Shoot == "Si":
            player2_Lifes -= 1

        player2_Shoot = (
            input("El player 2 dispara, ¿Este impacto con el jguador 1? \n <Si | No>: ")
            .strip()
            .capitalize()
        )

        while player2_Shoot != "Si" and player2_Shoot != "No":
            player2_Shoot = (
                input(
                    "Entrada incorrecta!\nEl player 2 dispara, ¿Este impacto con el jguador 1? \n <Si | No>: "
                )
                .strip()
                .capitalize()
            )

        if player2_Shoot == "Si":
            player1_Lifes -= 1

        print(
            f"El jugador 1 tiene: {player1_Lifes} vidas! | El jugador 2 tiene: {player2_Lifes} vidas!"
        )

    if player2_Lifes == 0:
        print("El player 1 gana!")
    else:
        print("El player 2 gana!")

    print("Fin del juego")
    choise = input("<Jugar | Salir>: ").strip().capitalize()

    while choise != "Salir" and choise != "Jugar":
        choise = (
            input("Input incorrecta, intentelo de nuevo\n<Jugar | Salir>: ")
            .strip()
            .capitalize()
        )

print("Fin del juego")


# import pygame
# import sys

# pygame.init()
# screen = pygame.display.set_mode((800, 400))
# pygame.display.set_caption("Mi primer videojuego")
# clock = pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     pygame.display.update()
#     clock.tick(60)

choise = input("<Jugar | Salir>: ").strip().capitalize()

while choise != "Salir" and choise != "Jugar":
    choise = (
        input("Input incorrecta, intentelo de nuevo\n<Jugar | Salir>: ")
        .strip()
        .capitalize()
    )

while choise != "Salir":
    player1_Lifes = 3
    player1_Shoot = True
    player2_Lifes = 3
    player2_Shoot = True

    player1_Input = (
        input("Acción del jugador 1: <W, A, S, D, E, Q, ESQ, ClickIzq>: ")
        .strip()
        .upper()
    )
    while (
        player1_Input != "W"
        and player1_Input != "A"
        and player1_Input != "S"
        and player1_Input != "D"
        and player1_Input != "E"
        and player1_Input != "Q"
        and player1_Input != "CLICKIZQ"
        and player1_Input != "ESQ"
    ):
        player1_Input = (
            input(
                "Input incorrecta, intentelo de nuevo\nAcción del jugador 1: <W, A, S, D, E, Q, ESQ, ClickIzq>: "
            )
            .strip()
            .upper()
        )

    player2_Input = (
        input("Acción del jugador 2: <W, A, S, D, E, Q, ESQ, ClickIzq>: ")
        .strip()
        .upper()
    )
    while (
        player2_Input != "W"
        and player2_Input != "A"
        and player2_Input != "S"
        and player2_Input != "D"
        and player2_Input != "E"
        and player2_Input != "Q"
        and player2_Input != "CLICKIZQ"
        and player2_Input != "ESQ"
    ):
        player2_Input = (
            input(
                "Input incorrecta, intentelo de nuevo\nAcción del jugador 2: <W, A, S, D, E, Q, ESQ, ClickIzq>: "
            )
            .strip()
            .upper()
        )

    pos_valida = False
    while not pos_valida:
        x_txt = input("Inserte la posición en X del player 1 (1-9): ").strip()
        y_txt = input("Inserte la posición en Y del player 1 (1-9): ").strip()

        if not (x_txt.isdigit() and y_txt.isdigit()):
            print("Error: ingrese solo números enteros.")
            continue

        player1_posx = int(x_txt)
        player1_posy = int(y_txt)

        if 0 < player1_posx < 10 and 0 < player1_posy < 10:
            pos_valida = True
        else:
            print(
                "No puedes salirte de los límites del juego!\nIntente de nuevo con valores entre 1 y 9."
            )

    pos_valida = False
    while not pos_valida:
        x_txt = input("Inserte la posición en X del player 2 (1-9): ").strip()
        y_txt = input("Inserte la posición en Y del player 2 (1-9): ").strip()

        if not (x_txt.isdigit() and y_txt.isdigit()):
            print("Error: ingrese solo números enteros.")
            continue

        player2_posx = int(x_txt)
        player2_posy = int(y_txt)

        if 0 < player2_posx < 10 and 0 < player2_posy < 10:
            pos_valida = True
        else:
            print(
                "No puedes salirte de los límites del juego!\nIntente de nuevo con valores entre 1 y 9."
            )

    print("Batalla de Tanques Inicia!")

    while player1_Lifes > 0 and player2_Lifes > 0:
        while True:
            player1_LifesTxt = input(
                "Inserte la cantidad de vidas del jugador 1: "
            ).strip()
            if not player1_LifesTxt.isdigit():
                print("Error: ingrese solo números enteros.")
                continue
            player1_Lifes = int(player1_LifesTxt)
            if 0 <= player1_Lifes <= 3:
                break
            else:
                print(
                    "Cantidad inválida de vidas!\nIntente de nuevo con valores entre 3 y 0"
                )
        while True:
            player2_LifesTxt = input(
                "Inserte la cantidad de vidas del jugador 2: "
            ).strip()
            if not player2_LifesTxt.isdigit():
                print("Error: ingrese solo números enteros.")
                continue
            player2_Lifes = int(player2_LifesTxt)
            if 0 <= player2_Lifes <= 3:
                break
            else:
                print(
                    "Cantidad inválida de vidas!\nIntente de nuevo con valores entre 3 y 0"
                )
        if player1_Lifes > 0 and player2_Lifes > 0:
            print("El juego continua!")

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

# Puntos Suspensivos

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo [B]

Juego de batalla de tanques para dos jugadores con modo local y, más adelante, modo multijugador cliente-servidor en red LAN.

## Integrantes

- Ariel Cortés
- Gregory Trávez
- Victor Carabajo

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta del repositorio:

```
python juego.py          (menú)
python game_logic.py     (validación de la jugada y fin de la partida)
```

## Estructura del repositorio

| Archivo | Qué hace | Estado |
|---|---|---|
| `juego.py` | [Menú que se repite hasta «Salir» (parte de DF1)] | [Terminado / Iniciado] |
| `game_logic.py` | [Validación de la jugada (DF2) y fin de la partida (DF3)] | [Terminado / Iniciado] |
| `server.py` | [Comentario con lo que hará el servidor (Jugador 1)] | [Pendiente] |
| `client.py` | [Comentario con lo que hará el cliente (Jugador 2)] | [Pendiente] |
| `diseno/` | Diagramas `.rap` de la Fase 2 | [Subido] |

## Del diseño al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
|---|---|---|
| DF1 Partida completa (solo el menú y bucle del juego) | `juego.py`, líneas: 0 - 78 | Se modificaron varios problemas lógicos que se tenían en el diagrama original. Se invirtieron los condicionales del Loop en Raptor que determinaba si la partida empezaba o terminaba, se cambio el "or" por un "and". Se agrego la validación de la entrada del jugador al decidir si el disparo impacto o no, de esta forma, el programa solo continua si se eligue por un "Si" o un "No", caso contrario, se le pedirá al jugador elegir de nuevo. Se añadió un mensaje de cuantas vidas tiene cada jugador despues de cada turno. |
| DF2 Validación de la jugada | `game_logic.py`, líneas: 0 - 100 | Se modifico el orden de la validación de la jugada, primero se validó la entrada del jugador, luego la posición que se le asignaba a este y finalmente la cantidad de vidas. Se Separo la validación de la entrada de cada jugador, así se revisaba que el input del jugador 1 este dentro de las opción y lo mismo con el 2do jugador. Así, el juego no continuará hasta que ambos tengan entradas válidas. Lo mismo ocurre con la posición y las vidas de cada jugador. Finalmente se añade un bucle al juego para poder salir o volver a jugar luego de cada partida.|
| DF3 Fin de la partida | `game_logic.py`, líneas: 100 - 149 | Se válido la entrada de la asignación de vidas de cada jugador mediante la función "isdigit()" para verificar que sea una entrada válida. Finalmente se añade un bucle al juego para poder salir o volver a jugar luego de cada partida. |

## Video explicativo

[Enlace al video] (máximo 5 minutos: el menú, la validación con una jugada inválida, el fin de la partida y cómo
tradujimos un diagrama a código).

## Licencia

Este proyecto se distribuye bajo la licencia [MIT]. El texto completo está en el archivo `LICENSE`.

## Declaración de autoría

Declaramos que el código de este repositorio fue escrito por los integrantes del equipo, salvo los recursos
citados en la sección «Créditos».

## Créditos

| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
|---|---|---|---|
| [...] | [...] | [...] | [...] |

### Uso de IA

<!-- Si no usaron IA, escriban: «No se usaron herramientas de IA». -->

| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
|---|---|---|
| Antigravity | Se uso para entender de mejor forma como funcionaba GitHub y como funcionaba una licencia MIT| Se creó un archivo LICENSE mediante una plantilla en GitHub al crear el repositorio |

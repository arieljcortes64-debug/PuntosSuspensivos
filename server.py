"""
server.py - Servidor de Batalla de Tanques (Jugador 1) [Fase 4]

Qué hará este archivo:
- Iniciar un servidor con socket TCP en la red LAN y esperar al Jugador 2.
- Enviar el estado inicial al conectarse el cliente (posiciones y 3 vidas).
- Recibir los inputs del Jugador 2 (W, A, S, D, E, Q, ESQ, ClickIzq).
- Validar límites del mapa, disparos, impactos y vidas de ambos tanques.
- Enviar actualizaciones de posición/estado y anunciar al ganador o desconexión.
"""

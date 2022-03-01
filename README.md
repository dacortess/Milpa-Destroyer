# **Milpa Destroyer**

A spaceships plataform multiplayer game.

# Introduction

The game logic was created with pygame and the multiplayer was created with the libraries sockets and threading.

This proyect contains two elements:
1. The server
2. The client

The server is independent from the game, this means that you can run it from another place or computer that is connected to the same local network as the clients.

The game needs, as minimum, two succsesfull conexions to start (two clients). If a third player run the client, the game will wait for another player to open the client. And so on.

# Requirements

1. Python 3.x
2. Pygame 2.1.2

# How To Play

To start the server:

```console
$ python Server/server.py
```
To open a game client:

```console
$ python main.py
```

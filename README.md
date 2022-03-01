# **Milpa Destroyer**

A spaceships plataform multiplayer game.

# Introduction

The game logic was created with pygame and the multiplayer was created with the libraries sockets and threading.

This proyect contains two elements:
1. The server
2. The client

The server is independent from the game, this means that you can run it from another place or computer that is connected to the same local network as the clients.

At enter the game, the client have two options, and the server and the player playing in this moments decide what you do. If exist a player waiting for a teamate, the server conext you with him, otherwise, you the server will have you wqaiting for another player.

For the above, the game needs, as minimum, two succsesfull conexions to start (two clients). 

# How To Play

The game consist in defeat the other player shotting him laser bullets, when you hit a shot, the score increase in one point. Each heart resist 6 hits, so if you recive 18 hits, you lose the game.

You can only move your spaceship sideways, and you can shot a bullet with crtl key. You can shot at most three bullets, so if you have three bullets in the screen, when a bullet hit the enemy or get out the screen you can shoot 1 more.

# Game Caracteristics

If you are waiting for another player to play, the game shows you a waiting message and dont shows the other player.

<img src="rm_images/p1_waiting.png"
     alt="La cabeza y el torso de un esqueleto de dinosaurio;
           tiene una cabeza grande con dientes largos y afilados"
     width="300">

When the 2 players are connected, the game shows all the interface wich is made up of the lifes, scores and players.


### **Player 2**
<img src="rm_images/p2.png"
     alt="La cabeza y el torso de un esqueleto de dinosaurio;
           tiene una cabeza grande con dientes largos y afilados"
     width="300">

### **Player 1**
<img src="rm_images/p1.png"
     alt="La cabeza y el torso de un esqueleto de dinosaurio;
           tiene una cabeza grande con dientes largos y afilados"
     width="300">

And when a player defeat his teamate, the game show a message with the winner.

<img src="rm_images/winner.png"
     alt="La cabeza y el torso de un esqueleto de dinosaurio;
           tiene una cabeza grande con dientes largos y afilados"
     width="300">

# Requirements

- Python 3.x
- Pygame 2.1.2

# How To Play

To start the server:

```console
$ python Server/server.py
```
To open a game client:

```console
$ python main.py
```

# Bugs/Errors

1. The changes in the score and life depends the client. **(Fixed)** 
2. When two players finish the game, the server do not remove his data, saving trash info in memory.

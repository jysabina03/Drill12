import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie


# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global balls

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)
    game_world.add_collision_pair('boy:ball',boy,None)
    # fill here

    balls = [Ball(random.randint(100,1500),60,0)for _ in range(30)]
    game_world.add_objects(balls,1)

    for ball in balls:
        game_world.add_collision_pair('boy:ball',None,ball)

    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies,1)

    game_world.add_collision_pair('zombie:ball',boy,None)








def finish():
    game_world.clear()
    pass


def update():
    game_world.update()

    # fill here
    game_world.handle_coollisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass


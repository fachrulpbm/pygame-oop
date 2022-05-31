import pygame
# from bullets.arrow import Arrow
from bullets.fire import Fire
from control import GameController
from scene import Scene
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3
from levels.level4 import Level4
from levels.level5 import Level5
from player import Player

pygame.init()

clock = pygame.time.Clock()


scene = Scene((640, 480))
scene.setup_level(
  Level1,
  Level2,
  Level3,
  Level4,
  Level5,
)

scene.next_level()

player = Player(scene, Fire())
game_controller = GameController(player)

running = True

while(running):
  scene.fill()
  game_controller.keyboard_event()
  game_controller.mouse_position_event()
  clock.tick(60)
  pygame.display.flip()
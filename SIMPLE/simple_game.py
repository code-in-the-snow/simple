# 11-12-2015
# simple_game.py
# Script that calls game app and interface.

from gameApp import GameApp
from graphic_interface import GraphicInterface

interface = GraphicInterface()
game = GameApp(interface)
game.run()

# 11-12-2015
# simple_game.py
# Script that calls game app and interface.

from gameApp import GameApp
from text_interface import TextInterface

interface = TextInterface()
game = GameApp(interface)
game.run()

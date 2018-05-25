import Inventory
import Character
import GameState
import time
import Key


mark = 4101011
if GameState.IsInGame():
    if Character.HasBuff(2, mark) == False:
        Key.Press(0x22)
        time.sleep(1)

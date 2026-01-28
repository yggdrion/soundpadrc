import sys
import time

sys.path.insert(0, "..")
from src.soundpadrc import Soundpad

sp = Soundpad()

while True:
    try:
        print(sp.categories())
        # print(sp.query_sounds("hobbit"))
        # print(sp.get_all_sounds())
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(3)

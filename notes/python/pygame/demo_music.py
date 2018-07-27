"""
add music is a not kernel question
"""

import os
import pygame, sys
import time


source = "/home/martin/AllWorkStation/Atom/learnPython/pygame/source"
m = os.path.join(source, "Madilyn Bailey - Maps.mp3")


soundObj = pygame.mixer.Sound(m)
soundObj.play()
time.sleep(10)
soundObj.stop()

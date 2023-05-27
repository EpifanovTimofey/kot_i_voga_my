import time

import view
import menu_view
import controller
import model
import menu_controller

while True:
    if model.scena == "play":
        time.sleep(1 / 70)
        controller.p()
        view.flip()
        model.move_ob()
        model.move_kaplya()
    elif model.scena == "menu":
        menu_view.m()
        menu_controller.p()
    elif model.scena == "pause":
        menu_view.a()
        menu_controller.p2()

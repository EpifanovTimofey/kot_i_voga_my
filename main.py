import time

import view
import controller
import model
while True:
    time.sleep(1/70)
    controller.p()
    view.flip()
    model.move_ob()
    model.move_kaplya()

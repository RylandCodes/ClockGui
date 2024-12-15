import pyglet
from pyglet.text import Label
import time

window = pyglet.window.Window()
time_label = Label(str(time.strftime("%H:%M:%S")), font_size=60,x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

def update(dt):
    current_time = time.strftime("%H:%M:%S")
    time_label.text = f"{current_time}"

@window.event
def on_draw():
    window.clear()
    time_label.draw()

pyglet.clock.schedule_interval(update, 1)
pyglet.app.run()

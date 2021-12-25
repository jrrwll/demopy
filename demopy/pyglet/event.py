from demopy.pyglet.main_window import window


@window.event
def on_resize(width, height):
    print('The window was resized to %dx%d' % (width, height))

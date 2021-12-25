import pyglet


class Resource:

    def __init__(self):
        pyglet.resource.path = ['./img']
        pyglet.resource.reindex()

        self.wood_image = pyglet.resource.image('green_wood.png')
        # for windows/linux
        self.icon32 = pyglet.resource.image('military_tank32x32.png')
        # for mac
        self.icon128 = pyglet.resource.image('military_tank128x128.png')


def load_resource() -> Resource:
    return Resource()

import pyglet

from demopy.pyglet.env import g_caption, g_resource, g_user_pref
from demopy.pyglet.util import center_image

window = pyglet.window.Window(
    caption=g_caption,
    width=g_user_pref.win_width,
    height=g_user_pref.win_height)

# win size
window.set_visible(False)
if g_user_pref.fullscreen:
    window.set_fullscreen(True)

# win icon
window.set_icon(g_resource.icon128, g_resource.icon32)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=460)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=window.width // 2, y=window.height // 2,
                                anchor_x='center')

center_image(g_resource.wood_image)
player_ship = pyglet.sprite.Sprite(img=g_resource.wood_image, x=400, y=300)


@window.event
def on_draw():
    window.clear()
    level_label.draw()
    score_label.draw()
    player_ship.draw()


def show_prev_window():
    window.set_visible(True)
    window.switch_to()

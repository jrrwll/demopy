import pyglet

from demopy.pyglet.env import g_caption, g_resource, g_user_pref

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


def show_main_window():
    window.set_visible(True)
    window.switch_to()

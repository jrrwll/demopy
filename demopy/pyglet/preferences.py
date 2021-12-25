class Preferences:

    def __init__(self):
        self.fullscreen = False
        self.win_width = 800
        self.win_height = 600


def load_user_pref() -> Preferences:
    pref = Preferences()
    return pref

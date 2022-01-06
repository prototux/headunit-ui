from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
import os

_app_name_ = 'music'

class musicApp(Screen):
    def __init__(self, **kwargs):
        super(musicApp, self).__init__(**kwargs)
        self.name = _app_name_
        self.root = App.get_running_app().root
        self.dir = dirname = os.path.dirname(__file__)
        layout = Builder.load_file("{}/music.kv".format(self.dir))
        layout.ids['background'].source = '{}/img/background.png'.format(self.dir)

        layout.ids['album_art'].source = '{}/img/album.png'.format(self.dir)


        for i in range(1, 100):
            playlist = Button(text='Playlist {}'.format(i), size_hint_y=None)
            layout.ids['playlists_list'].add_widget(playlist)
        self.add_widget(layout)

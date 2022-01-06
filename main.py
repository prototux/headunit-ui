import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty, ObjectProperty
from kivy.clock import Clock

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
import importlib
from functools import partial
import yaml
import sys

# Custom widgets
from widgets import AppsScreen, ImageButton, BarIcon, AppsTrayIcon

class Apps:
    def __init__(self):
        self.apps = {}

    def add_app(self, name, dt=None):
        if name in self.apps:
            print('An app already exists with the name {}, aborting'.format(name))
            return

        try:
            spec = importlib.util.spec_from_file_location(name, './apps/{}/__init__.py'.format(name))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            instance = getattr(mod, '{}App'.format(name))()
        except:
            mod = importlib.import_module('apps.{}'.format(name), package=__name__)
            instance = getattr(mod, '{}App'.format(name))()

        App.get_running_app().root.ids['sm'].add_widget(instance)
        App.get_running_app().root.ids['apps_grid'].add_widget(ImageButton(app=name))
        self.apps[name] = instance

    def add_shortcut(self, name, dt=None):
        App.get_running_app().root.ids['bar_icons'].add_widget(BarIcon(name=name))

    def stop(self):
        for name, instance in self.apps.items():
            if 'on_stop' in dir(instance):
                print(f'Stopping {name}')
                try:
                    instance.on_stop()
                except:
                    e = sys.exc_info()[0]
                    print(f'Error while stopping {name}: {e}')
            else:
                print(f'Ignoring stopping {name}')


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Add Wallpaper
        self.wallpaper = Image(allow_stretch=True, keep_ratio=False)
        self.wallpaper.source = 'data/wallpapers/blackgreenmaterial.png'
        self.add_widget(self.wallpaper)

class MainApp(App):
    def add_apps_icon(self, dt=None):
        self.root.ids['bar_icons'].add_widget(AppsTrayIcon())

    def build(self):
        self.layout = Builder.load_file("main.kv")

        # Load apps
        for app in config['apps']:
            Clock.schedule_once(partial(apps.add_app, app))

        # Add shortcuts icons and then the apps tray icon
        for app in config['shortcuts']:
            Clock.schedule_once(partial(apps.add_shortcut, app))
        Clock.schedule_once(self.add_apps_icon)

        # Finalize build
        return self.layout

    def on_stop(self):
        global apps
        apps.stop()

if __name__ =='__main__':
    global apps
    apps = Apps()

    global config
    with open('config.yml', 'r') as cs:
        config = yaml.safe_load(cs)

    main = MainApp()
    main.run()

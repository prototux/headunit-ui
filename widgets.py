from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.screenmanager import Screen

class AppsScreen(Screen):
    pass

class ImaeButton(ButtonBehavior, RelativeLayout):
    def __init__(self, app=None, **kwargs):
        super(ImageButton, self).__init__(**kwargs)

        self.app = app
        self.root = App.get_running_app().root

        # App icon
        icon = Image(source='apps/{}/img/icon.png'.format(app))
        icon.size_hint = (0.5, 0.5)
        icon.pos_hint = {'center_x': 0.5, 'center_y': 0.7}
        self.add_widget(icon)

        # App name
        name = Label(text=app)
        name.font_size = 20
        name.pos_hint = {'center_x': 0.5, 'center_y': 0.42}
        self.add_widget(name)
        self.background_color = (0.9, 0.9, 0.9, 0.0)

    def on_press(self):
        self.root.ids['sm'].current = self.app
        print ('pressed: {}'.format(self.app))

class BarIcon(ButtonBehavior, Image):
    icon_size = (0.5, 0.5)
    icon_pos = {'center_x': 0.5, 'center_y': 0.5}

    def __init__(self, name=None, **kwargs):
        super(BarIcon, self).__init__(**kwargs)
        self.name = name
        self.source = 'apps/{}/img/sc_icon.png'.format(self.name)
        self.size_hint = self.icon_size
        self.pos_hint = self.icon_pos

    def on_press(self):
        if self.name == 'apps':
            if self.parent.parent.ids['sm'].current == 'apps':
                self.parent.parent.ids['sm'].transition.direction = 'down'
                self.parent.parent.ids['sm'].current = 'main'
            else:
                self.parent.parent.ids['sm'].transition.direction = 'up'
                self.parent.parent.ids['sm'].current = 'apps'
            self.source = 'data/icons/apps_pressed.png'.format(self.name)
        else:
            #self.size_hint = (0.6, 0.6)
            if self.parent.parent.ids['sm'].current == 'main':
                self.parent.parent.ids['sm'].transition.direction = 'up'
            else:
                self.parent.parent.ids['sm'].transition.direction = 'right'
            self.parent.parent.ids['sm'].current = self.name

    def on_release(self):
        if self.name == 'apps':
            self.source = 'apps/{}/img/sc_icon.png'.format(self.name)
        #else:
        #    self.size_hint = (0.5, 0.5)

class AppsTrayIcon(BarIcon):
    def __init__(self, **kwargs):
        super(AppsTrayIcon, self).__init__(**kwargs)
        self.source = 'data/icons/apps.png'
        self.size_hint = self.icon_size
        self.pos_hint = self.icon_pos

    def on_press(self):
        if self.parent.parent.ids['sm'].current == 'apps':
            self.parent.parent.ids['sm'].transition.direction = 'down'
            self.parent.parent.ids['sm'].current = 'main'
        else:
            self.parent.parent.ids['sm'].transition.direction = 'up'
            self.parent.parent.ids['sm'].current = 'apps'
        self.source = 'data/icons/apps_pressed.png'.format(self.name)

    def on_release(self):
        self.source = 'data/icons/apps.png'

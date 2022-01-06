import __init__ as app
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

global sub_app

class SubApp(App):
    def build(self):
        sm = ScreenManager(id='sm')
        sm.add_widget(sub_app())
        return sm

if __name__ =='__main__':
    sub_app = getattr(app, '{}App'.format(app._app_name_))
    SubApp().run()

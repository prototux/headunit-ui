from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


from kivy.uix.screenmanager import Screen

from kivy.core.image import Image as CoreImage
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.clock import Clock
from PIL import Image, ImageDraw, ImageFont, ImageGrab
from io import BytesIO
import threading
import sched, time
from functools import partial

_app_name_ = 'test'

class testApp(Screen):
    def update_screen(self, *args):
        frame = ImageGrab.grab().transpose(method=Image.FLIP_TOP_BOTTOM).tobytes()
        self.texture.blit_buffer(frame, colorfmt='rgb', bufferfmt='ubyte')

    def __init__(self, **kwargs):
        super(testApp, self).__init__(**kwargs)
        self.name = 'test'
        App.get_running_app().root

        # Try something
        self.texture = Texture.create(size=(1920*2, 1080*2))
        self.screen = Widget()
        self.add_widget(self.screen)
        with self.screen.canvas:
            Rectangle(texture=self.texture, pos=self.screen.pos, size=(1000, 450))

    def on_enter(self):
        Clock.schedule_interval(self.update_screen, 0.0001)

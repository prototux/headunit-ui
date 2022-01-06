import os
import sched, time
import threading
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapMarker, MapLayer

_app_name_ = 'navigation'

class navigationApp(Screen):
    def __init__(self, **kwargs):
        super(navigationApp, self).__init__(**kwargs)
        self.name = _app_name_
        self.root = App.get_running_app().root
        self.dir = dirname = os.path.dirname(__file__)

        self.sched = sched.scheduler(time.time, time.sleep)
        self.sched.enter(1, 10, self.update_coord)

        layout = Builder.load_file("{}/navigation.kv".format(self.dir))
        self.map = layout.ids.map
        self.add_widget(layout)

    def update_coord(self):
        #print("UPDATE!")
        self.car.lat += 0.001
        self.map.center_on(self.map.lat+0.001, self.map.lon)
        self.sched.enter(1, 10, self.update_coord)


    def on_enter(self):
        # Setup map
        self.map.center_on(48.856614,2.3522219)
        self.car = MapMarker(lat=48.856614, lon=2.3522219)
        self.map.add_marker(self.car)

        # Run auto-update
        self.thread = threading.Thread(target=self.sched.run)
        self.thread.start()

    def on_stop(self):
        if self.hasattr('thread'):
            self.thread.stop()

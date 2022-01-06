# HeadUnit UI

## Intro

This is the UI part of a headunit project from OpenLeo, based on python and kivy, it looks like this:

![headunit preview image](.github/preview.gif?raw=true)

## Design (and integration in the whole head unit project)

This should be launched last, and ideally (not there yet), it should only interface to the other components of the headunit system, not directly to CAN/VAN and devices. A watchdog system (with the UI sending a heartbeat to the OS) would be ideal, as this could then be used to reload the UI should a crash happen.

The UI is based on a core that is basically the home screen + the app bar + launching apps and giving them context (and ideally, custom widgets to have a coherent style across all apps). All the actual features are in "apps", which are actually python modules.


## Apps design rules

* You can test your apps without launching the whole UI by running the app as a module (eg. with it's `__main__.py`)
* You should avoid multiple menus and submenus, keep it simple, it is used while driving!
* You should only interface with the car and devices thru what the headunit and UI provides. some apps may require direct connection (for example a diagnostics app that would need direct connection to CAN), but if you happens to connect directly to something, it is more likely that the actual need would be to add a component to the head unit OS instead.
* Dependencies should be self contained, if possible.
* Two icons are needed: `icon.png` for the menu and `sc_icon.png` for the shortcut in app bar

## FAQ

* **Why using python and kivy for an embedded project?** Because it was the best compromise between being easy to work with, without licencing nightmare, and still being able to work directly on a framebuffer (kivy being SDL2 based, you can run it without X11 or Wayland).
* **Why only the UI?** Because it makes the whole head unit more reliable, if the UI crashes, it wouldn't lose CAN frames or the music being played, and the embedded linux can then detect and reload the UI only, which should make it safer as it wouldn't distract as much while driving.
* **Is this PSA/Leo only?** Actually, the whole head unit design is made so it should be possible to port it for any other car architecture, even if these aren't the focus of OpenLeo.
* 

## TODO

* Give the apps context so they can interface with the car (can bus for telematics, climate control, and the like)
* Also give context for the other components of the head unit (music playback, navigation, bluetooth...)
* Have a basic (eg. turn by turn symbols) navigation
* Have working apps...
* Add custom widgets that follow a common OpenLeo design guiderules set
* Inject constant infos to apps (car make, model, version, etc)

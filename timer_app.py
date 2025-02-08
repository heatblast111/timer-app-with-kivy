import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class OutWindow(Widget):
    pass
class TimerApp(App):
    def build(self):
        return OutWindow()

if __name__ == '__main__':
    TimerApp().run()
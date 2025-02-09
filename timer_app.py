import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import time

class OutWindow(Widget):
    pass
class TimerApp(App):
    def build(self):
        return OutWindow()
    def timer_function(self):
        max_seconds = int(input("enter the timer count in seconds : "))
        for i in range(max_seconds, 0, -1):
            sec = i % 60;
            mins = int(i / 60) % 60
            hour = int(i / 3600)
            print(f'{hour:02d} : {mins:02d} : {sec:02d}')
            time.sleep(1)



if __name__ == '__main__':
    TimerApp().timer_function()
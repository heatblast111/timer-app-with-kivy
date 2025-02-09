from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
# Config.set('graphics', 'fullscreen', 'auto')


class RootWidget(BoxLayout):
    pass  

class CountdownWidget(BoxLayout):
    # Holds the remaining seconds.
    remaining = NumericProperty(0)
    # Displays the timer in hh:mm:ss format.
    timer_text = StringProperty("00:00:00")

    def start_timer(self):
        """Starts the countdown timer using the seconds from the TextInput."""
        try:
            total_seconds = int(self.ids.input_seconds.text)
        except ValueError:
            total_seconds = 0
        
         # Hide the TextInput and Button
        self.ids.input_seconds.opacity = 0
        self.ids.input_seconds.disabled = True
        self.ids.start_button.opacity = 0
        self.ids.start_button.disabled = True

        self.remaining = total_seconds
        self.update_timer_text(self.remaining)

        # Unschedule any previous timer to avoid multiple schedules.
        Clock.unschedule(self.update_timer)
        # Schedule the update_timer callback every second.
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        """Called every second; decrements the counter and updates the display.
        When the timer ends, the TextInput and Button are made visible again."""
        if self.remaining <= 0:
            Clock.unschedule(self.update_timer)
            self.timer_text = "Time's up!"
             # Re-show the TextInput and Button
            self.ids.input_seconds.opacity = 1
            self.ids.input_seconds.disabled = False
            self.ids.start_button.opacity = 1
            self.ids.start_button.disabled = False
        else:
            self.remaining -= 1
            self.update_timer_text(self.remaining)

    def update_timer_text(self, seconds):
        """Formats seconds into hh:mm:ss and updates the label."""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        self.timer_text = f"{hours:02d}:{minutes:02d}:{secs:02d}"


class TimerApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    TimerApp().run()

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout


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

        self.remaining = total_seconds
        self.update_timer_text(self.remaining)

        # Unschedule any previous timer to avoid multiple schedules.
        Clock.unschedule(self.update_timer)
        # Schedule the update_timer callback every second.
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        """Called every second; decrements the counter and updates the display."""
        if self.remaining <= 0:
            Clock.unschedule(self.update_timer)
            self.timer_text = "Time's up!"
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
        # The CountdownWidget now fills the window.
        return CountdownWidget()


if __name__ == "__main__":
    TimerApp().run()

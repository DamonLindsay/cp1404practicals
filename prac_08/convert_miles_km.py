"""
Estimated: 90 minutes
Actual: 70 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRES_CONVERSION_RATE = 1.60934  # 1 kilometer


class MilesToKilometersConverterApp(App):
    """Miles to Kilometres Converter App is a Kivy App for converting miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "0.0"
        return self.root

    def handle_update(self):
        """Handle text input changes and update the displayed result."""
        miles = self.root.ids.user_input.text
        try:
            kilometres = self.convert_miles_to_kilometres(float(miles))
            self.message = f"{kilometres}"
        except ValueError:
            self.message = "0.0"

    def handle_increment(self, increment_value):
        """Increment or decrement the miles based on the given value."""
        current_miles = self.root.ids.user_input.text
        try:
            if not current_miles:
                updated_miles = increment_value
            else:
                miles = float(current_miles)
                updated_miles = miles + increment_value
            self.root.ids.user_input.text = str(updated_miles)
        except ValueError:
            updated_miles = increment_value
            self.root.ids.user_input.text = str(updated_miles)

    def convert_miles_to_kilometres(self, miles):
        """Convert miles to kilometres."""
        return miles * MILES_TO_KILOMETRES_CONVERSION_RATE


MilesToKilometersConverterApp().run()

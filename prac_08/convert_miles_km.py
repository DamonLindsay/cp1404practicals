from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesToKM(App):
    """"""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Enter your miles and press the Convert button to see in Kilometres."
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        miles = self.root.ids.user_input.text
        try:
            kilometres = self.convert_miles_to_km(float(miles))
            self.message = f"{kilometres}"
        except ValueError:
            self.message = "0.0"

    def convert_miles_to_km(self, miles):
        """Convert miles to kilometres."""
        return miles * 1.60934

    def handle_increment(self, increment_value):
        """Increment the miles."""
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


ConvertMilesToKM().run()

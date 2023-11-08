from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKM(App):
    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKM().run()

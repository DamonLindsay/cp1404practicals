"""
Estimated: 30 minutes
Actual: Approx 30 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Dynamic Labels App to dynamically create labels based on information given."""

    def __init__(self, **kwargs):
        """Initialize the Dynamic Labels App object."""
        super().__init__(**kwargs)
        self.name_to_favourite_colour = {"Damon Lindsay": "Purple", "Liam Lindsay": "Green", "Jordan Lindsay": "Pink",
                                         "Camryn Lindsay": "Blue"}

    def build(self):
        """Construct the app."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name, colour in self.name_to_favourite_colour.items():
            temp_label = Label(text=f"{name} - Favourite Colour: {colour}")
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()

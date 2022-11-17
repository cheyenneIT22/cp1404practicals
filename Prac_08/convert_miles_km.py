"""GUI Program- Covert miles to kilometres"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty()


def build(self):
    self.title = "Convert Miles to Kilometres"
    self.root = Builder.load_file('convert_miles_km.kv')
    return self.root


def handle_calculate(self, text):
    print("Handle calculate")
    miles = self.convert_to_number(text)
    self.update_results(miles)


def handle_increment(self, text, change):
    print("handle Increment")
    miles = self.convert_to_number(text) + change
    self.root.ids.input_miles.text = str(miles)


def update_results(self, miles):
    print("Update")
    self.output_km = str(miles * MILES_TO_KM)


def convert_to_number(text):
    try:
        return float(text)
    except ValueError:
        return 0.0


MilesConverterApp().run()

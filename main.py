from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr_tb"


class WidgetLayoutApp(App):
    pass


WidgetLayoutApp().run()

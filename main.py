from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout


class LayoutAssignment(BoxLayout):
    pass


class GridLayoutExample(GridLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        b = Button(text="A", size_hint=(.2, .2))
        self.add_widget(b)


class WidgetLayoutApp(App):
    pass


WidgetLayoutApp().run()

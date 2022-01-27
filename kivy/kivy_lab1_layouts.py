from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    count = 0
    toggle_state = 0
    def on_button_click(self):
        print("Button clicked")
        if self.toggle_state:
            self.count += 1
        self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state =="normal":
            # OFF case
            widget.text = "OFF"
            self.toggle_state = 0
        else:
            # ON case
            widget.text = "ON"
            self.toggle_state = 1


class BoxLayoutExample(BoxLayout):
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()
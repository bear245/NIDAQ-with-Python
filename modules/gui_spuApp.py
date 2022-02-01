from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout




class MainWidget(BoxLayout):
    pass

class BoxLayoutV1(BoxLayout):
    comment_text = StringProperty("comment")
    def on_start_task_click(self):
        print("Start Task clicked")

    def on_stop_task_click(self):
        print("Stop Task clicked")

    def on_do_click(self):
        print("Digital Output clicked")

    def on_di_click(self):
        print("Digital Input clicked")

    def on_ai_click(self):
        print("Analog Input clicked")

    def on_savelog_click(self):
        print("Save log clicked")

    def on_quit_click(self):
        print("Quit clicked")


class BoxLayoutV2(BoxLayout):
    pass

class gui_spuApp(App):
    pass

gui_spuApp().run()
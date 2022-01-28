from kivy.app import App
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0, 1)
            Line(circle=(400, 200, 80), width=2)
            Color(0, 0, 1, 1)
            Line(rectangle=(500, 350, 200, 150), width=2)
            self.rect = Rectangle(pos=(600, 200), size=(150, 100))

    def on_button_a_click(self):
        # print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        if (x + w + inc) <= (self.width):
            x += inc
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=(self.center), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        # print("on size: " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        # print("update")
        x, y = self.ball.pos

        if (self.ball_size + x) > self.width or x < 0:
            self.vx = - self.vx
        if (self.ball_size + y) > self.height or y < 0:
            self.vy = - self.vy
        x += self.vx
        y += self.vy
        self.ball.pos = (x, y)

class CanvasExample6(Widget):
    pass


TheLabApp().run()
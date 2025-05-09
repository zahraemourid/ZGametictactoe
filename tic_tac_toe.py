from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class TicTacToe(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.current = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.spacing = 5
        self.padding = 10

        with self.canvas.before:
            Color(0.9, 0.7, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        for i in range(3):
            for j in range(3):
                btn = Button(font_size=50, background_normal='', background_color=(1, 1, 1, 1))  
                btn.bind(on_press=self.make_move(i, j, btn))
                self.add_widget(btn)

    def make_move(self, i, j, btn):
        def callback(instance):
            if self.board[i][j] == "":
                self.board[i][j] = self.current
                btn.text = self.current
                btn.color = (1, 0, 0, 1) if self.current == "X" else (0, 0, 1, 1)  
                if self.check_winner():
                    self.show_popup(f"{self.current} wins! 🎉")
                    self.reset()
                elif all(cell for row in self.board for cell in row):
                    self.show_popup("It's a draw! 😕")
                    self.reset()
                else:
                    self.current = "O" if self.current == "X" else "X"
        return callback

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return True
            if b[0][i] == b[1][i] == b[2][i] != "":
                return True
        if b[0][0] == b[1][1] == b[2][2] != "":
            return True
        if b[0][2] == b[1][1] == b[2][0] != "":
            return True
        return False

    
    def show_popup(self, message):
        popup_content = Button(text=message, font_size=24, color=(0, 0, 0, 1),
                               background_normal='', background_color=(1, 1, 1, 1))   
        popup = Popup(title='Game Over', content=popup_content,
                      size_hint=(None, None), size=(300, 200))
        popup.open()

    def reset(self):
        self.clear_widgets()
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current = "X"
        for i in range(3):
            for j in range(3):
                btn = Button(font_size=50, background_normal='', background_color=(1, 1, 1, 1))
                btn.bind(on_press=self.make_move(i, j, btn))
                self.add_widget(btn)

    def on_size(self, *args):
        self.rect.size = self.size

    def on_pos(self, *args):
        self.rect.pos = self.pos

class TicApp(App):
    def build(self):
        return TicTacToe()

if __name__ == '__main__':
    TicApp().run()


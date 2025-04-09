from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

from kivy.config import Config  # 📌 Config moduli orqali sozlash
Config.set('graphics', 'width', '900')  # 🔹 Ekran kengligi (800px)
Config.set('graphics', 'height', '600')  # 🔹 Ekran balandligi (600px)
Config.set('graphics', 'resizable', False)  # 🔹 O‘lchamini o‘zgartirib bo‘lmaydi
#Config.set('graphics', 'fullscreen', 'auto')  # 📌 Ilovani to‘liq ekranda ochish
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # 🔹 **Oq fon**
        with self.canvas.before:
            Color(0.8, 0.8, 0.8, 1)  # **Oq rang**
            self.rect = Rectangle(size=self.size, pos=self.pos)

        def update_rect(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        
        self.bind(pos=update_rect, size=update_rect)

        # 🔹 **Fon rasmi**
        bg = Image(source='wing2.jpg', size_hint=(1, 1))  
        layout.add_widget(bg)

        # 🔹 **Sarlavha**
        title = Label(
            text="[b]  Wing     Loong 1 [/b]",
            markup=True,
            font_size="80sp",
            color=(0, 0, 0, 1),  # **Qora matn**
            size_hint=(None, None),
            size=(500, 80),
            pos_hint={"center_x": 0.5, "center_y": 0.85}
        )
        layout.add_widget(title)

        # 🔹 **Xatoliklar tugmasi**
        error_button = Button(
            text="Xatoliklar",
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={"center_x": 0.2, "center_y": 0.7},
            background_color=(135/255, 206/255, 235/255, 1),  # **Qizil tugma**
            color=(1, 1, 1, 1)  # **Oq matn**
        )
        layout.add_widget(error_button)

        # 🔹 **Parvoz oldi tayyorgarlik tugmasi**
        checklist_button = Button(
            text="Parvoz oldi tayyorgarlik",
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={"center_x": 0.8, "center_y": 0.7},
            background_color=(0, 0.9, 0.9, 1),  # **Ko‘k tugma**
            color=(1, 1, 1, 1)  # **Oq matn**
        )
        layout.add_widget(checklist_button)

        self.add_widget(layout)

class HavoPosboniApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        return sm

HavoPosboniApp().run()

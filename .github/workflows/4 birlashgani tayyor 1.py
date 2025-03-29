from kivy.config import Config
Config.set('graphics', 'width', '400')  # 🔹 Ekran kengligi (900px)
Config.set('graphics', 'height', '400')  # 🔹 Ekran balandligi (600px)
Config.set('graphics', 'resizable', False)  # 🔒 Oyna o‘lchamini o‘zgartirishni bloklash
Config.write()
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Line
#from kivy.core.window import Window
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import fitz
import io
import os
from kivy.core.image import Image as CoreImage
from kivy.uix.screenmanager import Screen

from threading import Thread


class StartScreen(Screen):
    def on_pre_enter(self):
        Window.size = (540, 360)  # ✅ StartScreen uchun o'lcham
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # 🔹 **Oq fon**
        with self.canvas.before:
            self.bg_color = Color(0.8, 0.8, 0.8, 1)  # **Oq fon**
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(pos=self.update_rect, size=self.update_rect)

        # 🔹 **Fon rasmi**
        bg = Image(source='wing6.jpg', size_hint=(1, 1))
        layout.add_widget(bg)

        # 🔹 **"Keyingi ekran" tugmasi**
        next_button = Button(
            text="HavoPosboni ",
            font_size="40sp",
            size_hint=(None, None),
            size=(300, 80),
            pos_hint={"center_x": 0.7, "center_y": 0.7},
            background_color=(0, 0, 0, 0),
            color=(0, 0, 1, 1)
        )
        next_button.bind(on_press=self.go_to_next_screen)
        layout.add_widget(next_button)

        self.add_widget(layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_next_screen(self, instance):
        self.manager.current = "menu"

class MenuScreen(Screen):
    def on_pre_enter(self):
        Window.size = (540, 350)  # ✅ StartScreen uchun o'lcham
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # 🔹 **Oq fon**
        with self.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
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
            font_size="50sp",
            color=(0, 0, 1, 1),
            size_hint=(None, None),
            size=(500, 80),
            pos_hint={"center_x": 0.5, "center_y": 0.85}
        )
        layout.add_widget(title)

        # 🔹 **Xatoliklar tugmasi**
        error_button = Button(
            text="Xatoliklar",
            font_size="30sp",
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={"center_x": 0.2, "center_y": 0.6},
            background_color=( 0, 0, 0, 0),
            color=(0, 0, 1, 1)
        )
        error_button.bind(on_press=self.go_to_errors)  # 📌 **Funksiya qo‘shildi**
        layout.add_widget(error_button)

        # 🔹 **Parvoz oldi tayyorgarlik tugmasi**
        checklist_button = Button(
            text="Parvoz oldi \ntayyorgarlik",
            font_size="30sp",
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={"center_x": 0.22, "center_y": 0.3},
            background_color=(0, 0, 0, 0),
            color=(0, 0, 1, 1)
        )
        layout.add_widget(checklist_button)

        # 🔹 **Ortga qaytish tugmasi**
        back_button = Button(
            text="<< ortga",
            font_size="20sp",
            size_hint=(None, None),
            size=(90, 20),
            pos_hint={"center_x": 0.079, "center_y": 0.05},
            background_color=(0, 0, 0, 0),
            color=(0, 0, 1, 1)
        )
        back_button.bind(on_press=self.go_to_start_screen)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_start_screen(self, instance):
        self.manager.current = "start"

    def go_to_errors(self, instance):
        self.manager.current = "errors"  # 📌 **Xatoliklar sahifasiga o‘tish**


###########################################################
# Xatoliklar ro'yxati
errors = {
    "1-kategoriya": [
        "Отказ вычислителя управления полётом",
        "Отказ по телуправлению L и UHF",
        "Отказ по телеизмерению",
        "Отказ телуправления + отказ телеизмерения",
        "Отказ Остановка двигателя",
        "Отказ рулевой машины заслонки",
        "Отказ по горизонтальной фиксации",
        "Отказ по местоположению GPS",
        "Отказ по высоте",
        "Отказ по приборной скорости",
        "Отказ по угловой скорости тангажа",
        "Отказ по сигналу курса",
        "Отказ по сигналу воздушного положения",
        "Отказ выпуска шасси",
        "Отказ лазерной системы инерционной навигации",
        "Количество топлива меньше 30л",
        "Низкий уровень топлива",
        "Stall Speed (Пониженная индикаторная воздушная скорость)",
        "Индикаторная воздушная скорость повышенная",
        "Отказ по безопасной высоте"
    ],
    "2-kategoriya": [
        "Одноканальный отказ вычислителя упр-я полётом",
        "Отказ основной цепи телуправления L",
        "Отказ запасной цепи телуправления UHF",
        "Отказ GPS1",
        "Отказ GPS2",
        "Отказ дифференциального GPS",
        "Отказ неудачной выставки системы инерционной навигации",
        "Отказ неудачной выставки системы стабилизации воздушного положения",
        "Отказ непроходящего самоконтроля системы управления полётом",
        "Отказ передачи приёмника воздушного давления",
        "Передустановка блока управления турбиной",
        "Отказ радиовысотомера",
        "Отказ вычислителя атмосферных данных",
        "Отказ системы стабилизации воздушного положения",
        "Отказ инерционного измерительного блока",
        "Отказ по связи блока управления турбиной",
        "Отказ по неработоспособности рулевой машины носового колеса",
        "Одноканальный отказ рулевой машины заслонки",
        "Одноканальный отказ рулевой машины носового колеса",
        "Отказ рулевых поверхностей",
        "Отказ уборки закрылка",
        "Отказ выпуска закрылка",
        "Понижение напряжения аккумулятора 12В",
        "Отказ распределительной системы",
        "Отказ отрыва диода шины",
        "Отказ электропитания генератора 12В",
        "Пониженные обороты при положении заслонки 115%",
        "Отказ связи вычислителя управления задачами",
        "Отказ управления шасси",
        "Одноканальный отказ по курсу",
        "Ненормальное состояние давления топлива",
        "Отказ датчика уровня топлива",
        "Предупреждение об остатке топлива меньше 75л",
        "Ненормальное состояние двигателя",
        "Отказ электропитания 12В",
        "Отказ основной шины",
        "Отказ вторичной шины",
        "Отказ аварийного электропитания",
        "Низкая ёмкость аккумулятора",
        "Пониженная индикаторная воздушная скорость",
        "Повышенная индикаторная воздушная скорость",
        "Ненормальный полёт по продольному направлению",
        "Несоответствие условий взлёта",
        "Ненормальное давление левого тормоза",
        "Ненормальное давление правого тормоза"
    ],
    "3-kategoriya": [
        "Отказ обжатия шасси",
        "Ненормальное состояние двигателя",
        "Отказ NVRAM (несъёмное запоминающее устройство)",
        "Отказ отсутствия параметров полёта и руления",
        "Отказ отсутствия параметров отклонения нуля рулевой машины",
        "Отказ короткого замыкания диода шины",
        "Отказ связи зарядника",
        "Пониженная температура аккумулятора 12В",
        "Отказ радиовысотомера",
        "Остальные отказы",
        "Отказ прекращения электроснабжения CCS"
    ]
}


class MainScreen(Screen):
    def on_pre_enter(self):
        Window.size = (540, 700)  # ✅ StartScreen uchun o'lcham
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_buttons = []
        
        layout = BoxLayout(orientation='vertical')

                # 🔹 Qidiruv maydoni va ortga qaytish tugmasi bir qatorda
        search_layout = BoxLayout(size_hint_y=None, height=40)

        # Qidiruv maydoni
        self.search_input = TextInput(hint_text="Xatolikni qidiring ",
                                      size_hint=(0.70,1))  # Kattaligi moslashtirildi
        self.search_input.bind(text=self.filter_errors)
        search_layout.add_widget(self.search_input)

        # "X" tozalash tugmasi
        clear_button = Button(
            text="X",
            font_size="14sp",
            size_hint=(0.06, 1),  # 10% joy oladi
            background_normal='',
            background_color=(1, 0.3, 0.3, 1),  # Qizil rang
            color=(0, 0, 0, 1))  # Oq matn

        def clear_search(instance):
            self.search_input.text = ""  # Qidiruv maydonini tozalash

        clear_button.bind(on_press=clear_search)
        search_layout.add_widget(clear_button)

        # 🔹 **Ortga qaytish tugmasi**
        back_button = Button(
            text=" menyuga\nqaytish",
            font_size="12sp",
            size_hint=(0.15, 1),  # Kattaligi moslashtirildi
            background_normal='',
            background_color=(0.9, 0.9, 0.9, 1),
            color=(0, 0, 0, 1),
            halign = 'center',
            valign = 'middle')
        back_button.bind(on_press=self.go_to_start_screen)

        
        search_layout.add_widget(back_button)  # Tugmani qidiruv yoniga qo‘shish

        layout.add_widget(search_layout)  # BoxLayout ni asosiy layoutga qo‘shish

        

        

        # Kategoriyalar menyusi
        menu_layout = BoxLayout(size_hint_y=None, height=50)
        for category in errors.keys():
            btn = Button(text=category, on_press=self.show_category, font_size=14,
                         background_normal = '',
                         background_color=(0.7, 0.7, 0.7, 1),  # Oq tugma
                         color=(0, 0, 0, 1),  # Qora yozuv
                         border=(20, 20, 20, 20))  # Chegara
            def update_border(instance, value):
                instance.canvas.after.clear()
            
               # 🔲 Tugma chegarasini chizish
                with instance.canvas.after:
                    Color(0, 0, 0, 1)  # Chegara rangi (qora)
                    Line(rectangle=(instance.x, instance.y, instance.width, instance.height), width=1.5)
            btn.bind(pos=update_border, size=update_border)  # 📌 Chegarani doimiy yangilash
            menu_layout.add_widget(btn)

        #btn_all = Button(text="Hamma xatoliklar", on_press=self.show_all, font_size=14,
        btn_all = Button(
            text="Hamma xatoliklar",
            on_press=self.show_all,
            font_size=14,
            background_normal='',
            background_color=(0.7, 0.7, 0.7, 1),  # Kulrang tugma
            color=(0, 0, 0, 1),  # Qora matn
            border=(2, 2, 2, 2)
        )

        def update_border(instance, *args):
            instance.canvas.after.clear()
            with instance.canvas.after:
                Color(0, 0, 0, 1)  # Chegara rangi (qora)
                Line(rectangle=(instance.x, instance.y, instance.width, instance.height), width=1.5)

        btn_all.bind(pos=update_border, size=update_border)  # 📌 Chegarani doimiy yangilash
        menu_layout.add_widget(btn_all)
        layout.add_widget(menu_layout)

        # Xatoliklarni chiqarish uchun ScrollView
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=3, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)

        self.show_all()
        self.add_widget(layout)

    

    def show_category(self, instance):
        self.grid.clear_widgets()
        for error in errors[instance.text]:
            btn = Button(text=error, size_hint_y=None, height=60, font_size=12, text_size=(170, None),
                         background_normal = '',
                         background_color=(0.9, 0.9, 0.9, 1),  # Oq fonda tugma
                         color=(0, 0, 0, 1),  # Qora yozuv
                         border=(2, 2, 2, 2))  # Chegaralar
            def update_border(instance, value):
                instance.canvas.after.clear()
            
               # 🔲 Tugma chegarasini chizish
                with instance.canvas.after:
                    Color(0, 0, 0, 1)  # Chegara rangi (qora)
                    Line(rectangle=(instance.x, instance.y, instance.width, instance.height), width=1.5)
            btn.bind(pos=update_border, size=update_border)  # 📌 Chegarani doimiy yangilash
            btn.bind(on_press=self.show_error)
            self.grid.add_widget(btn)

    def show_all(self, *args):
        self.grid.clear_widgets()
        for category in errors:
            for error in errors[category]:
                btn = Button(text=error, size_hint_y=None, height=60, font_size=12, text_size=(170, None),
                             background_normal = '',background_color=(0.9, 0.9, 0.9, 1), color=(0, 0, 0, 1), border=(2, 2, 2, 2))
                def update_border(instance, value):
                    instance.canvas.after.clear()
            
               # 🔲 Tugma chegarasini chizish
                    with instance.canvas.after:
                        Color(0, 0, 0, 1)  # Chegara rangi (qora)
                        Line(rectangle=(instance.x, instance.y, instance.width, instance.height), width=1.5)
                btn.bind(pos=update_border, size=update_border)  # 📌 Chegarani doimiy yangilash
                btn.bind(on_press=self.show_error)
                self.grid.add_widget(btn)

    
    def show_error(self, instance):
        #
    
        error_screen = self.manager.get_screen("error_screen")
        error_screen.display_error(instance.text)  # PDF yuklash
        self.manager.current = "error_screen"

    def filter_errors(self, instance, value):
        search_text = value.lower()
        all_errors = [error for category in errors for error in errors[category]]
        filtered_errors = [error for error in all_errors if search_text in error.lower()]
        self.display_errors(filtered_errors)

    def display_errors(self, error_list):
         self.grid.clear_widgets()
         self.error_buttons.clear()
         for error in error_list:
             btn = Button(text=error, size_hint_y=None, height=60, font_size=12,text_size=(170,None))
             btn.bind(on_press=self.show_error)
             #btn.text_size = (btn.width - 10, None)
             btn.background_normal = ''
             btn.background_color = (0.9, 0.9, 0.9, 1)  # Shaffof yashil tugma
             btn.color = (0, 0, 0, 1)  # Oq matn
             btn.border = (2, 2, 2, 2)  # Yumaloq chekkalar
             btn.halign = 'center'
             btn.valign = 'middle'
             def update_border(instance, value):
                 instance.canvas.after.clear()

                 with instance.canvas.after:
                     Color(0, 0, 0, 1)  # Chegara rangi (qora)
                     Line(rectangle=(instance.x, instance.y, instance.width, instance.height), width=1.5)

             btn.bind(pos=update_border, size=update_border)  # 📌 Chegarani doimiy yangilash
             self.grid.add_widget(btn)
             self.error_buttons.append(btn)
        
         #self.update_layout()
    def go_to_start_screen(self, instance):
        self.manager.current = "menu"

class ErrorScreen(Screen):
    def on_pre_enter(self):
        Window.size = (540, 700)  # ✅ StartScreen uchun o'lcham

    def __init__(self, pdf_path=None, crop_y0=50, crop_y1=-50, scale=1.3, rotation=0, **kwargs):
        super().__init__(**kwargs)
        self.pdf_path = pdf_path  # PDF fayl yo‘li
        self.doc = None  # PDF hujjat
        self.current_page = 0  # Hozirgi sahifa raqami

        # 📌 **Kesish va sifat sozlamalari**
        self.crop_y0 = crop_y0  # Yuqori qirqish
        self.crop_y1 = crop_y1  # Pastki qirqish
        self.scale = scale  # Rasm sifati (masshtab)
        self.rotation = rotation  # Aylantirish burchagi

        self.layout = BoxLayout(orientation='vertical')

        # 📌 **Image widget** (PDF sahifalarini ko‘rsatish uchun)
        self.image_widget = Image(size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(self.image_widget)

        # 🔹 **Navigatsiya tugmalari**
        btn_layout = BoxLayout(size_hint_y=None, height=50)

        self.btn_prev = Button(text=" Oldingi", on_press=self.prev_page, size_hint_x=0.3)
        self.btn_back = Button(text=" Orqaga", on_press=self.go_back, size_hint_x=0.2)
        self.page_label = Label(text="Sahifa 0 / 0", size_hint_x=0.2)
        self.btn_next = Button(text="Keyingi ", on_press=self.next_page, size_hint_x=0.3)

        btn_layout.add_widget(self.btn_back)
        btn_layout.add_widget(self.btn_prev)
        btn_layout.add_widget(self.page_label)
        btn_layout.add_widget(self.btn_next)

        self.layout.add_widget(btn_layout)

        self.add_widget(self.layout)

    def display_error(self, error_text):
        """Tanlangan xatolikka mos PDF-ni yuklash va ko‘rsatish"""
        pdf_folder = "D:/fleshka parol quyish proekt/havo posponi/"  # PDF fayllar katalogi
        pdf_filename = f"{error_text}.pdf"  # Fayl nomi
        self.pdf_path = os.path.join(pdf_folder, pdf_filename)  # To‘liq yo‘l

        if os.path.exists(self.pdf_path):
            self.doc = fitz.open(self.pdf_path)
            self.current_page = 0
            self.show_page()
        else:
            print(f"Xatolik: {self.pdf_path} topilmadi!")

    def show_page(self):
        """PDF sahifani rasmga aylantirib, ekranda ko‘rsatish"""
        if not self.doc or self.current_page >= len(self.doc):
            return
        
        page = self.doc[self.current_page]
        page_rect = page.rect

        # ✅ **Tepa va pastdan kesish (`crop_y0`, `crop_y1`) ishlaydi**
        crop_rect = fitz.Rect(
            page_rect.x0,  
            page_rect.y0 + self.crop_y0,  
            page_rect.x1,  
            page_rect.y1 + self.crop_y1
        )

        # ✅ **Matrix bilan o‘lcham moslash**
        matrix = fitz.Matrix(self.scale, self.scale).prerotate(self.rotation)  # Masshtab va burish
        pix = page.get_pixmap(matrix=matrix, clip=crop_rect, alpha=False)

        # ✅ **Rasmni Kivy formatiga o‘tkazish**
        img_data = io.BytesIO(pix.tobytes("png"))  # PNG format sifatni oshiradi
        texture = CoreImage(img_data, ext="png").texture
        self.image_widget.texture = texture

        # 📌 **Image widget o‘lchamini moslash**
        self.image_widget.size = (pix.width, pix.height)  
        self.page_label.text = f"Sahifa {self.current_page + 1} / {len(self.doc)}"

    def next_page(self, instance):
        """Keyingi sahifaga o‘tish"""
        if self.doc and self.current_page < len(self.doc) - 1:
            self.current_page += 1
            self.show_page()

    def prev_page(self, instance):
        """Oldingi sahifaga o‘tish"""
        if self.doc and self.current_page > 0:
            self.current_page -= 1
            self.show_page()

    def go_back(self, instance):
        """Ortga qaytish (MainScreen ga qaytish)"""
        self.manager.current = "errors"


 ######################################################       

class HavoPosboniApp(App):
    def build(self):
       # Window.icon = "852.png"  # 🔹 **Ilova ikonini belgilash** (PNG formatdagi rasm)
        sm = ScreenManager(transition=NoTransition())  # 🔹 **Tez o‘tish uchun NoTransition qo‘shildi**
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(MainScreen(name='errors'))  # 📌 **Xatoliklar sahifasi qo‘shildi**
        sm.add_widget(ErrorScreen(name="error_screen"))
        return sm

HavoPosboniApp().run()

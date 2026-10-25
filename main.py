import requests
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

SERVER_URL = "http://127.0.0.1:8080/v1/chat/completions"

class ZZZAssistantUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 12
        self.spacing = 8
        
        # Элитная неоновая шапка в стиле New Eridu
        self.header = Label(
            text="[ PROXIFY // SYSTEM OVERLAY ACTIVE ]",
            size_hint_y=0.1,
            color=(0, 1, 0.8, 1),
            bold=True,
            font_size='14sp'
        )
        self.add_widget(self.header)
        
        # Область логов и диалога с ИИ
        self.scroll = ScrollView(size_hint=(1, 0.73))
        self.chat_history = Label(
            text="> Соединение с локальным ядром установлено.\n> Я на связи, Яков. Жду инструкций.\n",
            size_hint_y=None,
            color=(0.8, 0.9, 1, 1),
            halign='left',
            valign='top',
            font_size='13sp'
        )
        self.chat_history.bind(texture_size=self.update_history_height)
        self.scroll.add_widget(self.chat_history)
        self.add_widget(self.scroll)
        
        # Панель ввода запроса
        input_layout = BoxLayout(size_hint_y=0.14, spacing=6)
        self.input_field = TextInput(
            hint_text="Введите запрос...",
            multiline=False,
            background_color=(0.07, 0.09, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 1, 0.8, 1),
            font_size='14sp'
        )
        self.input_field.bind(on_text_validate=self.send_message)
        
        send_btn = Button(
            text="➤",
            size_hint_x=0.18,
            background_color=(0, 1, 0.8, 1),
            color=(0.04, 0.06, 0.1, 1),
            bold=True
        )
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.input_field)
        input_layout.add_widget(send_btn)
        self.add_widget(input_layout)

    def update_history_height(self, instance, value):
        self.chat_history.text_size = (self.scroll.width, None)
        self.chat_history.height = self.chat_history.texture_size[1]

    def send_message(self, instance):
        text = self.input_field.text.strip()
        if not text:
            return
        self.chat_history.text += f"\n[YOU]: {text}"
        self.input_field.text = ""
        threading.Thread(target=self.query_llm, args=(text,)).start()

    def query_llm(self, prompt):
        payload = {
            "model": "local-model",
            "messages": [
                {"role": "system", "content": "Ты — автономный ассистент Якова в стиле Zenless Zone Zero. Отвечай коротко и четко."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 150
        }
        try:
            res = requests.post(SERVER_URL, json=payload, timeout=12)
            if res.status_code == 200:
                ans = res.json()["choices"][0]["message"]["content"].strip()
                self.chat_history.text += f"\n[ZZZ]: {ans}\n"
            else:
                self.chat_history.text += f"\n[ERR]: Код {res.status_code}\n"
        except Exception:
            self.chat_history.text += "\n[ERR]: Нет связи с сервером\n"

class ZZZApp(App):
    def build(self):
        Window.clearcolor = (0.04, 0.06, 0.1, 0.96)
        return ZZZAssistantUI()

if __name__ == "__main__":
    ZZZApp().run()

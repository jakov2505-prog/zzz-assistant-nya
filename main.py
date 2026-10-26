from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import requests

class ZZZAssistantRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(ZZZAssistantRoot, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.title_label = Label(
            text='[b]ZZZ ASSISTANT // NYA[/b]',
            markup=True,
            font_size='24sp',
            halign='center',
            valign='middle',
            color=(0.95, 0.8, 0.2, 1)
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        self.add_widget(self.title_label)

        self.status_label = Label(
            text='Status: Standby [■]',
            font_size='16sp',
            halign='center',
            valign='middle',
            color=(0.8, 0.8, 0.8, 1)
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        self.add_widget(self.status_label)

        self.action_btn = Button(
            text='Запросить статус / Погоду',
            font_size='18sp',
            size_hint=(1, 0.3),
            background_color=(0.9, 0.3, 0.1, 1)
        )
        self.action_btn.bind(on_press=self.on_action_clicked)
        self.add_widget(self.action_btn)

    def on_action_clicked(self, instance):
        self.status_label.text = 'Status: Connecting to Local LLM...'
        Clock.schedule_once(self.fetch_dummy_data, 1)

    def fetch_dummy_data(self, dt):
        try:
            response = requests.get('https://httpbin.org/ip', timeout=3)
            if response.status_code == 200:
                self.status_label.text = 'Status: Online [Connected]'
            else:
                self.status_label.text = 'Status: Error [Bad Code]'
        except Exception as e:
            self.status_label.text = 'Status: Offline / Local Mode'

class ZZZAssistantApp(App):
    def build(self):
        return ZZZAssistantRoot()

if __name__ == '__main__':
    ZZZAssistantApp().run()

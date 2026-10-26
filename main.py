from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ZZZAssistantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        label = Label(
            text='[b]ZZZ Floating Assistant[/b]\nSystem Online',
            markup=True,
            font_size='22sp',
            halign='center',
            valign='middle'
        )
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    ZZZAssistantApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import QLabel
from kivy.uix.button import Button

class GeoAcousticApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.title_label = QLabel(
            text='محلل الصوتيات الجيولوجية',
            font_size=24,
            halign='center'
        )
        
        self.status_label = QLabel(
            text='النظام جاهز للاستشعار وتحليل الطبقات',
            font_size=16,
            halign='center'
        )
        
        scan_button = Button(
            text='بدء المسح التجريبي',
            font_size=18,
            size_hint=(1, 0.3)
        )
        scan_button.bind(on_press=self.start_scan)
        
        layout.add_widget(self.title_label)
        layout.add_widget(self.status_label)
        layout.add_widget(scan_button)
        
        return layout

    def start_scan(self, instance):
        self.status_label.text = 'جاري جمع وتحليل الإشارات الصوتية...'

if __name__ == '__main__':
    GeoAcousticApp().run()

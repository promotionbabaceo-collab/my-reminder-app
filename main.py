from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock

class ReminderApp(App):
    def build(self):
        # App ko automatic full screen aur bina border ke chalane ke liye
        Window.fullscreen = 'auto'
        Window.borderless = True
        
        # Aapki uploaded image ka naam (Dhyan rahe Colab me bhi yahi naam ho)
        self.image_name = "reminder.png" 
        
        # Image widget banana jo poori screen par stretch ho sake
        self.img_widget = Image(source=self.image_name, allow_stretch=True, keep_ratio=False)
        return self.img_widget

    def on_start(self):
        # Jaise hi app shuru ho, screen touch event ko bind kar do
        Window.bind(on_touch_down=self.on_screen_touch)

    def on_screen_touch(self, instance, touch):
        # Agar photo dikh rhi hai, toh touch karne par use chupa do (hide)
        if self.img_widget.opacity == 1:
            self.img_widget.opacity = 0  
            # Thik 10 second baad photo ko dobara dikhane ke liye timer chalu
            Clock.schedule_once(self.show_popup_again, 10) 

    def show_popup_again(self, dt):
        # 10 second khatam hote hi photo fir se full screen par aa jayegi
        self.img_widget.opacity = 1  

if __name__ == "__main__":
    ReminderApp().run()
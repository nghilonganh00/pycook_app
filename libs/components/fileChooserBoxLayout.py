from kivy.uix.boxlayout import BoxLayout
from plyer import filechooser

class FileChooserBoxLayout(BoxLayout):
    added_image_path = ''
    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)
    
    def selected(self, selection):
        self.added_image_path = selection[0]
        self.ids.add_food_image.source = selection[0]
        self.ids.add_food_image.size = (340, 240)





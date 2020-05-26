from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

import win32clipboard

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

saveInput = ""

class CalculatorApp(App):

    def calculate(self, symbol):
        global saveInput
        if symbol.text is 'CA':
            saveInput = self.result.text = ""

        elif symbol.text is '<':
            self.result.text = self.result.text[0:len(self.result.text)-1]

        elif symbol.text is 'M':
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(saveInput)
            win32clipboard.CloseClipboard()
        elif symbol.text is 'MR':
            win32clipboard.OpenClipboard()
            dat = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            self.result.text += dat
            saveInput += dat
        elif symbol.text is 'MC':
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText('')
            win32clipboard.CloseClipboard()

        elif symbol.text is 'Pi':
            self.result.text += '3,1415926'
            saveInput += '3,1415926'
        elif symbol.text is not '=':
            self.result.text += symbol.text
            saveInput += symbol.text

        else:
            try: saveInput = self.result.text = str(eval(saveInput))
            except: saveInput = self.result.text = ""
        
    def build(self):
        root = BoxLayout(orientation = "vertical", padding = 5)

        self.result = TextInput(
            text = "", readonly = True, font_size = 25, 
            size_hint = [1,.65], background_color = [1,1,1,.8])
        root.add_widget(self.result)

        allButtons = GridLayout(cols = 5)

        allButtons.add_widget(Button(text = '7', on_press = self.calculate))
        allButtons.add_widget(Button(text = '8', on_press = self.calculate))
        allButtons.add_widget(Button(text = '9', on_press = self.calculate))
        allButtons.add_widget(Button(text = "+", on_press = self.calculate))
        allButtons.add_widget(Button(text = "CA", on_press = self.calculate))

        allButtons.add_widget(Button(text = '4', on_press = self.calculate))
        allButtons.add_widget(Button(text = '5', on_press = self.calculate))
        allButtons.add_widget(Button(text = '6', on_press = self.calculate))
        allButtons.add_widget(Button(text = "-", on_press = self.calculate))
        allButtons.add_widget(Button(text = "(", on_press = self.calculate))

        allButtons.add_widget(Button(text = '1', on_press = self.calculate))
        allButtons.add_widget(Button(text = '2', on_press = self.calculate))
        allButtons.add_widget(Button(text = '3', on_press = self.calculate))
        allButtons.add_widget(Button(text = "*", on_press = self.calculate))
        allButtons.add_widget(Button(text = ")", on_press = self.calculate))

        allButtons.add_widget(Button(text = '0', on_press = self.calculate))
        allButtons.add_widget(Button(text = ".", on_press = self.calculate))
        allButtons.add_widget(Button(text = "=", on_press = self.calculate))
        allButtons.add_widget(Button(text = "/", on_press = self.calculate))
        allButtons.add_widget(Button(text = "%", on_press = self.calculate))

        allButtons.add_widget(Button(text='Pi', on_press=self.calculate))
        allButtons.add_widget(Button(text="M", on_press=self.calculate))
        allButtons.add_widget(Button(text="MR", on_press=self.calculate))
        allButtons.add_widget(Button(text='MC', on_press=self.calculate))
        allButtons.add_widget(Button(text="<", on_press=self.calculate))

        root.add_widget(allButtons)
        return root

if __name__ == "__main__":
    CalculatorApp().run()
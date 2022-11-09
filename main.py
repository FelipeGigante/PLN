#importação das bibliotecas para PLN
import joblib
from nltk import word_tokenize

#importação das bibliotecas para GUI
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Aplicativo(App):
    
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.6)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.greeting = Label(
                        text= "Digite sua frase para classificação",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    padding_y= (12,12),
                    size_hint= (0.25, 0.25)
                    )

        self.window.add_widget(self.user)

        self.button = Button(
                      text= "Enviar",
                      size_hint= (0.25,0.25),
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        
        path = 'trained_POS_taggers/'
        teste_tagger = joblib.load(path+'POS_tagger_brill.pkl')
        cls = teste_tagger.tag(word_tokenize(self.user.text))
        self.greeting.text = str(cls)
             

if __name__ == "__main__":
    Aplicativo().run()
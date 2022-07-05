from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import textfield

KV=''' 
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'MyApp'
            left_action_items:[["menu", lambda x: x]]
        TelaLogin:
<SenhaCard>:
    size_hint: .7 , .7
    pos_hint:{'center_x':.5 , 'center_y':.5}
    orientation: 'vertical'

    MDBoxLayout:
        size_hint_y: .2
        padding: [20,0,20,0]
        md_bg_color: app.theme_cls.primary_color
    
        MDLabel:
            text:'Mudar Senha'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
        MDIconButton:
            icon:'close-thick'
            on_release: root.fechar_card()
            



    MDFloatLayout 
          
        MDTextField:
            hint_text: 'Nova Senha'
            pos_hint:{'center_x':.5 , 'center_y':.8}
            size_hint_x:.9 
        MDTextField:
            hint_text: 'Confirmar Nova Senha'
            pos_hint:{'center_x':.5 , 'center_y':.6}
            size_hint_x:.9
        MDRaisedButton:
            text:'Salvar'
            pos_hint:{'center_x':.5, 'center_y':.4}

<TelaLogin>:
    MDLabel:
        text:'HITALO VIADO'
        pos_hint: {'center_y':.8}
        halign:'center'
        
    MDTextField:
        size_hint_x:.9
        hint_text:'Email:'
        pos_hint:{'center_x':.5 , 'center_y':.6}
    MDTextField:
        size_hint_x:.9
        hint_text:'Senha:'
        pos_hint:{'center_x':.5 , 'center_y':.5}
    MDRaisedButton:
        pos_hint:{'center_x':.5 , 'center_y':.4}
        text: 'Login'
        size_hint_x:.9
    MDTextButton:
        pos_hint:{'center_x':.5 , 'center_y':.3}
        text: 'Cadastre-se'
    MDTextButton:
        pos_hint:{'center_x':.5 , 'center_y':.2}
        text: 'Esqueceu a senha?'
        on_release: root.abrir_card()
        

'''


class SenhaCard(MDCard):
   def fechar_card(self):
       self.parent.remove_widget(self)

class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())
    


class MainApp(MDApp):
    
    def build(self):
        
        self.theme_cls.primary_palette='Armer'
        return Builder.load_string(KV)
MainApp().run()
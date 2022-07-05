from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import textfield







wapp = '''
Screen:
    
    TelaLogin:


<TelaLogin>:

    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        icon: 'content-cut'
        user_font_size: '75sp'

    MDTextField:
        hint_text: "Email"
        mode: "round"
        max_text_length: 20
        pos_hint:{'center_x':.5 , 'center_y':.5}
        size_hint_x:.6
        fill_color_normal: [255, 0, 0, 0.48]
        line_color: [0, 0, 0, 0.0]
        line_color_focus: 0,0,0,1
        
        

    MDTextField:
        hint_text: "Senha"
        mode: "round"
        max_text_length: 20
        pos_hint:{'center_x':.5 , 'center_y':.4}
        size_hint_x:.6
        fill_color_normal: [255, 0, 0, 0.48]
        line_color: [0, 0, 0, 0.0]
        line_color_focus: 0, 0, 0, 1
        
        

    MDRoundFlatButton:
        text: "Login"
        text_color: 0, 0, 0, 1
        pos_hint:{'center_x':.5 , 'center_y':.3}
        size_hint_x:.3
        md_bg_color: [255, 0, 0, 0.8]
        line_color: [0, 0, 0, 0.0]
        
    
    MDTextButton:
        pos_hint:{'center_x':.5 , 'center_y':.2}
        text: 'Esqueceu a senha ?'
    MDTextButton:
        pos_hint:{'center_x':.5 , 'center_y':.1}
        text: 'Cadastre-se'









'''


class TelaLogin(FloatLayout):
    ...


class main(MDApp):
    def build(self):
        
        return Builder.load_string(wapp)
main().run()
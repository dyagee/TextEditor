#import the neccessary packages

from pywebio.input import*
from pywebio.output import* 
from pywebio.pin import*
from pywebio import config, start_server
from pywebio.session import go_app
import pyperclip as clip

#custom styling for the dark and light theme
dark_css = """
#pywebio-scope-btn button{
    margin-right:20px;
}
#pywebio-scope-container{
    margin-top:5px;
   
}
body{
    background:#000000;
}
.form-group > textarea{
background:none;

 }

"""
light_css = """
#pywebio-scope-btn button{
    margin-right:20px;
}
#pywebio-scope-container{
    margin-top:5px;
   
}
body{
    background:#ffffff;
}

"""
#the various app functionalities
def lowercase():
    text = pin.text.lower()
    pin_update('text',value = text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Lowered successfully!"), closable=True, scope="alert")
    pos()

def trim():
    text = pin.text
    text = " ".join(text.split())
    pin_update('text',value = text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Trimmed successfully!"), closable=True, scope="alert")
    pos()

    
def uppercase():
    text = pin.text.upper()
    pin_update('text',value = text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is UpperCased successfully!"), closable=True, scope="alert")
    pos()
def capitalized():
    text = pin.text.capitalize()
    pin_update('text',value = text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Capitalized successfully!"), closable=True, scope="alert")
    pos()
def paste():
    text = clip.paste()
    pin_update('text',value = text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text Pasted successfully!"), closable=True, scope="alert")
    pos()

def copy():
    clip.copy(pin.text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Copied successfully!"), closable=True, scope="alert")
    pos()
def clearText():
    text = ''
    pin_update('text',value = text)
    clear("alert")
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Cleared successfully!"), closable=True, scope="alert")
    pos()

def replace(s,r):
    text = pin.text
    text = text.replace(r,s,1)
    pin_update('text',value = text)
    clear("alert")
    put_success(put_html("<b>Success</b> Text is Replaced successfully!"), closable=True, scope="alert")
    pos()
def replaceall(s,r):
    text = pin.text
    text = text.replace(r,s)
    pin_update('text',value = text)
    clear("alert")
    put_success(put_html("<b>Success</b> All text Replaced successfully!"), closable=True, scope="alert")
    pos()

def pos():
    #this function returns and focuses on the display scope
    scroll_to("alert", position='bottom')

#dark theme style
@config(css_style=dark_css)
def dark():
    with use_scope("container"):
        #put_row([None,put_link('Dark mode', app='index')],size="75% 10%").style("color:#fff;")
        put_row([None,put_button('Light mode', color="light",outline=True,onclick= lambda :go_app('index',new_window=False))],size="75% 20%").style("color:#fff;")
        put_html("<h2>TEXTEDIT_0.2.0</h2>").style('color:#fff;')
        put_textarea('text', rows=6, placeholder="text to be edited").style("margin-bottom:40px;")
        with use_scope("btn"):
            put_buttons([
                    {'label': 'LowerCase', 'value': 'lower',"color":"light"},
                    {'label': 'Capitalize', 'value': 'capital' ,"color":"light"},
                    {'label': 'Trim', 'value': 'trim' ,"color":"light"},
                    {'label': 'UpperCase', 'value': 'upper', "color":"light"},
                    {'label': 'Copy', 'value': 'copy',"color":"light"},
                    {'label': 'Paste', 'value': 'paste',"color":"light"},
                    {'label': 'Clear', 'value': 'clear',"color":"light"},],onclick=[lowercase,capitalized,trim,uppercase,copy,paste,clearText],outline=True).style("margin-bottom:40px;")
        put_row([put_button("Replace",color='light', onclick= lambda :replace(pin.replace1,pin.replace2), outline=True),None, put_textarea('replace1',rows=2, placeholder="text"),None, put_textarea('replace2',rows=2, placeholder="replaceable text")],size="100px 10px 200px 10px 200px").style(" margin-bottom:20px;")
        put_row([put_button("ReplaceAll",color='light', onclick= lambda :replaceall(pin.replaceall1,pin.replaceall2), outline=True),None, put_textarea('replaceall1',rows=2, placeholder="text",help_text="New Text"),None, put_textarea('replaceall2',rows=2, placeholder="replaceable text",help_text="Text to be Replaced")],size="100px 8px 200px 10px 200px").style("margin-bottom:5px;")
        put_scope("alert").style("position:relative;left:40%;width:400px;")

#default app style
@config(css_style=light_css)
def index():
    with use_scope("container"):
        #put_row([None,put_link('Dark mode', app='dark')],size="75% 10%").style("color:#000000;")
        put_row([None,put_button('Dark mode',color="dark",outline=True,onclick=lambda :go_app('dark',new_window=False))],size="75% 20%").style("color:#000000;")
        put_html("<h2>TEXTEDIT_0.2.0</h2>").style('color:#000000;')
        put_textarea('text', rows=6, placeholder="text to be edited").style("margin-bottom:40px;")
        with use_scope("btn"):
            put_buttons([
                    {'label': 'LowerCase', 'value': 'lower',"color":"dark"},
                    {'label': 'Capitalize', 'value': 'capital' ,"color":"dark"},
                    {'label': 'Trim', 'value': 'trim' ,"color":"dark"},
                    {'label': 'UpperCase', 'value': 'upper', "color":"dark"},
                    {'label': 'Copy', 'value': 'copy',"color":"dark"},
                    {'label': 'Paste', 'value': 'paste',"color":"dark"},
                    {'label': 'Clear', 'value': 'clear',"color":"dark"},],onclick=[lowercase,capitalized,trim,uppercase,copy,paste,clearText],outline=True).style("margin-bottom:40px;")
        put_row([put_button("Replace",color='dark', onclick= lambda :replace(pin.replace1,pin.replace2), outline=True),None, put_textarea('replace1',rows=2, placeholder="text"),None, put_textarea('replace2',rows=2, placeholder="replaceable text")],size="100px 10px 200px 10px 200px").style(" margin-bottom:20px;")
        put_row([put_button("ReplaceAll",color='dark', onclick= lambda :replaceall(pin.replaceall1,pin.replaceall2), outline=True),None, put_textarea('replaceall1',rows=2, placeholder="text",help_text="New Text"),None, put_textarea('replaceall2',rows=2, placeholder="replaceable text",help_text="Text to be Replaced")],size="100px 8px 200px 10px 200px").style("margin-bottom:5px;")
        put_scope("alert").style("position:relative;left:40%;width:400px;")
  
    

if __name__ == "__main__":
    start_server([index,dark],debug=True)
    
           
        
            



















'''put_textarea('text', rows=10, label="TEXTEDIT", placeholder="text to be edited").style("margin-bottom:40px;")
put_buttons([
                {'label': 'LowerCase', 'value': 'lower',"color":"dark"},
                {'label': 'Capitalize', 'value': 'capital' ,"color":"dark"},
                {'label': 'Trim', 'value': 'trim' ,"color":"dark"},
                {'label': 'UpperCase', 'value': 'upper', "color":"dark"},
                {'label': 'Copy', 'value': 'copy',"color":"dark"},
                {'label': 'Paste', 'value': 'paste',"color":"dark"},
                {'label': 'Clear', 'value': 'clear',"color":"dark"},],onclick=[lowercase,capitalized,trim,uppercase,copy,paste,clear],outline=True).style("margin-bottom:40px;")
put_row([put_button("Replace",color='dark', onclick= lambda :replace(pin.replace1,pin.replace2), outline=True),None, put_textarea('replace1',rows=2, placeholder="text",help_text="New Text"),None, put_textarea('replace2',rows=2, placeholder="replaceable text",help_text="Text to be Replaced")],size="100px 10px 200px 10px 200px").style(" margin-bottom:40px;")
put_row([put_button("ReplaceAll",color='dark', onclick= lambda :replaceall(pin.replaceall1,pin.replaceall2), outline=True),None, put_textarea('replaceall1',rows=2, placeholder="text",help_text="New Text"),None, put_textarea('replaceall2',rows=2, placeholder="replaceable text",help_text="Text to be Replaced")],size="100px 8px 200px 10px 200px").style("margin-bottom:5px;")
'''        
   

    
    
    






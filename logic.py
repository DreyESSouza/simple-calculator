def update_display(display, new_text):
    max_characteres = 16
    display.configure(text= new_text[-max_characteres:])

#-----------------------------------------------------------------------------------------------------------------#

def write_display(button,display):
    text = button.cget("text")
    text_label = display.cget("text")
    
    if text_label == "0" or text_label == "Error": 
        clear_display(display)
        text_label=""

    if text_label == "" and text=="0": return
    else: update_display(display, f"{text_label}{text}")

#-----------------------------------------------------------------------------------------------------------------#

def porcetage(button,display):
    symbols = ("-", "+", "÷", "×", ".")
    text_label = display.cget("text")

    for symbol in symbols:
        if text_label.endswith(symbol):
            text_label = text_label[0:-1]
    
    text = button.cget("text")
    if text_label == "" and text == "%": return
    else: update_display(display, f"{text_label + text}")

#-----------------------------------------------------------------------------------------------------------------#

def math_signs(button, display):
    symbols = ("-", "+", "÷", "×")
    text_label = display.cget("text")
    text = button.cget("text")
    
    for symbol in symbols:
        if text_label.endswith(symbol):
            text_label = text_label[0:-1]

    if not text_label == "" or text in ("-", "+"): 
        update_display(display,f"{text_label + text}")
    else: return

#-----------------------------------------------------------------------------------------------------------------#

def calculate(display):
    response = display.cget("text")
    symbols = ("-", "+", "÷", "×", "√")
    
    for symbol in symbols:
        if response.endswith(symbol): return
    
    response = response.replace("÷", "/").replace("×", "*").replace("%","*0.01")
    
    try:
        result = round(eval(response),3)
        update_display(display, f"{result}")
    except:
        update_display(display, "Error")

#-----------------------------------------------------------------------------------------------------------------#

def clear_display(display):
    display.configure(text="")

# ----------------------------------------------------------------------------------------------------------------- #

def delete_caractere(display):
    text_label = display.cget("text")
    text_label = text_label[0:-1]
    display.configure(text=f"{text_label}")
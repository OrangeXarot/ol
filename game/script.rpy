define e = Character("Halo")
define me = Character("[name]")

label name:
    python:
        name = renpy.input("Come ti chiami?", length=32)
        name = name.strip()
    
    menu correct:
        "Ti chiami [name]?"
        "Sì":
            jump dream
        "No":
            jump name

label start:

    jump name
    
label dream:

    show bg white
    show halo dream
    with fade

    e "Here's my cock."
    e "You like it?"

    menu choice:
        "You like it?"
        "Yes":
            jump yessed
        "No":
            jump noed
        
label yessed:
    me "Yes, I love it!"
    jump after

label noed: 
    me "I Hate it!"
    "But I was lying"
    jump after

label after:

    hide bg white
    hide halo
    with dissolve

    me "Wait what?"
    me "What is happening?"

    scene bg wake
    with fade

    me "Ah god damn bro"
    me "Ho rifatto quel sogno"
    me "Certo che addormentarmi giocando ad Halo mi fa sempre quel effetto"
    me "Poi era pure in inglese..."
    me "Vabbè meglio se mi sbrigo a prepararmi che devo andare a scuola"

    return

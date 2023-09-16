define e = Character("Halo")
define me = Character("[name]")
define b = Character("Bullo")
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

    e "Here's my cock, [name]."
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
    me "Certo che addormentarmi giocando ad Halo mi fa sempre quell'effetto"
    me "Poi era pure in inglese..."
    me "Vabbè meglio se mi sbrigo a prepararmi che devo andare a scuola"

    hide bg wake

    #spero questo sia un commento, comunque bisogna aggiungere un bg

    me "Spero che almeno oggi i bulli mi lascino in pace..."
    "2 ore dopo"
    b "hey [name], oggi quanti soldi hai portato?"
    me "No ti prego mi servono per il pranzo"
    b "Cos'hai detto scusami? Prova a parlarmi così un'altra volta e te ne pentirai"
    menu choice1:
        "Come risponderai?"
        "Hai ragione scusa":
            jump pussy
        "Vaffanculo":
            jump bold

label pussy:
    b "Bravo..."
    b "Anzi sai che c'é? Oggi ho voglia di fare male a qualcuno"
    b "Seguimi in bagno"
    jump bullying

label bold:
    b "Come ti permetti figlio di puttana?!"
    "SLAP!"
    b "Ora te vieni con me in bagno"
    jump bullying

label bullying:

    return

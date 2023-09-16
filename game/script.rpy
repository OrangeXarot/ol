define e = Character("Halo")
define me = Character("[name]")
define bullo= Character("Bullo")
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

    #vpunchlink
    #When invoked, this transition shakes the screen vertically for a quarter second. Imitating and customizing this transition and hpunch is best done using ATL Transitions.
    # hpunchlink
    #When invoked, this transition shakes the screen horizontally for a quarter second.

    # https://imgs.search.brave.com/DqTf6mFweu6hoGJHOkiRvDVc_5LluAXUI9Io3jhgtTs/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL2hhbmRzb21l/LWd1eS1wbmctbWFu/LWluLWJsYWNrLWNv/YXQtbWFsZS1oYW5k/c29tZS0yOTAucG5n
    # https://imgs.search.brave.com/P_o8HYtP1oBK4EtwI4Ck5pJhaJhuDJzsB9Xij7Ik19g/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL3BuZy1oZC1o/YW5kc29tZS1tYW4t/eW91LXNob3VsZC1j/aGVjay1vdXQtbmV2/ZXItc3BsaXQtdGhl/LWRpZmZlcmVuY2Ut/YnktY2hyaXMtdm9z/cy1pdHUwMDI3cy1h/LWdyZWF0LWJvb2st/NDAzLnBuZw
    # https://imgs.search.brave.com/D9qxE7wPAbq52ktw_FHYiXmcm1PCqHy_8ubmlTlzZaM/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/Y2xpcGFydG1heC5j/b20vcG5nL21pZGRs/ZS8yMjMtMjIzMjI0/NV9oYW5kc29tZS1w/ZXRlci1mYW1pbHkt/Z3V5LWhhbmRzb21l/LXBldGVyLnBuZw
    # https://imgs.search.brave.com/SHS8l93Sy4Sfd3NYv3kGKZUBHeDDrIZ2bA8TdLvv484/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWcu/bG92ZXBpay5jb20v/b3JpZ2luYWxfb3Jp/Z2luX3BpYy8xOC8x/MS8wMy9jNjE5MzQw/OTI2ZDQ0MGY5Yjky/NjdiZjVkODA1NDY4/MS5wbmdfd2g4NjAu/cG5n
    # https://imgs.search.brave.com/2c3qk6pVCrFVXaCQ9YMLTg-0uJ-XPxYbARkyY5tl99Q/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL3BuZy1oZC1o/YW5kc29tZS1tYW4t/bWFuLWhhbmRzb21l/LWhhbmRzb21lLW1h/bi1tYWxlLXlvdW5n/LXBlb3BsZS02NjYu/cG5n



    me "Spero che almeno oggi i bulli mi lascino in pace..."
    "2 ore dopo"
    
    show bollo
    
    bullo"hey [name], oggi quanti soldi hai portato?"
    me "No ti prego mi servono per il pranzo"
    bullo "Cos'hai detto scusami? Prova a parlarmi così un'altra volta e te ne pentirai"
    menu choice1:
        "Come risponderai?"
        "Hai ragione scusa":
            jump pussy
        "Vaffanculo":
            jump bold

label pussy:

    bullo"Bravo..."
    bullo"Anzi sai che c'é? Oggi ho voglia di fare male a qualcuno"
    bullo"Seguimi in bagno"
    jump bullying

label bold:

    bullo"Come ti permetti figlio di puttana?!"
    "SLAP!"
    
    bullo"Ora te vieni con me in bagno"
    jump bullying

label bullying:

    return

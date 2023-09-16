define e = Character("Halo")
define me = Character("[name]")
define bullo = Character("Bullo")

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

    scene bg white
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


    #vpunch
    #When invoked, this transition shakes the screen vertically for a quarter second. Imitating and customizing this transition and hpunch is best done using ATL Transitions.
    # hpunch
    #When invoked, this transition shakes the screen horizontally for a quarter second.

    scene bg strada with fade:
        xzoom 2 yzoom 2
    # https://www.pinterest.com/pin/827114287795436044/
    # GAy
    


    me "Spero che almeno oggi i bulli mi lascino in pace..."

    scene bg black with fade
    "2 ore dopo"
    
    scene bg classe with fade:
        xzoom 2.5 yzoom 2.5


    show bollo
    
    bullo "hey [name], oggi quanti soldi hai portato?"
    me "No ti prego mi servono per il pranzo"
    bullo "Cos'hai detto scusami? Prova a parlarmi così un'altra volta e te ne pentirai"
    menu choice1:
        "Come risponderai?"
        "Hai ragione scusa":
            jump pussy
        "Vaffanculo":
            jump bold

label pussy:

    bullo "Bravo..."
    bullo "Anzi sai che c'é? Oggi ho voglia di fare male a qualcuno"
    bullo "Seguimi in bagno"
    jump bullying

    
label bold:

    bullo "Come ti permetti figlio di puttana?!"

    scene bg kapow:
        xzoom 3.3 yzoom 2.7


    # https://imgs.search.brave.com/2HxP9DOJKVv-93Gg5_47kvUn80jjrYwvzfEjlypyHZk/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS12ZWN0b3Iv/d29yZC1rYXBvdy1j/b21pYy1jbG91ZF8x/MzA4LTU0NjM0Lmpw/Zz9zaXplPTYyNiZl/eHQ9anBn

    "~ SLAP! ~" with hpunch

    scene bg classe:
        xzoom 2.5 yzoom 2.5
        
    show bollo
    
    bullo "Ora te vieni con me in bagno"
    jump bullying

    # toilet
    # https://imgs.search.brave.com/PNdzFNSOqLqwEUm2pSElgiU4qy72M9uZa_7f092RWwY/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTgz/MjkzOTUwL3Bob3Rv/L29wZW4tdG9pbGV0/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1yMDRndmVkNWY0/dGd0ZmM2aTlzMzFJ/S1lxM1dSaERKVEE3/QXFfT1hUQ1JvPQ
    # https://imgs.search.brave.com/2QJ_zELY4RzwWc5YX2l_0qqlikO-Zkn7vGu7v6UO8Ek/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNTMw/NjIyODI0L3Bob3Rv/L3B1YmxpYy1iYXRo/cm9vbS1zdGFsbC5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/cXh5Sk8wQ3ItY0Vq/dC00ZHFPeF9tRV9G/Q2o4U2xQV1dzbEo1/aXRoUEllUT0
    # https://imgs.search.brave.com/uCjxoMf2-GrE4ZQm181dDc2chd0EW4i2Kq646rGpMkg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNTIz/ODcyNzc5L3Bob3Rv/L21hbi1zaXR0aW5n/LWluLXB1YmxpYy1y/ZXN0cm9vbS5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9YmVm/ckdjVWFxWkpMbUxx/ZjlKU2ZBZDJVRGll/eTJnZTUzLUk4MzZI/VElfST0

    # bathroom
    # https://imgs.search.brave.com/1AztOtEbd9lm5roXEJ-439mLiDt_PJsn31xXzOkOKhw/rs:fit:860:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9j/L2M1L1RvaWxldHNf/aW5fUXVlZW5zbGFu/ZF9BcnRfR2FsbGVy/eV8wMS5qcGc
    # https://imgs.search.brave.com/4P1KDge4AVulQhGvUzFh4krCmFyPZXrucfp9Bm3ozw8/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAwLzkxLzA4LzA0/LzM2MF9GXzkxMDgw/NDA1X210emM5RERr/UU01TVJwSndrNGl4/alU1cnJDT3JQc1My/LmpwZw

label bullying:

    scene bg bagno

    # play sound "woof.mp3" volume 0.5


    bullo "Vieni qua"
    me "Ok..."
    "Oh no cosa vuole fare?"
    play sound "pipe.mp3"
    "~ pipe.mp3 ~"
    me "huh cos'era quel suono??"
    bullo "Stai zitto e vieni qui"

    # splash
    # https://vid.puffyan.us/watch?v=SB-QvuQEmwY (https://www.youtube.com/watch?v=SB-QvuQEmwY shhh)
    # https://imgs.search.brave.com/CQr_ljJ_Nh1TXEzJ9cw8sTaJTHJqGolhqckMgyBoiLU/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTU3/NjcyMTkxL3Bob3Rv/L3NwbGFzaC5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9R2JD/MnhqWkZDTVdaSHQ4/Q2l5SThVLUpOU3Rx/R0ttdVctZzM5Q29t/LXdGZz0
    
    "~ SPLASH ~"
    scene bg splash
    play sound "splash.mp3"
    me "BRHGGRG blbl °°°°"
    "e ancora una volta sono dentro questo cesso"
    scene bg black
    

    scene bg apnea
    


    # Timmy Returner
    return
    

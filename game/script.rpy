define e = Character("Halo")
define me = Character("[name]")
define bullo = Character("Antonio")
define bullo2 = Character("Antonello")
define bullo3 = Character("Bullo 3")

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
    # https://www.myinstants.com/en/instant/youtube-uwuuuuu-67534/ (/s)
    
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
    # 👆🤓

    scene bg strada with fade:
        xzoom 2 yzoom 2
    # https://www.pinterest.com/pin/827114287795436044/
    # GAy
    


    me "Spero che almeno oggi i bulli mi lascino in pace..."

    scene bg black with fade
    "2 ore dopo"
    
    scene bg classe with fade:
        xzoom 2.5 yzoom 2.5

    # bullo2 https://imgs.search.brave.com/-62evOVTI5xU4HmygCYZ_sjexaat2HKIrMy41d4Db88/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL3BuZy1oZC1o/YW5kc29tZS1tYW4t/c3RhcnQteW91ci1w/b3J0Zm9saW8taGFu/ZHNvbWUtZ3V5LXBu/Zy00NjEucG5n
    # bullo3 https://imgs.search.brave.com/ThVgjvUfXCVmvqesLgL-p3zuNofLb2cKvomGT40W-Bg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL2hhbmRzb21l/LWd1eS1wbmctdGFy/a2FuLXRoZW1lLXN0/dWR5LWZvci1tZW4t/c3BlY2lhbC1wbmct/cG5nLW1hbi1oYW5k/c29tZS1ndXlzLWVt/b3Rpb25hbC1wcml2/YXRlLTM5My5wbmc



    show bollo normale
    show bollo2 nero at right
    show bollo3 nero at left
    
    bullo "Hey [name], oggi quanti soldi hai portato?"
    show bollo nero with dissolve
    me "No vi prego mi servono per il pranzo"
    show bollo2 normale with dissolve
    bullo2 "Cos'hai detto scusami? Prova a parlarci così un'altra volta e te ne pentirai"
    menu choice1:
        "Come risponderai?"
        "Hai ragione scusa":
            jump pussy
        "Vaffanculo":
            jump bold

label pussy:

    show bollo nero with dissolve
    show bollo2 nero with dissolve
    show bollo3 nero with dissolve

    me "Avete ragione scusate"
    show bollo3 normale with dissolve
    bullo3 "Bravo..."
    show bollo3 nero with dissolve
    show bollo normale with dissolve
    bullo "Anzi sai che c'é? Oggi ho voglia di fare male a qualcuno"
    bullo "Seguimi in bagno"
    jump bullying

    
label bold:

    show bollo nero with dissolve
    show bollo2 nero with dissolve
    show bollo3 nero with dissolve

    me "Vaffanculo"
    show bollo normale with dissolve
    bullo "Come ti permetti figlio di puttana?!"

    scene bg kapow:
        xzoom 3.3 yzoom 2.7


    # https://imgs.search.brave.com/2HxP9DOJKVv-93Gg5_47kvUn80jjrYwvzfEjlypyHZk/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS12ZWN0b3Iv/d29yZC1rYXBvdy1j/b21pYy1jbG91ZF8x/MzA4LTU0NjM0Lmpw/Zz9zaXplPTYyNiZl/eHQ9anBn
    #https://www.myinstants.com/en/instant/slapped-6402/?utm_source=copy&utm_medium=share
    play sound "slap.mp3"
    "~ SLAP! ~" with hpunch

    scene bg classe:
        xzoom 2.5 yzoom 2.5
        
    show bollo normale
    show bollo2 nero at right
    show bollo3 nero at left
    
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

    scene bg bagno with fade:
        xzoom 3.8 yzoom 3.3

    # play sound "woof.mp3" volume 0.5

    show bollo normale
    show bollo2 nero at right
    show bollo3 nero at left

    bullo "Vieni qua"

    show bollo nero with dissolve
    me "Ok..."
    "Oh no cosa vuole fare?"
    
    # define audio.pipe = "audio/pipe.mp3.mp3"
    # play sound pipe
    
    play sound "audio/pipe.mp3.mp3" 

    "~ pipe.mp3 ~"
    me "Huh cos'era quel suono??"

    show bollo normale with dissolve
    bullo "Stai zitto e vieni qui"

    # splash
    # https://vid.puffyan.us/watch?v=SB-QvuQEmwY (https://www.youtube.com/watch?v=SB-QvuQEmwY shhh)
    # https://imgs.search.brave.com/CQr_ljJ_Nh1TXEzJ9cw8sTaJTHJqGolhqckMgyBoiLU/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTU3/NjcyMTkxL3Bob3Rv/L3NwbGFzaC5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9R2JD/MnhqWkZDTVdaSHQ4/Q2l5SThVLUpOU3Rx/R0ttdVctZzM5Q29t/LXdGZz0
    
    play sound "audio/splash.mp3.mp3"
    scene bg splash:
        xzoom 3.3 yzoom 3
    "~ SPLASH ~"
    
    scene bg black
    me "BRHGGRG blbl °°°°"
    "E ancora una volta sono dentro questo cesso"
    
    # define audio.sunflower = "music/sun-flower-slow-jam.ogg"
    # play sound sunflower
    # no era solo flavio e windows insieme... the fuck is pipe.mp3.mp3

    scene bg apnea with fade:
        xzoom 10 yzoom 10

    "Uff, l'umidità di quest'acqua che mi avvolge è davvero un enigma."
    "In un mondo costantemente guidato da convenzioni e norme sociali,"
    "l'essere bagnati sembra un'anomalia che sfida la nostra percezione dell'ordine."
    "Chi siamo noi, se non creature vulnerabili, esposte agli elementi senza alcun controllo?"
    "L'acqua penetra le fibre del mio abbigliamento, avvicinandosi al mio corpo, e con essa, si insinua un senso di disagio."
    "Mi ritrovo a riflettere sull'inconvenienza di questa situazione, non per la prima volta."
    "Ogni goccia è come una piccola sfida alla mia esistenza, una sfida a mantenermi asciutto e intonso in un mondo che sembra divertirsi a mettermi alla prova."
    "L'umidità rende tutto più pesante, le scarpe squelchiano sotto il mio peso, i vestiti si appiccicano alla pelle, e ogni passo è un impegno."
    "Ma c'è un'essenza più profonda in questo disagio fisico."
    "Essere bagnati mi fa sentire vulnerabile, mi costringe a riconoscere la mia fragilità e la mia dipendenza dagli elementi naturali."
    "Mi chiedo se, in fondo, questa esperienza non sia una lezione di modestia."
    "Il nostro desiderio di controllo, di dominio sulla natura, è spesso illusorio."
    "Siamo soggetti alle forze della natura, e l'acqua è solo uno dei suoi molteplici strumenti di umiliazione."
    "Ma c'è anche bellezza in questa vulnerabilità."
    "Nell'essere bagnati, ci uniamo a un ciclo millenario di cambiamenti di stato dell'acqua, da liquido a vapore, da ghiaccio a rugiada."
    "Siamo parte integrante di questo sistema, eppure spesso ci sforziamo di sfuggire alla sua influenza."
    "Uff, essere bagnati è un'esperienza scomoda, ma forse è anche una lezione."
    "Una lezione sull'accettazione della nostra vulnerabilità, sulla modestia di fronte alla natura, e sulla bellezza dell'essere parte di un mondo in costante mutamento."
    "Forse, in fondo, dovrei ringraziare l'acqua per questa preziosa riflessione."
    "Grazie."
    
    bullo "HEY TU CHI SEI??"
    "Huh?"
    
    bullo3 "NO FERMO"
    play sound "punch.mp3"
    "~ SBANG ~" with hpunch
    play sound "scream.mp3"
    bullo3 "AAAAAAA"
    # bullo 3 muore

    bullo2 "NO NO NO"
    play sound "strongpunch.mp3"
    "~ SVIUUM ~" with hpunch
    play sound "fortnite.mp3"
    bullo2 "EUOIUO"
    # bullo 2 muore

    bullo "PERCHE' COSA TI ABBIAMO FATTO???"
    play sound "falconpunch.mp3"
    "~ FALCON PUNCH ~" with hpunch
    play sound "oof.mp3"
    bullo "OOF"
    # bullo 1 muore


    # https://www.myinstants.com/en/instant/punch1/?utm_source=copy&utm_medium=share
    # https://www.myinstants.com/en/instant/anime-punch/?utm_source=copy&utm_medium=share
    # https://www.myinstants.com/en/instant/falcon-punch/?utm_source=copy&utm_medium=share
    
    # https://www.myinstants.com/en/instant/one-puuuuunch-76720/
    # https://www.myinstants.com/en/instant/muda-muda-muda-kicks-85146/

  
    # https://www.myinstants.com/en/instant/death-sound-fortnite-13941/ METTIAMO3 QUESTO
    # https://www.myinstants.com/en/instant/roblox-death-sound-real-file-9/?utm_source=copy&utm_medium=share
    # https://www.myinstants.com/en/instant/wilhelm-scream/?utm_source=copy&utm_medium=share


    scene bg soffitto with fade
    # Si gira
    show halo normale

    show water:
        alpha .5
        zorder 5

    e "Tutto bene?"
    # halo che dice "boh roba"
    "Che cazzo?"

    scene bg black with fade
    # M.c. sviene (fucking halo starts the riot then he fucking sviene in inglese, ah giusto pass out)
    # https://www.pngegg.com/en/search?q=master+Chief


    # overlay
    # opac

    # show water:
    #       alpha .5
    #       zorder 5
    
    # soffitto https://imgs.search.brave.com/ChxEFNkEhU4vjEX8fbJjKj7gBbrhRvCf4_BGvoE9Hfk/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5sYXZvcmluY2Fz/YS5pdC9wb3N0LzIy/LzIxMjg1L2dhbGxl/cnkvMzgyMTkvY29u/dHJvc29mZml0dG8t/Y29uLWRvY2NpYS1k/aS1sdWNlLWEtbGVk/LmpwZw
    # water https://imgs.search.brave.com/bGuAquUg7yKtjTUZpTtt4v0enXLB9i5evOsYya5gj0k/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTU3/NTcyNTc0L3Bob3Rv/L3dhdGVyLXJpcHBs/ZS1vdmVyLXNhbmR5/LWJlYWNoLmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz15Y0RL/dGtMaDZmSk9CWVVU/c2dOMlQ2MDNiLVR2/TWk4ZWN6TGFTbDRX/TXk0PQ
 
    "fine."
    
    # Timmy Returner 🤓🤓🤓🤓⛪⛪⛪⛪
    return
    

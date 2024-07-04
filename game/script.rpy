define e = Character("Halo")
define me = Character("[name]")
define bullo = Character("Antonio")
define bullo2 = Character("Antonello")
define bullo3 = Character("Bullo 3")
define mist = Character("???")
define cove = Character("Covenant")
define ralof = Character("Ralof")
define prof = Character("Professore")
define morty = Character("Morty")
define batman = Character("Batman") 
define dave = Character("Crazy Dave")
define dio = Character("Dio")
define morde = Character("Mordecock")

label start:
    jump globalsex


label globalsex:
    python:
        mcAffectionRate = 0
        mordeAffectionRate = 0
        
    jump name

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
    python:
        mcAffectionRate += 0.5 
    me "Yes, I love it!"
    # https://www.myinstants.com/en/instant/youtube-uwuuuuu-67534/ (/s)
    
    jump after

label noed: 
    python:
        mcAffectionRate -= 0.3

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
    me "Quel fottuto Antonio"

    scene bg black with fade
    "2 ore dopo"
    
    scene bg classe with fade:
        xzoom 2.5 yzoom 2.5

    # bullo2 https://imgs.search.brave.com/-62evOVTI5xU4HmygCYZ_sjexaat2HKIrMy41d4Db88/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL3BuZy1oZC1o/YW5kc29tZS1tYW4t/c3RhcnQteW91ci1w/b3J0Zm9saW8taGFu/ZHNvbWUtZ3V5LXBu/Zy00NjEucG5n
    # bullo3 https://imgs.search.brave.com/ThVgjvUfXCVmvqesLgL-p3zuNofLb2cKvomGT40W-Bg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL2hhbmRzb21l/LWd1eS1wbmctdGFy/a2FuLXRoZW1lLXN0/dWR5LWZvci1tZW4t/c3BlY2lhbC1wbmct/cG5nLW1hbi1oYW5k/c29tZS1ndXlzLWVt/b3Rpb25hbC1wcml2/YXRlLTM5My5wbmc
    
    "Eccoli stanno arrivando..."


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

    "~ pipe.mp3.mp3 ~"
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
    # - chatgpt

    mist "Lasciatelo in pace"
    bullo "HEY TU CHI SEI??"
    "Huh?"
    
    mist "Ora ti faccio vedere io chi sono"
    bullo3 "NO FERMO"
    play sound "punch.mp3"
    "~ SBANG ~" with hpunch
    play sound "scream.mp3"
    bullo3 "AAAAAAA"
    # bullo 3 muore

    mist "E invece tu..."
    bullo2 "NO NO NO"
    play sound "strongpunch.mp3"
    "~ SVIUUM ~" with hpunch
    play sound "fortnite.mp3"
    bullo2 "EUOIUO"
    # bullo 2 muore

    bullo "PERCHE' COSA TI ABBIAMO FATTO???"
    mist "Sir, finishing this fight, o qualcosa del genere, viene da halo 2, non la sento da millenni"
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


    scene bg soffitto with fade:
        xzoom 3.7 yzoom 3.3

    # Si gira
    show halo normale at center:
        xzoom 1.3 yzoom 1.3
    # https://fortnite.fandom.com2/it/wiki/Master_Chief

    show water:
        alpha .3
        xzoom 3.3 yzoom 3.3
        # zorder 5

    e "Tutto bene?"
    # halo che dice "boh roba"
    "Che cazzo? Master Chief?"

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
 

    scene bg nursery with fade:
        xzoom 1.2 yzoom 1.1
    "Uh? Dove mi trovo?"
    mist "Hey, you, you're finally awake"

    
    me "Aspetta, conosco questa frase..."
    me "VIENE DA The Elder Scrolls V: Skyrim"

    # Ralof
    # https://imgs.search.brave.com/uQ8wU3C4FifTOGon8xSIGwSQ-8Xqi2bzCdkeMJ7xD44/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/bmljZXBuZy5jb20v/cG5nL2RldGFpbC8x/MDA5LTEwMDk3OTEw/X3JhbG9mLXNreXJp/bS1zdG9ybWNsb2Fr/cy1lbGRlcnNjcm9s/bHMtZWxkZXJzY3Jv/bGxzdi1za3lyaW0t/cmFsb2YucG5n
    # Flavio salva questio come "ralof normale"

    # Arbiter (Arbitro) 
    # https://www.planetminecraft.com/skin/the-arbiter-4994491/
    # https://imgbin.com/png/5XFqFMS2/halo-3-halo-2-halo-4-halo-combat-evolved-halo-reach-png
    # https://www.halopedia.org/Ripa_%27Moramee
    # https://imgs.search.brave.com/olqDvKdNzBNte5lVS4EBnhDfdGY-tc2bepX6pODNt18/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/c2Vla3BuZy5jb20v/cG5nL2RldGFpbC82/OS02OTUyODVfaGFs/by1wbmcucG5n
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FArbiter_%2528Halo%2529&psig=AOvVaw0RmWm8xNGAHfhxO8otlfhW&ust=1695068007334000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCIDbp8W6soEDFQAAAAAdAAAAABAE
    # Flavio succhiami il cazzo "covenant normale"
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.aiaschio.it%2Fdaniele-orsato%2F&psig=AOvVaw2SWN5ivvg3c23VGSpOZiUj&ust=1695067934053000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPjkta26soEDFQAAAAAdAAAAABAE
    # approvo


    show ralof normale at center:
        xzoom 1.5 yzoom 1.5
    
    ralof "Eh?"
    me "TU SEI RALOF!"
    # 👆🤓 quanto nerd devi essere per sapere il nome, frocio
    ralof "Come conosci il mio nome?"
    # 👆🤓 chissà perché...
    me "Come fai ad essere qua!?"
    ralof "Boh, credo si sia aperto un portale(?)"

    show ralof black at left
    show covenant normale at right:
        xzoom 1.5 yzoom 1.5
    cove "Ignoralo, si è ritrovato qua e non fa altro che ripetere quella frase"
    show covenant black at right:
        xzoom 1.5 yzoom 1.5
    me "Quale frase?"
    "..."
    me "ASPETTA TU SEI ARBITER WTF"
    show ralof normale at left
    ralof "Questa frase: Hey, you, you're finally awake"
    me "Ahh... COSA CAZZO STA SUCCEDENDO"
    show ralof black at left
    show covenant normale at right
    cove "Come ha già detto lui, sembra che si siano aperti dei portali che hanno connesso diversi mondi"
    me "Questa cosa non ha senso... E POI PERCHE' SEI VESTITO DA INFERMIERA?!"
    cove "Non ti preoccupare"
    cove "Ah la tua vera infermiera mi ha detto che devi tornare in classe se stai bene."
    me "Ok..."
    
    scene bg black with fade
    "Poco dopo..."
    scene bg classe with fade:
        xzoom 2.5 yzoom 2.5
    
    me "Ma cosa sta succendendo in questa giornata?"
    me "Non ci sto capendo niente..."
    show prof normale
    # https://imgs.search.brave.com/2DSBohC317ZpduglYzm_Kxr84-T_4lEV9afy015kA_c/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL2hhbmRzb21l/LWd1eS1wbmctc3Vp/dC1wbmctaW1hZ2Ut/OTIwLnBuZw    
    prof "[name] concentrati! E' da tutta la lezione che sei distratto"
    me "Ah si scusi... Ma non le sembra strano che ci sia un alieno nella nostra infermeria?"
    prof "Ma quale alieno? Smettila di inventarti storie o ti metto una nota"
    me "Va bene..."
    "Ma sto impazzendo?"
    # Spoiler sì

    scene bg black with fade
    
    "Dopo le lezioni..."
    
    scene bg strada with fade:
        xzoom 2 yzoom 2
    
    me "Questa è stata una delle giornate più strane della mia vita"
    me "Forse stare troppo tempo sotto l'acqua del cesso mi ha fatto male..."
    play sound "caduta.mp3"
    "~ THUMP ~" with vpunch
    
    me "Ahia"
    me "Porca troia" 
    me "Fregnacia"
    me "Vaffanculo cazzo" 
    me "Scemo di merda" 
    me "Chiappa"
    me "Puttana laida" 
    me "Troia schifosa" 
    me "Bastardo" 
    me "Puttanella"
    me "Cornuto"
    me "Coglione"
    me "Rincoglionito" 
    me "Figa" 
    me "Cacone"
    me "Comunista" 
    me "Capitalista"
    me "Citrullo" 
    me "Cazzone" 
    me "Mongoloide" 
    me "Stronzo" 
    me "Scemo" 
    me "Sussy Baka"
    me "Merdaccia" 
    me "Porca troia" 
    me "Porca palleta"
    me "Porco cazzo"
    me "Maremma maiala" 
    me "Pirla" 
    me "Cazzo pizza"
    me "Gay" 
    me "Testa di cazzo" 
    me "Puta madre" 
    me "Maiale porco" 
    me "Pene"
    me "Cane" 
    me "Crucco di merda" 
    me "Finocchio" 
    me "Terrone"
    me "Imbecille"
    me "Cretino" 
    me "Cafone"
    me "Frocio" 
    me "9?"
    me "Bimbo minchia"
    me "Minchione"
    me "Mortacci tua"
    me "Cafone"
    me "Succhia" 
    me "Sti cazzi"
    me "Cazzi" 
    me "Perbacco"
    me "Bocchino"
    me "Cessone" 
    me "Chiavare"
    me "Bastardo" 
    me "Balle"
    me "Mortacci" 
    me "Sega (azienda di videogiochi)" 
    me "Sega (l'utensile)"
    me "Sega (la cosa che si fanno i maschietti)"
    me "Fottuto" 
    me "Rompipalle"
    me "Rompicoglioisazzi" 
    me "FIGÀ" 
    me "Mignotta"
    me "Cavoletti"
    me "Pendejo"
    me "Puta madre"
    me "Concha de la lora"
    me "Webon"
    me "Rizzy"
    me "Albóndigas"
    me "Cabrón"
    me "Cagada asquerosa"
    me "Repelente"
    me "Mugrosa"
    me "Diarreosa"
    me "Maldita"
    me "Estercolera"
    me "Inmunda"
    me "Malnacida"
    me "Pudenda"
    me "Maloliente"
    me "Apestosa"
    me "Cabrona"
    me "Maricona"
    me "Huevona"
    me "Tarada"
    me "Cancerígena"
    me "Jodida"
    me "Culiada"
    me "Gilipollesca"
    me "Pelotudo"
    me "Encamada"
    me "Malnacido"
    me "Retardada"
    me "Retrasado"
    me "Anatroccolo"
    me "Incestuoso"
    me "Burda"
    me "Insulza"
    me "Putrefacta"
    me "Diarrea"
    me "Chupapollas"
    me "Soplahuevos"    
    me "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    me "Cerda"
    me "Nauceabunda"
    me "Pasta al huevo"
    me "Cochambrosa"
    me "Infame"
    me "Babbo"
    me "Sei proprio un babbo"
    me "Codardo"
    me "Figlio di sultana"
    "..."

    # Aggiungere più parolacce NO BASTA :'(
    # NO RACIAL COMMENTS mimimi flavio pussy
     


    # "la crittografia assimmetrica è lenta"
    # "quella simmetrica invece è veloce ma c'è il problema che bisogna trasmettere la chiave in un canale sicuro"


    me "Ok mi è passato il dolore, mi sono solo sbucciato il ginocchio"
    
    scene bg black with fade
    
    "Dopo il tempo che [name] ci mette per arrivare a casa..."

    scene bg casa with fade:
        xzoom 2.4 yzoom 2.4
    
    me "Finalmente sono tornato a casa"
    me "Casa dolce casa..."
    me "Vabbè facciamo partire Halo Reach e freghiamocene altamente dei compiti"
    
    scene bg wake with fade
    me "Uè b4stocino69 facciamo qualche giro dentro Reach?"
    # presumo Reach... lol

    scene bg black with fade
    "4 ore dopo..."

    scene bg wake with fade
    
    play sound "knock.mp3"
    "~ KNOCK KNOCK KNOCK ~"
    
    me "CHI CAZZO E' ORA CHE PORCAPUTTANA STO PERDENDO"
    
    scene bg door with fade:
        xzoom 2.5 yzoom 2.5
    # NOTODO IMMAGINE

    show morty normale

    me "Salve, hai bisogno?"
    morty "Mmm-mmmh ciao sono Morty e-ehm... o-oh g-geez"
    me "MA CHE CAZZO"
    me "ALLORA NON STAVO IMPAZZENDO"
    morty "Ehm.. n-non so di cosa tu stia parlando ma a me sembri abbastanza pazzo"
    me "NO NON CAPISCI"
    me "TU NON DOVRESTI ESISTERE"
    me "SEI UN CARTONE ANIMATO"
    # https://www.youtube.com/watch?v=35gH6iWMSM8 anime
    morty "O-oh quello... oh geez potrebbe essere stata colpa mia"
    morty "P-potrei aver fatto un piccolo c-casino con la portal gun..."
    me "TU COSA? CHE CAZZO HAI FATTO?"
    morty "Oh geez, ora ti spiego tutto..." 

    scene bg black with fade
    
    "Dopo un lungo monologo molto descrittivo, e molto importante per la lore e ai fini della storia sull'accaduto"
    
    scene bg door with fade:
        xzoom 2.5 yzoom 2.5

    
    show morty normale
    
    morty "Ed è per questo che devo ritrovare subito Rick"
    me "Zzz..."
    me "Oh hai finito?"
    morty "S-sì, oh geez"
    me "Ok ma in tutto ciò, cosa cazzo centro io?"

    # Morty muore giusto? no, batman non uccide
    

    batman "I AM VENGEANCE"
    play sound "punch.mp3"
    "~ SBANG ~" with hpunch
    
    show morty morto
    morty "AAAAAAAAAAAAAAAAAAAAAAAAAAH"
    # aggiungere immagini TODO
    # http://pluspng.com/img-png/batman-png-1280.png Batman
    # https://e1.pngegg.com/pngimages/72/833/png-clipart-rick-and-morty-hq-resource-man-illustration.png Morty
    morty "SONO M-MORTY, S-SONO M-MORTY M-M-MORTO"
    
    show morty morto black at left with dissolve
    show batman normale at right with dissolve:
        xzoom 0.75 yzoom 0.75
    # https://static.wikia.nocookie.net/rickandmorty/images/5/52/PM-304.png/revision/latest?cb=20210718063614 Morty ferito
    batman "No non sei morto, però tutte le tue ossa sì" 
    show batman normale with dissolve
    show morty morto with dissolve
    morty "Ugh..."
    hide morty
    show batman normale at center with dissolve
    me "Ehm... Batman... Cosa ti ha fatto Morty?"
    batman "Prima di venire qua ha rubato un lecca lecca ad un bambino"
    me "Ah... e non ti sembra di aver esagerato un pochino?"
    batman "Nahh... Boh... Non mi ricordo manco se fosse stato lui a farlo"
    # https://cdn.imgbin.com/23/20/13/imgbin-batman-the-man-who-laughs-joker-drawing-batman-qRBrBreXgLYmGwHZgRb46WbZT.jpg Batman stupido
    # chatgpt è fosse o era?
    me "Uhm... ok..."
    batman "VABBEH FRA, CI SENTIAMO"
    hide batman with dissolve
    play sound "whoosh.mp3"
    "SWOOOOM" with vpunch
    me "bruh... devo decisamente andare a dormire..."
    # AH RAGA DOBBIAMO ASSOLUTAMENTE FARE UNALTRO DREAM SEQUENCE -ELIA
    # SI OK BRO MA CON COSA DENTRO -FLAVIO
    scene bg black with fade
    "Zzz..."
    scene bg white with fade
    show halo dream
    with fade

    e "Hey, [name]."
    e "Do you remember 21 night of September?"
   
    menu september:
        "Do you remember 21 night of September?"
        "Sì":
            jump fatechanged
        "No":
            jump normal


label fatechanged:
    python:
        fatechanged = True
    e "Wake me up when september ends"
    # immagine questa azione avrà ripercusioni sulla story line
    # non so se hai capito
    # https://i.ytimg.com/vi/NEofyFAABEs/maxresdefault.jpg
    # 👍
    show bg ripercussioni at topright:
        xzoom 1.5 yzoom 1.5
    # capito?
    # yep
    jump november

label normal:
    python:
        fatechanged = False
    e "Oh ok"

    jump november

label november:
    hide halo
    with dissolve

    # me "la crittografia assimmetrica è lenta"
    # me "Quella simmetrica invece è veloce ma c'è il problema che bisogna trasmettere la chiave in un canale sicuro"
    # AHAHHAHAHA
    # NOO

    me "Wait what?"
    me "What is happening?"
    
    scene bg wake
    with fade
    me "Ma che cazzo di nuovo"
    me "Halo mi arrapa troppo"

    # quando parla dave : play sound "dave.mp3"
    # https://www.myinstants.com/en/instant/discord-call-44910/?utm_source=copy&utm_medium=share
    # BARREL ROOLL
    # https://vid.puffyan.us/watch?v=iUKRXpL9k10
    
    
    play sound "dave1.mp3"
    " ~ Urlo Distante ~ "
    # meh
    # https://www.myinstants.com/en/instant/crazy-dave-long-3-20460/?utm_source=copy&utm_medium=share
    me "Oddio cosa c'è ora..."
    scene bg fuoricasa with fade:
        xzoom 3.2 yzoom 3.2
    show dave il pazzo

    play sound "dave.mp3"
    dave "IL MONDO STA FINENDO"
    # E POI ARRIVA GERSON 
    # https://www.myinstants.com/en/instant/chinese-rap-song-70819/?utm_source=copy&utm_medium=share

    play sound "dave3.mp3"
    dave "IL MONDO DEI VIDEOGIOCHI STA COLLASSANDO DENTRO IL MONDO REALE"
    play sound "dave2.mp3"
    # https://www.myinstants.com/en/instant/wubbawubawobobwaboulobobelwabbawubbawob-72964/?utm_source=copy&utm_medium=share
    # dave2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    # ...
    dave "COMPRATE LE MIE PIANTE PER DIFENDERVI"
    # https://www.myinstants.com/en/instant/crazy-dave-line-6-4984/?utm_source=copy&utm_medium=share
    # Flavio metti questo (in daveroll), l'hai fatto vero?? siisisisisisisiomomweqopdnwfrgeibto woeèavrà
    play sound "daveroll.mp3"
    dave "SONO IN SCONTOOO!"
    me "Ma che sta dice... Ah giusto, lo chiamano dave il \"pazzo\" per un motivo"
    dave "Crazy? i was crazy once" # (.
    # parte "crazy train.mp3" nah jk
    # non so cosa sia
    # ignorante
    # gay
    me "Once? Se lo dici tu"
    dave "Sei tu quello che sta vedendo un personaggio di un videogioco, fai tu..."
    me "Touché"
    me "WAIT MA QUINDI SIETE VERI O NO??"
    play sound "dave4.mp3"
    dave "COMPRATE LE MIE PIANTE"
    hide dave il pazzo
    with dissolve
    me "..."
    me "E niente l'abbiamo perso"
    # AHAHAHHAHA
    # yay ora appaio io -elia
    me "Non saprò mai se sto impazzendo"
    me "Anche se in questo momento sto parlando da solo"
    mist "Sicuro?"
    me "Oddio chi c'è adesso"
    mist "Proprio Dio"
    me "Quello di JoJo?"
    mist "..."
    mist "No..."
    show keanu at top
    with fade
    me "Ma te sei... Keanu Reeves?"
    dio "No, Keanu è la mia reincarnazione nel mondo terrestre, sono Dio"
    me "Uhhhh ok?"
    dio "Beh... come va la vita?"
    me "Quindi Dio viene a parlare direttamente con me e la prima cosa che mi chiede è 'come va la vita'"
    me "..."
    me "..."
    me "..."
    "Ok sto decisamente impazzendo"
    me "Bene..."
    me "...Anche se credo di star impazzendo"
    dio "Nah sei ancora sano non ti preoccupare"
    me "Certo... Comunque c'era qualcosa che dovevi dirmi oltre a chiedermi come andava la mia vita?"
    dio "Hmmmmm"
    dio "No non credo"
    me "Ok allora puoi andartene per piacere?"
    dio "Hmmmm"
    dio "Ok bella bro"
    dio "Ci vediamo sulla Arasaka Tower"
    "Finalmente"
    dio "Comunque sono tecnicamente pansessuale"
    "..."
    "That's kinda gay"
    dio "Perché amo tutti capito?"
    "..."
    dio "Perché sono Dio no?"
    me "TE NE VAI???"
    dio "OKOK VADO CALMATI ZIO"
    hide keanu 
    with dissolve
    "OHHH"
    "..."
    me "Ok adesso che faccio?"
    me "Boh mi sa che torno dentro casa e mi rimetto a giocare ad halo con b4stocino69"
    me "Oppure a baldur's gate idk"
    # è passato così tanto tempo che prima non esisteva HAHAHAHAHA
    
    scene bg wake with fade
    
    play sound "knock.mp3"
    "~ KNOCK KNOCK KNOCK ~"
    
    me "EH MA DIO SANTO HO APPENA CHIUSO LA PORTA"
    "Anzi lasciamo stare dio che è meglio"
    "E non perché ora so che esiste"
    "Ma perché poi sto coglione torna a parlarmi del fatto che vuole scopare tutti"

    scene bg door with fade:
        xzoom 2.5 yzoom 2.5

    me "CHI CAZZO È?!"

    scene bg fuoricasa with fade:
        xzoom 3.2 yzoom 3.2
    
    e "Mi dispiace disturbare, ma ho sentito che stavi cercando qualcuno con cui giocare a Halo. Sono il leggendario Halo, non so se mi conosci, e ho bisogno del tuo aiuto per sconfiggere un nemico ancora più potente di tutti gli Halo messi insieme."
    me "Master Chief?! oh.. uhm.. wow.. tu mi hai salvato la vita ieri uwu"
    e "Mi chiamo Halo, e sì, a quanto pare sei importante per la lore"
    me "Solo perché sono il protagonista"
    e "Quanto egocentrico calmati fra"
    e "Comunque devi aiutarmi"

    play sound "bonk.mp3"
    "~ BONK ~" with vpunch
    e "AHIA!"
    #show Morde
    #with fade
    morde "You will be far more useful in death"
    me "MA CHE CAZZO TE SEI MORDEKAISER"
    "* Instant boner *"
    morde "Si mortale, e presto sia te che tutti gli altri mortali di questo mondo sarete sotto il mio controllo"
    me "Wowowo slow down daddy... uhm volevo dire... buddy"
    # hihi down
    me "Non puoi metterti ad uccidere tutti e poi risuscitarli"
    morde "Uhm actually, posso farlo"
    "* nerd emoji* "
    #"-🤓"
    e "Non finchè ci sono qua io"
    
    play sound "punch.mp3"
    "~ SBANG ~" with hpunch

    morde "You... have earned my attention..."
    "Developers Note: Mordekeiser ha un problema con la lingua, visto che è bilingue continua a switchare tra inglese e italiano, ogni tanto usa anche il francese"
    #LUI PUò OK?
    morde "Escargot à la Bourguignonne!"
    "Developers Note: Ecco appunto"

    play sound "morde_ult.mp3"
    "~ SWISHIUVUM ~"

    me "Oh shit, non so se Master Chief può vincere uno scontro con Mordekaiser"

    "2 minuti dopo..."

    me "Di solito non dura così tanto la ulti di Mordekaiser..."
    # dura più di me
    
    # play sound "cock.mp69"
    "~ SWOOM ~"

    me "OH ECCOLI"
    "Chissà chi ha vinto..."

    # ↓lemon party***↓
    scene tea party:
        xzoom 1.2
    with fade
    morde "E poi gli ho detto 'You claim strength, Darius? Prove it.'"
    e "Lol (hehe capita? League Of Legends cioè lol hihi) e lui come ha risposto?"
    morde "Boh l'ho one-shottato subito dopo lmao"
    e "Rofl"
    me "Ma che cazzo..."
    morde "Oh hey [name], ho deciso di non conquistare più il tuo mondo tranquillo"
    morde "Ah e halo mi ha detto tutto su di te"
    me "Oh ok ne sono felic-"
    me "Aspetta cosa ti ha detto di me?"
    play sound "mordekaiser_laugh.mp3"
    morde "Solo che sei uno sfigato a cui ha salvato il culo da dei patetici bulli MWAHAHAHAHA"
    # Pazzesco pensare che ora siamo maturi
    e "Ma no dai poverino"
   
menu rebel:
    "Come vuoi rispondere a Mordekaiser??"
    "Succhiami lo scroto troia":
        jump mioScroto
    "Ok scusa morde posso succhiarti le palle per piacere? uwu tehee~~~":
        jump suePalle

label mioScroto:
    python:
        mordeAffectionRate -= 1
    me "Succhiami lo scroto troia"
    morde "COSA HAI DETTO LURIDO MORTALE?!"
    show angryMorde
    play angryAnime.mp3
    "Oh cazzo mi sono appena suicidato"
    me "S-scusa non vo-"
    me "Aspe cos'era quella voce?"
    morde "Ehm... quando mi arrabbio la mia voce diventa un po' acuta"
    morde "MA NON è QUELLO IL PUNTO"
    e "Heyy perché non ci calmiamo un po' tutti eh?"
    morde "NON DIRMI COSA FARE"
    e "Oooook"
    e "(Sottovoce a [name]) Corri a casa mentre provo a calmarlo"
    me "Oh ok grazie"
    morde "*Angry anime girl noises*"
    # (incazzato)


label suePalle:
    python:
        mordeAffectionRate += 0.7
        mcAffectionRate -= 0.5
    me "Ok scusa morde, posso succhiarti le palle per piacere? uwu tehee~~~"
    morde "C-cosa hai detto lurido mortale?!"
    # (appagato e confuso)
    e "Ayo wtf man"
    me "Ehm volevo dire"
    me "Ok scusa morde, mi fanno un po' male le spalle"
    morde "Uh... Ok... Ma non chiamarmi morde"
    me "Oh sì scusa Master"
    e "Mi hai chiamato?"
    morde "..."
    me "MORDEKAISER***"
    morde "What the hell man"
    me "Ok scusate vado a casa mia a piangere sotto la doccia"
    e "Oook..."
    morde "This kid got problems man"
    e "Io te l'ho detto bro"
  

    label palleSucchiate:
    #"Glub glub glub °°°°"
    #morde "MWAHHAHA! Ho usato la mia ulti \"Static Field\" contro di te"
    #morde "Jkjk quella è la ulti di Lux"
    # il resto lo lascio a te
    "Fine."
    
    # Barbie "Now I Am Become Destroyer, the Death of Worlds"
    # Yoshikage Kira fa il suo monologo
    # https://img1.picmix.com/output/stamp/normal/9/5/0/2/2172059_80b99.png me when coffe TODO flavio la voleva Lo useremo quando tradisci mc (non il mc) con qualcunaltro e lui ti scopre
    # Prima o poi aggiungere scena su arasaka tower con dio 
    # 卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍卍
    # non approvo -flavio☭
    # e poi Hitler da un bacio a stalin (https://i.kym-cdn.com/photos/images/original/002/422/739/f49.gif)
    # and HAWK TUAH spit on that thang
    # Timmy Returner 🤓🤓🤓🤓⛪⛪⛪⛪
    return
    

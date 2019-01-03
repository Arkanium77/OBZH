#scene_1
label sc1:

    play music "sounds/music/7.mp3"
    scene bg black
    $renpy.pause(3,hard=True)
    "???" "В какой момент начинается день?"
    "???" "Когда ты открываешь глаза?"
    "???" "Когда ты выпиваешь чашечку ароматного кофе?"
    stop music fadeout 3.0
    play sound "sounds/sound/alarm.mp3"
    "???" "...или когда начинает звенеть этот КОЛОКОЛ АПОКАЛИПСИСА?!"
    scene bg black
    $renpy.pause(3,hard=True)
    stop sound
    play sound  "sounds/sound/punch.mp3"
    scene bg room_j
    with vpunch

    #выползает снизу экрана
    play music "sounds/music/madhouse.mp3"
    show jar pyj dou at wakeup
    $renpy.pause(3,hard=True)
    "???" "С добрым утром, Джаред. С днём рождения тебя."
    jar "Эх, хоть и выходной, но, всё равно, приходится вставать рано."
    jar "За что мне это?!"
    show jar pyj std with dissolve
    jar "Впрочем, не всё так плохо. Мы с Мэй договорились пойти в кино."
    jar "Ладненько, пора завтракать."
    show jar at offscreenleft with move

    scene bg hall
    show dad std at left
    with fade
    show jar pyj std at offscreenright
    show jar pyj std at right with move
    dad "Привет, сын."
    show dad smi with dissolve
    dad "С днём рождения!"
    show dad std
    show jar pyj smi
    with dissolve
    jar "Спасибо, пап."
    jar "Что у нас на завтрак?"
    show jar pyj std at center with move
    show dad smi with dissolve
    dad "Ну, у меня была яичница, а что там у вас с Мэй будет - понятия не имею. Мама ушла на работу, так что..."
    show dad std
    with dissolve
    jar "..."

    stop music
    play sound "sounds/sound/tapestop.mp3"
    show jar pyj exc with vpunch
    jar "Мэй?!"
    dad "Да, она пришла пораньше и ждала пока ты проснёшься."
    show jar with vpunch
    play music "sounds/music/friends.mp3"
    jar "А я чуть в таком виде не вышел, господи. Я сейчас!"
    show jar at offscreenright with move
    show dad smi with dissolve
    dad "Ха-ха. Вот я в твои годы..."

    scene bg black with fade
    #звуки одежды
    "Мэй - моя подруга детства."
    "Мы знакомы ещё с тех пор, как играли вместе в песочнице."
    "Со временем она превратилась в умную и красивую девушку."
    "Было бы очень неловко так опростоволоситься перед ней."
    "Да ещё и в свой день рождения."

    scene bg hall
    show dad std at left
    with fade
    show jar std at offscreenright
    show jar at right with move
    dad "Ну, так-то лучше."
    dad "Ладно, иди уж. А я у себя буду."
    jar "Хорошо."

    show jar at offscreenleft
    show dad at offscreenright
    with move
    #звук лестницы

    scene bg kitchen
    show mai std at left
    show jar std at offscreenright
    with fade
    show jar at right with move
    mai "Джаред!"
    show mai smi with dissolve
    mai "С днём рождения!"
    show mai at center with move #right2
    "С этими словами она подбежала ко мне и крепко обняла."
    show jar blu with dissolve
    jar "Спасибо, Мэй."
    show mai std at left with move
    show jar std with dissolve
    mai "Ну, что, идём?"

    python:
        q=[]
    menu l1:
        "Идём?"
        "Да, я готов.":
            jar "Да, я готов."
            show jar smi with dissolve
            jar "Пойдём."
            stop music fadeout 4.0
            show mai smi with dissolve
            show mai at offscreenright
            show jar at offscreenright
            with move
            jump sc2
        "Нет, подожди." if not (1 and 2) in q:
            jar "Нет, Мэй, погоди."
            show mai dou with dissolve
            mai "Что-то не так?"
            jar "Нет-нет, всё в порядке, просто..."

            menu:
                "Просто..."
                "...я не завтракал." if not 1 in q:
                    init:
                        $eat_c=0
                    $eat_c=1
                    jar "... я не завтракал ещё."
                    mai "Ой, точно. Я как-то и не подумала."
                    mai "Сама-то вовремя поела"
                    show mai smi with dissolve
                    mai "Кушай, это важно."
                    scene bg black with fade
                    "Я наскоро сварил себе макароны, натёр сыр и славно
                    позавтракал."
                    "Мэй, хоть и сказала, что не голодная, присоединилась."
                    scene bg kitchen
                    show mai std at left
                    show jar std at right
                    with fade
                    mai "Ну, что, идём?"
                    $q.append(1)
                    jump l1

                "...надо отца предупредить." if not 2 in q:
                    init:
                        $dad_c=0
                    $dad_c=1
                    jar "... надо сказать отцу."
                    jar "Он будет волноваться."
                    jar "Кроме того, я случайно услышал, что они с мамой хотят
                    устроить мне сюрприз."
                    show jar smi with dissolve
                    jar "Не буду им портить планы."
                    show mai smi with dissolve
                    mai "Это хорошая идея."
                    mai "Давай так и сделаем."
                    mai "Я подожду тебя здесь."
                    show jar std with dissolve
                    jar "Хорошо."
                    show jar at offscreenright with move
                    #черный экран и звук лестницы
                    "Так, отец находится наверху, в своей комнате."
                    "Интересно, каким будет сюрприз?"

                    scene bg hall
                    show dad std at right
                    show jar std at offscreenleft
                    with fade
                    show jar at left with move
                    #удивление отца
                    dad "Ооо, Джаред."
                    jar "Отец, я как раз тебя искал."
                    jar "Мы с Мэй уходим."
                    jar "Вернемся вечером."
                    show dad smi with dissolve
                    dad "Хорошо."
                    dad "Повеселитесь."
                    show dad std with dissolve
                    dad "Только будь внимателен. Смотри по сторонам."
                    show jar smi with dissolve
                    jar "Ха-ха. Хорошо, отец."
                    jar "Я пошёл."
                    show jar at offscreenleft with move
                    #черный экран и звук лестницы

                    scene bg kitchen
                    show mai std at left
                    show jar std at offscreenright
                    with fade
                    show jar at right with move
                    jar "Всё, можем идти."
                    show mai smi with dissolve
                    mai "Отлично."

                    $q.append(2)
                    jump l1
                "...да нет, ничего. Идём.":
                    jar "...да нет, ничего. Просто думал, ничего ли я не забыл."
                    show jar smi with dissolve
                    jar "Идём."
                    stop music fadeout 4.0
                    show mai smi with dissolve
                    show mai at offscreenright
                    show jar at offscreenright
                    with move

                    jump sc2


        "Я передумал.":
            #Звук удара

            play sound "sounds/sound/tapestop.mp3"
            stop music
            #jar "Я передумал."
            show mai ang with vpunch
            mai "ЧТО?!"
            $mes="Возможно, отказывать девушке, которая ждёт тебя с самого утра - не лучшая идея."
            #mai "Я приехала к тебе, а ты ПЕРЕДУМАЛ?!"
            #show jar dou with dissolve
            #jar "Нуу... я хочу побыть дома."
            #jar "Поэтому прости. Поход в кино придётся перенести."

            jump end

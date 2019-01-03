label sc2:
scene bg black with fade
play music "sounds/music/careless.mp3"
jar "Мы вышли из квартиры, спустились в подъезд и пошли по дворам, по которым гуляли в детстве."
jar "Мэй выглядела счастливой и я, глядя на неё, тоже чувствовал в душе что-то тёплое."
play bgs "sounds/sound/street.mp3" fadein 2.0
scene bg street
show mai smi at left
show jar std at right
with Fade(1, 0.2, 1)

mai "...и это так здорово! Надеюсь, фильм окажется действительно хорошим!"
show jar smi with dissolve
jar "На это есть все надежды. Отзывы в интернете хорошие, да и вообще, это же Марвел."
mai "Кстати, а прошлый фильм ты смотрел?"
play bgs1 "sounds/sound/traf.mp3" fadein 2.0
$renpy.pause(2,hard=True)
$ time = 5
$ timer_range = 5
$ timer_jump = 'menu1_slow'
show screen countdown
menu:
    "Мы подошли к дороге. Мэй, кажется, слишком увлечена разговором..."
    "Да, смотрел...":
        hide screen countdown
        jar "Да, смотрел. Мне, если честно, он понравился больше, чем самые первые, хотя..."
        "За разговором я тоже отвлёкся..."
        $mes="Всегда будьте внимательны, переходя дорогу! Сначала посмотрите налево, затем направо и только убедившись в отсутствии опасности переходите дорогу."
        play sound car
        jump end
    "Пожалуй, стоит быть осмотрительнее при переходе дороги.":
        hide screen countdown
        "Движение здесь не слишком оживлённое, но всё равно стоит смотреть по сторонам."
        "Я посмотрел налево."
        show mai at offscreenleft with MoveTransition(3.0)
        "Затем посмотрел направо и... увидел машину, которая едет слишком быстро."
        show jar sad1 with dissolve
        "Ох, а где Мэй..?"
        show jar exc with dissolve
        jar "Мэй, стой!"
        $mes="Если вы видите, что кто-то ведёт себя неосторожно на дороге - остановите его. В конце-концов, этим вы можете спасти другому человеку жизнь."
        play sound car
        jump end
    "Мэй, осторожнее. Дорога ведь...":
        hide screen countdown
        jar "Мэй, осторожнее."
        mai "А? Что?"
        jar "Дорога ведь. Надо быть осторожнее."
        jar "Сначала посмотреть налево."
        jar "Потом посмотреть напра..."
        play sound "sounds/sound/race.mp3"
        show car car at offscreenright
        show car at offscreenleft with MoveTransition(0.35)
        show jar exc
        show mai exc
        with dissolve
        $renpy.pause(2.0,hard=True)
        play sound "sounds/sound/auto.mp3"
        "Мимо нас на полном ходу пронёсся АВТОМОБИЛЬ!"

stop music fadeout 2.0
play music "sounds/music/forest.mp3"
jar "...это было близко."
show mai sad with dissolve
mai "..."
show mai cry with vpunch
mai "!!!"
mai "Я..."
mai "Мы..."
mai "Мы ведь могли..."
jar "Ох. Ну, могли. Но..."
show jar sad with dissolve
jar "Не плачь, пожалуйста."
jar "Всё ведь хорошо кончилось."
show mai sad with dissolve
mai "Да. Но, всё же, это было так страшно."
show jar std with dissolve
jar "Ну же, успокойся. Я знаю, что может поднять тебе настроение!"
show mai dou with dissolve
mai "И что же?"
show jar smi with dissolve
jar "Еда, конечно! Времени у нас полно, так что мы вполне можем зайти поесть."
mai "Я не настолько люблю еду."
show mai smi with dissolve
mai "Но давай зайдём. Раз уж ТЫ хочешь."
stop music fadeout 3.0
show jar at offscreenright
show mai at offscreenright
with MoveTransition(4.0)

jump sc3

label menu1_slow:
    hide screen countdown
    "Я не успел ничего сделать"
    $mes="Всегда будьте внимательны, переходя дорогу! Сначала посмотрите налево, затем направо и только убедившись в отсутствии опасности переходите дорогу."
    play sound car
    jump end

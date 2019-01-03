# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
#define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    #################
    #    ТАЙМЕРЫ    #
    #################
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0


    #ВАРИАНТ С БАРОМ
    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01),
        false=[Hide('countdown'), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.12 xmaximum 300 at alpha_dissolve


    jump sc1
    transform wakeup:
        xalign 0.9
        yalign 17.0
        linear 3.0 yalign 1.0
        #repeat
    init python:
        renpy.music.register_channel("bgs", "sfx", loop=True)
        renpy.music.register_channel("bgs1", "sfx", loop=True)

label end:
    scene bg black with fade
    #stop sound fadeout (0.5)
    stop sound
    stop bgs
    stop bgs1
    stop music
    play sound ds_sound
    show ds with Dissolve(4.3)
    "Здравый смысл""[mes]"
    scene bg black
    show ds
    hide bg black
    show bg black with Dissolve(3)

label sc3:
# scene bg black
# stop sound fadeout 2.0
# stop bgs fadeout 2.0
# stop bgs1 fadeout 2.0
# stop music fadeout 4.0
# $renpy.pause(4,hard=True)
# "Авторы" "Спасибо за прохождение демонстрационной версии игры!"
# "Авторы" "Вы можете свободно использовать все материалы созданные нами, во время работы над игрой. \nПрава на все остальные материалы принадлежат их законным владельцам (см. раздел \"Об игре\")."
scene bg cafe
show jar std at offscreenleft
show mai std at offscreenleft
with fade

show jar at left
show mai at center
with move

jar "Что ты хочешь поесть?"
show mai smi with dissolve
mai "Может быть кексик?"
jar "А с какой начинкой?"

menu:
    "Я бы хотела..."
    "Ванильный":
        show mai std with dissolve
        mai "Я бы хотела ванильный кексик."
        $cake="ванильный"
    "Шоколадный":
        show mai std with dissolve
        mai "Я бы хотела шоколадный кексик."
        $cake="шоколадный"
    "С черникой":
        show mai std with dissolve
        mai "Я бы хотела кексик с черникой."
        $cake="с черникой"

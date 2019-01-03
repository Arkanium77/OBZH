#==========================================
# Определение персонажей игры.
#==========================================
define han = Character('Ханна', color="#F984EF")
define jar = Character('Джаред', color="#AA6651")

define mom = Character('Мама', color="#DEAA88")
define dad = Character('Папа', color="#4c2a1f")
define mai = Character('Мэй', color="#D53E07")

define luk = Character('Люк', color="#282828")
define car = Character('Машина', color="#000000")
#=============================================================
#Объявление изображений
#=============================================================
init:
#                         ПЕРСОНАЖИ                           #
#emoji:
#    ace (торжество)
#    ang (angry - злость)
#    dou (от Doubt - сомнение)
#    exc (от Excitement - волнение)
#    sad  (грусть)
#    smi (smile - улыбка)
#    std (standart - обычный)

    #Ханна
    image han ang= "/images/sprites/han/ang.png"
    image han cry= "/images/sprites/han/cry.png"
    image han dou= "/images/sprites/han/dou.png"
    image han exc= "/images/sprites/han/exc.png"
    image han sad= "/images/sprites/han/sad.png"
    image han smi= "/images/sprites/han/smi.png"
    image han std= "/images/sprites/han/std.png"

    image han sad1= "/images/sprites/han/sad1.png"

    #Джаред
    image jar ang= "/images/sprites/jar/ang.png"
    image jar blu= "/images/sprites/jar/blu.png"
    image jar dou= "/images/sprites/jar/dou.png"
    image jar exc= "/images/sprites/jar/exc.png"
    image jar sad= "/images/sprites/jar/sad.png"
    image jar smi= "/images/sprites/jar/smi.png"
    image jar std= "/images/sprites/jar/std.png"

    image jar sad1= "/images/sprites/jar/sad1.png"
    image jar std1= "/images/sprites/jar/std1.png"

    image jar pyj dou = "/images/sprites/jar/pyj/dou.png"
    image jar pyj std = "/images/sprites/jar/pyj/std.png"
    image jar pyj smi = "/images/sprites/jar/pyj/smi.png"
    image jar pyj exc = "/images/sprites/jar/pyj/exc.png"

    #Папа
    image dad smi= "/images/sprites/dad/smi.png"
    image dad std= "/images/sprites/dad/std.png"

    #Мама
    image mom ang= "/images/sprites/mom/ang.png"
    image mom smi= "/images/sprites/mom/smi.png"
    image mom std= "/images/sprites/mom/std.png"

    #Мэй
    image mai ang= "/images/sprites/mai/ang.png"
    image mai cry= "/images/sprites/mai/cry.png"
    image mai dou= "/images/sprites/mai/dou.png"
    image mai exc= "/images/sprites/mai/exc.png"
    image mai sad= "/images/sprites/mai/sad.png"
    image mai smi= "/images/sprites/mai/smi.png"
    image mai std= "/images/sprites/mai/std.png"

    image mai smi1= "/images/sprites/mai/smi1.png"


    image car car= "/images/sprites/car.png"


#                         ФОНЫ                           #

#day:
#    m   (morning - утро)
#    e   (evening - вечер)
#    n   (night - ночь)

    #Комната
    image bg room_j= "/images/bg/boys_room/room_j.jpg"
    image bg room_j_n= "/images/bg/boys_room/room_j_n.jpg"
    image bg hall= "/images/bg/boys_room/boyshall.jpg"
    image bg kitchen= "/images/bg/kitchen.jpg"
    image bg cafe= "/images/bg/cafe.jpg"

    image bg street= "/images/bg/street/street.jpg"
    image bg black= "/images/bg/black.jpg"
    image ds="/images/bg/ds.png"
    ###################
    #     ЗВУКИ       #
    ###################
    $ds_sound="sounds/sound/ds.mp3"#pm.mp3, pm1.mp3, pm2.mp3
    $car="sounds/sound/car.mp3"#pm.mp3, pm1.mp3, pm2.mp3
    $mes="Ненаписанное сообщение."

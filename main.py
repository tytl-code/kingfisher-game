@namespace
class SpriteKind:
    Teleporter = SpriteKind.create()
    Teleporter2 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Lvl, Boss2, myEnemy, statusbar, Boss3, MyEnemy2, Spinman
    if Lvl == 0:
        mySprite.set_position(8, 130)
        tiles.set_current_tilemap(tilemap("""
            level4
        """))
        info.set_life(3)
        Lvl = 1
        mySprite2.set_position(130, -1)
        sprites.destroy(mySprite5)
    else:
        if Lvl == 1:
            mySprite2.set_image(img("""
                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
            """))
            mySprite.set_position(110, 200)
            tiles.set_current_tilemap(tilemap("""
                level5
            """))
            Boss2 += 1
            Lvl = 2
            if Boss2 == 1:
                myEnemy = sprites.create(assets.image("""
                    5
                """), SpriteKind.enemy)
                statusbar = statusbars.create(20, 4, StatusBarKind.health)
                statusbar.set_color(2, 1)
                statusbar.set_label("HP")
                statusbar.max = 20
                statusbar.attach_to_sprite(myEnemy)
                myEnemy.follow(mySprite)
        else:
            if Lvl == 2:
                mySprite2.set_image(assets.image("""
                    b
                """))
                tiles.set_current_tilemap(tilemap("""
                    level12
                """))
                mySprite.set_position(120, 20)
                mySprite2.set_position(250, 130)
                Boss2 = 0
                Lvl = 3
            else:
                if Lvl == 3:
                    Boss3 = 1
                    mySprite2.set_image(assets.image("""
                        b
                    """))
                    tiles.set_current_tilemap(tilemap("""
                        level17
                    """))
                    mySprite.set_position(8, 130)
                    mySprite2.set_position(260, 130)
                    if Boss3 == 1:
                        info.set_life(3)
                        MyEnemy2 = sprites.create(assets.image("""
                            myImage2
                        """), SpriteKind.enemy)
                        MyEnemy2.follow(mySprite)
                        statusbar = statusbars.create(20, 4, StatusBarKind.health)
                        statusbar.attach_to_sprite(MyEnemy2)
                        statusbar.set_color(7, 1)
                        statusbar.set_label("HP")
                        statusbar.max = 25
                        Lvl = 4
                elif Lvl == 4:
                    tiles.set_current_tilemap(tilemap("""
                        level14
                    """))
                    mySprite2.set_position(130, 250)
                    mySprite.set_position(220, 130)
                    Lvl = 5
                elif Lvl == 5:
                    mySprite.set_position(110, 200)
                    mySprite.set_position(110, 20)
                    tiles.set_current_tilemap(tilemap("""
                        level18
                    """))
                    Spinman = sprites.create(img("""
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                                                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
                        """),
                        SpriteKind.enemy)
                    mySprite2.set_image(img("""
                        . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . .
                    """))
                    animation.run_image_animation(Spinman, assets.animation("""
                        myAnim
                    """), 50, True)
                    scaling.scale_to_pixels(Spinman, 20, ScaleDirection.HORIZONTALLY, ScaleAnchor.MIDDLE)
                    scaling.scale_to_pixels(Spinman, 20, ScaleDirection.VERTICALLY, ScaleAnchor.MIDDLE)
                else:
                    pass
sprites.on_overlap(SpriteKind.player, SpriteKind.Teleporter, on_on_overlap)

def on_on_zero(status):
    global mySprite5, mySprite2
    if Boss2 == 1:
        sprites.destroy(myEnemy)
        tiles.set_current_tilemap(tilemap("""
            level10
        """))
        mySprite2.set_position(130, 250)
        mySprite5 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        mySprite5.set_position(120, 230)
        mySprite2.set_image(img("""
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
        """))
    elif Boss3 == 1:
        tiles.set_current_tilemap(tilemap("""
            level
        """))
        mySprite2.set_image(img("""
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
        """))
        sprites.destroy(MyEnemy2)
        mySprite2.set_position(0, 120)
    elif False:
        pass
    else:
        sprites.destroy(mySprite3)
        tiles.set_current_tilemap(tilemap("""
            level0
        """))
        mySprite5 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        info.change_score_by(3)
        mySprite2 = sprites.create(img("""
                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
            """),
            SpriteKind.Teleporter)
        mySprite5.set_position(210, 120)
        mySprite2.set_position(240, 120)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_on_overlap2(sprite2, otherSprite2):
    statusbar.value += -1
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    if True:
        info.change_life_by(-1)
        pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

Right = 0
Up = 0
Down = 0
projectile: Sprite = None
Left = 0
Spinman: Sprite = None
MyEnemy2: Sprite = None
myEnemy: Sprite = None
mySprite5: Sprite = None
mySprite2: Sprite = None
Boss3 = 0
Boss2 = 0
Lvl = 0
mySprite3: Sprite = None
statusbar: StatusBarSprite = None
mySprite: Sprite = None
scene.set_background_color(6)
game.set_dialog_text_color(6)
game.set_dialog_frame(assets.image("""
    b
"""))
game.show_long_text("  The Kingfisher", DialogLayout.CENTER)
info.set_score(0)
info.set_life(3)
mySprite = sprites.create(assets.image("""
    s
"""), SpriteKind.player)
statusbar = statusbars.create(20, 2, StatusBarKind.health)
mySprite3 = sprites.create(assets.image("""
    f
"""), SpriteKind.enemy)
mySprite.set_stay_in_screen(True)
tiles.set_current_tilemap(tilemap("""
    level3
"""))
scene.set_background_color(6)
scene.camera_follow_sprite(mySprite)
Lvl = 0
mySprite3.set_position(-160, -160)
Boss2 = 0
statusbar.set_label("HP", 10)
statusbar.attach_to_sprite(mySprite3)
statusbar.set_color(10, 1)
statusbar.max = 4
Boss3 = 0

def on_forever():
    global projectile
    if controller.A.is_pressed():
        if Left:
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 1 . . . . . . . . 
                                    . . . . . . 1 6 1 . . . . . . . 
                                    . . . . . . . 1 . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                mySprite,
                -1000,
                0)
            pause(200)
        else:
            if Down == 1:
                projectile = sprites.create_projectile_from_sprite(img("""
                        . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . 1 . . . . . . . . 
                                            . . . . . . 1 6 1 . . . . . . . 
                                            . . . . . . . 1 . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . .
                    """),
                    mySprite,
                    0,
                    1000)
                pause(200)
            else:
                if Up == 1:
                    projectile = sprites.create_projectile_from_sprite(img("""
                            . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . 1 . . . . . . . . 
                                                    . . . . . . 1 6 1 . . . . . . . 
                                                    . . . . . . . 1 . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . . 
                                                    . . . . . . . . . . . . . . . .
                        """),
                        mySprite,
                        0,
                        -1000)
                    pause(200)
                else:
                    if Right == 1:
                        projectile = sprites.create_projectile_from_sprite(img("""
                                . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . 1 . . . . . . . . 
                                                            . . . . . . 1 6 1 . . . . . . . 
                                                            . . . . . . . 1 . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . . 
                                                            . . . . . . . . . . . . . . . .
                            """),
                            mySprite,
                            1000,
                            0)
                        pause(200)
forever(on_forever)

def on_forever2():
    music.play(music.create_song(hex("""
            00780004080200
        """)),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever2)

def on_forever3():
    global Up, Down, Right, Left
    if controller.up.is_pressed():
        mySprite.set_image(assets.image("""
            myImage
        """))
        mySprite.y += -3
        Up = 1
        Down = 0
        Right = 0
        Left = 0
forever(on_forever3)

def on_forever4():
    global Left, Up, Right, Down
    mySprite3.follow(mySprite)
    if controller.left.is_pressed():
        mySprite.set_image(assets.image("""
            myImage1
        """))
        mySprite.x += -3
        Left = 1
        Up = 0
        Right = 0
        Down = 0
forever(on_forever4)

def on_forever5():
    global Right, Down, Up, Left
    if controller.right.is_pressed():
        mySprite.set_image(assets.image("""
            s
        """))
        mySprite.x += 3
        Right = 1
        Down = 0
        Up = 0
        Left = 0
forever(on_forever5)

def on_forever6():
    global Down, Up, Right, Left
    if controller.down.is_pressed():
        mySprite.set_image(assets.image("""
            myImage0
        """))
        mySprite.y += 3
        Down = 1
        Up = 0
        Right = 0
        Left = 0
forever(on_forever6)

def on_forever7():
    controller.move_sprite(mySprite)
forever(on_forever7)

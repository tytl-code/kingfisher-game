@namespace
class SpriteKind:
    Teleporter = SpriteKind.create()
    Teleporter2 = SpriteKind.create()
    decor = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Lvl, Boss2, myEnemy, statusbar, Boss3, MyEnemy2, Spinman, Spin, Portal
    if Lvl == 0:
        mySprite.set_position(8, 130)
        tiles.set_current_tilemap(tilemap("""
            level4
        """))
        info.set_life(3)
        Lvl = 1
        mySprite2.set_position(130, -1)
        sprites.destroy(mySprite5)
    elif Lvl == 1:
        mySprite2.set_image(assets.image("""
            myImage3
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
    elif Lvl == 2:
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
        tiles.set_current_tilemap(tilemap("""
            level12
        """))
        mySprite.set_position(120, 20)
        mySprite2.set_position(250, 130)
        Boss2 = 0
        Lvl = 3
    elif Lvl == 3:
        Boss3 = 1
        mySprite2.set_image(assets.image("""
            myImage3
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
        info.set_life(3)
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
        statusbar = statusbars.create(20, 4, StatusBarKind.health)
        statusbar.attach_to_sprite(Spinman)
        statusbar.max = 4
        Spinman.set_velocity(120, 120)
        Spinman.set_bounce_on_wall(True)
        statusbar.set_color(8, 1, 9)
        statusbar.set_label("HP")
        Spin = 1
        Lvl = 6
    elif Lvl == 6:
        tiles.set_current_tilemap(tilemap("""
            level23
        """))
        mySprite.set_position(120, 200)
        mySprite2.set_position(200, 120)
        Portal = sprites.create(img("""
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
            SpriteKind.decor)
        animation.run_image_animation(Portal, assets.animation("""
            myAnim1
        """), 200, True)
        Portal.set_position(135, 127)
        scaling.scale_to_pixels(Portal, 25, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    else:
        pass
sprites.on_overlap(SpriteKind.player, SpriteKind.Teleporter, on_on_overlap)

def on_overlap_tile(sprite2, location):
    global Camera, FinalBoss, statusbar, cool_delete, Boom_Boom
    scene.set_background_image(assets.image("""
        myImage6
    """))
    tiles.set_current_tilemap(tilemap("""
        level28
    """))
    Camera = sprites.create(img("""
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
        SpriteKind.decor)
    Camera.set_image(img("""
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
    sprites.destroy(Portal)
    sprites.destroy(mySprite2)
    FinalBoss = 1
    statusbar = statusbars.create(100, 4, StatusBarKind.health)
    statusbar.position_direction(CollisionDirection.TOP)
    scene.camera_follow_sprite(Camera)
    if FinalBoss == 1:
        cool_delete = 0
        while FinalBoss == 1:
            scene.set_background_image(assets.image("""
                myImage10
            """))
            pause(100)
            cool_delete += 1
            scene.set_background_image(assets.image("""
                myImage6
            """))
            Boom_Boom = sprites.create(assets.image("""
                myImage9
            """), SpriteKind.projectile)
            Boom_Boom.set_position(randint(120, 300), randint(127, 200))
            Boom_Boom.follow(mySprite)
            pause(500)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile19
    """),
    on_overlap_tile)

def on_on_overlap2(sprite3, otherSprite2):
    sprites.destroy(Boom_Boom)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.projectile, on_on_overlap2)

def on_on_zero(status):
    global mySprite5, Boss3, mySprite2
    if Boss2 == 1:
        sprites.destroy(myEnemy, effects.trail, 500)
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
        sprites.destroy(MyEnemy2, effects.spray, 500)
        mySprite2.set_position(0, 120)
        Boss3 = 0
    elif Spin == 1:
        sprites.destroy(Spinman, effects.spray, 500)
        tiles.set_current_tilemap(tilemap("""
            level20
        """))
        mySprite2.set_position(90, 15)
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
    else:
        sprites.destroy(mySprite3, effects.rings, 500)
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

def on_on_overlap3(sprite32, otherSprite3):
    if True:
        info.change_life_by(-1)
        pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

def on_overlap_tile2(sprite4, location2):
    global Boom_Boom, FinalBoss, statusbar
    scene.set_background_image(assets.image("""
        myImage6
    """))
    tiles.set_current_tilemap(tilemap("""
        level51
    """))
    scene.camera_follow_sprite(mySprite2)
    mySprite2.set_image(assets.image("""
        myImage7
    """))
    Boom_Boom = sprites.create(assets.image("""
        myImage9
    """), SpriteKind.projectile)
    FinalBoss = 1
    statusbar = statusbars.create(100, 4, StatusBarKind.health)
    statusbar.position_direction(CollisionDirection.TOP)
    if FinalBoss == 1:
        while FinalBoss == 1:
            scene.set_background_image(assets.image("""
                myImage10
            """))
            pause(500)
            scene.set_background_image(assets.image("""
                myImage6
            """))
            Boom_Boom.set_position(0, 127)
            pause(500)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile20
    """),
    on_overlap_tile2)

def on_on_overlap4(sprite22, otherSprite22):
    statusbar.value += -1
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap4)

def on_combos_attach_combo():
    global ifyfifrirfryfriyfir, ifrif
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    sprites.destroy_all_sprites_of_kind(SpriteKind.status_bar)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Teleporter)
    tiles.set_current_tilemap(tilemap("""
        level25
    """))
    ifyfifrirfryfriyfir = sprites.create(img("""
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
        SpriteKind.player)
    animation.run_image_animation(ifyfifrirfryfriyfir,
        assets.animation("""
            myAnim0
        """),
        100,
        True)
    ifrif += 1
controller.combos.attach_combo("abababa", on_combos_attach_combo)

projectile: Sprite = None
Left = 0
Right = 0
Down = 0
Up = 0
ifyfifrirfryfriyfir: Sprite = None
Boom_Boom: Sprite = None
cool_delete = 0
FinalBoss = 0
Camera: Sprite = None
Portal: Sprite = None
Spin = 0
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
game.show_long_text("  The Kingfisher's     Dimensional Adventures",
    DialogLayout.CENTER)
ifrif = 0
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
    if ifrif == 1:
        if controller.A.is_pressed():
            game.game_over(True)
forever(on_forever)

def on_forever2():
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
forever(on_forever2)

def on_forever3():
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
forever(on_forever3)

def on_forever4():
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
forever(on_forever4)

def on_forever5():
    controller.move_sprite(mySprite)
forever(on_forever5)

def on_forever6():
    global projectile
    if controller.A.is_pressed():
        if Left:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                t
            """), mySprite, -1000, 0)
            music.play(music.melody_playable(music.pew_pew),
                music.PlaybackMode.IN_BACKGROUND)
            pause(200)
        elif Down == 1:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                ty
            """), mySprite, 0, 1000)
            music.play(music.melody_playable(music.pew_pew),
                music.PlaybackMode.IN_BACKGROUND)
            pause(200)
        elif Up == 1:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                tyu
            """), mySprite, 0, -1000)
            music.play(music.melody_playable(music.pew_pew),
                music.PlaybackMode.IN_BACKGROUND)
            pause(200)
        elif Right == 1:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                tyui
            """), mySprite, 1000, 0)
            music.play(music.melody_playable(music.pew_pew),
                music.PlaybackMode.IN_BACKGROUND)
            pause(200)
forever(on_forever6)

def on_forever7():
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
forever(on_forever7)

def on_forever8():
    music.play(music.string_playable("A E F G F E D F ", 90),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever8)

def on_forever9():
    music.play(music.create_song(assets.song("""
            song
        """)),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever9)

def on_forever10():
    music.set_volume(255)
    game.set_game_over_playable(False, music.melody_playable(music.wawawawaa), False)
forever(on_forever10)

def on_forever11():
    if FinalBoss == 1:
        pause(5000)
        sprites.destroy(Boom_Boom, effects.confetti, 500)
forever(on_forever11)

def on_forever12():
    if True:
        pass
forever(on_forever12)

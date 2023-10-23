namespace SpriteKind {
    export const Teleporter = SpriteKind.create()
    export const Teleporter2 = SpriteKind.create()
    export const decor = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Teleporter, function (sprite, otherSprite) {
    if (Lvl == 0) {
        mySprite.setPosition(8, 130)
        tiles.setCurrentTilemap(tilemap`level4`)
        info.setLife(3)
        Lvl = 1
        mySprite2.setPosition(130, -1)
        sprites.destroy(mySprite5)
    } else if (Lvl == 1) {
        mySprite2.setImage(assets.image`myImage3`)
        mySprite.setPosition(110, 200)
        tiles.setCurrentTilemap(tilemap`level5`)
        Boss2 += 1
        Lvl = 2
        if (Boss2 == 1) {
            myEnemy = sprites.create(assets.image`5`, SpriteKind.Enemy)
            statusbar = statusbars.create(20, 4, StatusBarKind.Health)
            statusbar.setColor(2, 1)
            statusbar.setLabel("HP")
            statusbar.max = 20
            statusbar.attachToSprite(myEnemy)
            myEnemy.follow(mySprite)
        }
    } else if (Lvl == 2) {
        mySprite2.setImage(img`
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
            `)
        tiles.setCurrentTilemap(tilemap`level12`)
        mySprite.setPosition(120, 20)
        mySprite2.setPosition(250, 130)
        Boss2 = 0
        Lvl = 3
    } else if (Lvl == 3) {
        Boss3 = 1
        mySprite2.setImage(assets.image`myImage3`)
        tiles.setCurrentTilemap(tilemap`level17`)
        mySprite.setPosition(8, 130)
        mySprite2.setPosition(260, 130)
        if (Boss3 == 1) {
            info.setLife(3)
            MyEnemy2 = sprites.create(assets.image`myImage2`, SpriteKind.Enemy)
            MyEnemy2.follow(mySprite)
            statusbar = statusbars.create(20, 4, StatusBarKind.Health)
            statusbar.attachToSprite(MyEnemy2)
            statusbar.setColor(7, 1)
            statusbar.setLabel("HP")
            statusbar.max = 25
            Lvl = 4
        }
    } else if (Lvl == 4) {
        tiles.setCurrentTilemap(tilemap`level14`)
        mySprite2.setPosition(130, 250)
        mySprite.setPosition(220, 130)
        Lvl = 5
    } else if (Lvl == 5) {
        mySprite.setPosition(110, 200)
        mySprite.setPosition(110, 20)
        tiles.setCurrentTilemap(tilemap`level18`)
        info.setLife(3)
        Spinman = sprites.create(img`
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
            `, SpriteKind.Enemy)
        mySprite2.setImage(img`
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
            `)
        animation.runImageAnimation(
        Spinman,
        assets.animation`myAnim`,
        50,
        true
        )
        scaling.scaleToPixels(Spinman, 20, ScaleDirection.Horizontally, ScaleAnchor.Middle)
        scaling.scaleToPixels(Spinman, 20, ScaleDirection.Vertically, ScaleAnchor.Middle)
        statusbar = statusbars.create(20, 4, StatusBarKind.Health)
        statusbar.attachToSprite(Spinman)
        statusbar.max = 4
        Spinman.setVelocity(120, 120)
        Spinman.setBounceOnWall(true)
        statusbar.setColor(8, 1, 9)
        statusbar.setLabel("HP")
        Spin = 1
        Lvl = 6
    } else if (Lvl == 6) {
        tiles.setCurrentTilemap(tilemap`level23`)
        mySprite.setPosition(120, 200)
        mySprite2.setPosition(200, 120)
        Portal = sprites.create(img`
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
            `, SpriteKind.decor)
        animation.runImageAnimation(
        Portal,
        assets.animation`myAnim1`,
        200,
        true
        )
        Portal.setPosition(135, 127)
        scaling.scaleToPixels(Portal, 25, ScaleDirection.Uniformly, ScaleAnchor.Middle)
    } else {
    	
    }
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    if (Boss2 == 1) {
        sprites.destroy(myEnemy)
        tiles.setCurrentTilemap(tilemap`level10`)
        mySprite2.setPosition(130, 250)
        mySprite5 = sprites.create(img`
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
            `, SpriteKind.Food)
        mySprite5.setPosition(120, 230)
        mySprite2.setImage(img`
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
            `)
    } else if (Boss3 == 1) {
        tiles.setCurrentTilemap(tilemap`level`)
        mySprite2.setImage(img`
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
            `)
        sprites.destroy(MyEnemy2)
        mySprite2.setPosition(0, 120)
        Boss3 = 0
    } else if (Spin == 1) {
        sprites.destroy(Spinman)
        tiles.setCurrentTilemap(tilemap`level20`)
        mySprite2.setPosition(90, 15)
        mySprite2.setImage(img`
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
            `)
    } else {
        sprites.destroy(mySprite3)
        tiles.setCurrentTilemap(tilemap`level0`)
        mySprite5 = sprites.create(img`
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
            `, SpriteKind.Food)
        info.changeScoreBy(3)
        mySprite2 = sprites.create(img`
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
            `, SpriteKind.Teleporter)
        mySprite5.setPosition(210, 120)
        mySprite2.setPosition(240, 120)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    if (true) {
        info.changeLifeBy(-1)
        pause(1000)
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    statusbar.value += -1
    info.changeScoreBy(1)
})
controller.combos.attachCombo("abababa", function () {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    sprites.destroyAllSpritesOfKind(SpriteKind.StatusBar)
    sprites.destroyAllSpritesOfKind(SpriteKind.Teleporter)
    tiles.setCurrentTilemap(tilemap`level25`)
    ifyfifrirfryfriyfir = sprites.create(img`
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
        `, SpriteKind.Player)
    animation.runImageAnimation(
    ifyfifrirfryfriyfir,
    assets.animation`myAnim0`,
    100,
    true
    )
    ifrif += 1
})
let projectile: Sprite = null
let Left = 0
let Right = 0
let Down = 0
let Up = 0
let ifyfifrirfryfriyfir: Sprite = null
let Portal: Sprite = null
let Spin = 0
let Spinman: Sprite = null
let MyEnemy2: Sprite = null
let myEnemy: Sprite = null
let mySprite5: Sprite = null
let mySprite2: Sprite = null
let Boss3 = 0
let Boss2 = 0
let Lvl = 0
let mySprite3: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite: Sprite = null
scene.setBackgroundColor(6)
game.setDialogTextColor(6)
game.setDialogFrame(assets.image`b`)
game.showLongText("  The Kingfisher", DialogLayout.Center)
let ifrif = 0
info.setScore(0)
info.setLife(3)
mySprite = sprites.create(assets.image`s`, SpriteKind.Player)
statusbar = statusbars.create(20, 2, StatusBarKind.Health)
mySprite3 = sprites.create(assets.image`f`, SpriteKind.Enemy)
mySprite.setStayInScreen(true)
tiles.setCurrentTilemap(tilemap`level3`)
scene.setBackgroundColor(6)
scene.cameraFollowSprite(mySprite)
Lvl = 0
mySprite3.setPosition(-160, -160)
Boss2 = 0
statusbar.setLabel("HP", 10)
statusbar.attachToSprite(mySprite3)
statusbar.setColor(10, 1)
statusbar.max = 4
Boss3 = 0
forever(function () {
    if (ifrif == 1) {
    	
    }
})
forever(function () {
    if (controller.up.isPressed()) {
        mySprite.setImage(assets.image`myImage`)
        mySprite.y += -3
        Up = 1
        Down = 0
        Right = 0
        Left = 0
    }
})
forever(function () {
    mySprite3.follow(mySprite)
    if (controller.left.isPressed()) {
        mySprite.setImage(assets.image`myImage1`)
        mySprite.x += -3
        Left = 1
        Up = 0
        Right = 0
        Down = 0
    }
})
forever(function () {
    light.setMode(NeoPixelMode.RGB)
    if (controller.right.isPressed()) {
        mySprite.setImage(assets.image`s`)
        mySprite.x += 3
        Right = 1
        Down = 0
        Up = 0
        Left = 0
    }
})
forever(function () {
    controller.moveSprite(mySprite)
    music.play(music.createSong(hex`0078000408020405001c000f0a006400f4010a00000400000000000000000000000000000000021e0004000800011d14001800012020002400011d28002c00012434003800011d07001c00020a006400f4016400000400000000000000000000000000000000032a000400080001240c001000012a10001400012718001c00012428002c00012738003c0001203c004000012708001c000e050046006603320000040a002d0000006400140001320002010002360000000400012708000c00012410001400012a18001c00012720002400012428002c00012a30003400012738003c0001243c004000012a09010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800360004000500010a0800090002010a1000110001011800190003010a0b200021000201082800290001013000310002010a3800390002010a`), music.PlaybackMode.UntilDone)
})
forever(function () {
    if (controller.A.isPressed()) {
        if (Left) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, mySprite, -1000, 0)
            music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
            pause(200)
        } else if (Down == 1) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, mySprite, 0, 1000)
            music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
            pause(200)
        } else if (Up == 1) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, mySprite, 0, -1000)
            music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
            pause(200)
        } else if (Right == 1) {
            projectile = sprites.createProjectileFromSprite(img`
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
                `, mySprite, 1000, 0)
            music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.InBackground)
            pause(200)
        }
    }
})
forever(function () {
    if (controller.down.isPressed()) {
        mySprite.setImage(assets.image`myImage0`)
        mySprite.y += 3
        Down = 1
        Up = 0
        Right = 0
        Left = 0
    }
})
forever(function () {
    music.play(music.createSong(hex`00780004080200`), music.PlaybackMode.UntilDone)
})
forever(function () {
    if (true) {
    	
    }
})

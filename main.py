@namespace
class SpriteKind:
    tipus_conversio_2 = SpriteKind.create()
    Canvi = SpriteKind.create()
    Sortida = SpriteKind.create()
    tipus_conversio_1 = SpriteKind.create()

def on_on_overlap(sprite2, otherSprite2):
    global tipus_conversio
    if game.ask("Entrar a la conversió?"):
        tipus_conversio = 1
        preparar_mercat()
sprites.on_overlap(SpriteKind.player,
    SpriteKind.tipus_conversio_1,
    on_on_overlap)

def on_on_overlap2(sprite32, otherSprite3):
    if game.ask("Vols sortir?"):
        preparar_home()
sprites.on_overlap(SpriteKind.player, SpriteKind.Sortida, on_on_overlap2)

def preparar_mercat():
    global patata, gallina, cabra, ou, cavall, mySprite
    scene.set_background_image(img("""
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88f888fc6fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff888fc88ffff888fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888f8888fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffff88ff888888fff8fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff888888888fff868ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffff8888888ff868ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccfcffffffffff88888888888ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccffffffffff888888fffffffcffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccccccccccfffffff88888ffff888fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccc77eeeeeeeefff88ffffffffff8fffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccc777eeeeeeeeeeffffffffffffffff8ffffffffffffffffffccffffffffffffffffffffffffffff
        ffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffccccccccccccccc77777eeeeeeeeeeefffccfffffffffffffffffffffffffffffccffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffcffffffffffffffffffffffffffffcccffcccccccccccccccc777777eeeeeeeeeeeeeeeefffffcfffffffffffffffffffffccfffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffccccccccccccccccccccccccccccc7777777eccccccccccccccccccccccfffffffffffffffffcfffcffffcfffffffffffffffffffffff
        fffffffffffffffffffffffffffcccffffffffffffffcccccccccccccccccccccccccccccccccc777777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffcccffffcfffffffffffffffffffffff
        fffffffffffffffffffffffffcfccccfffffffffccccccccccccccccccccccccccccccccccc7777bb777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffc7cfccfcffcffffffffffffffffffff
        ffffffffffffffffffffffffffffcccccfffffffccccccccccccccccccccccccccccccccccc777bbbb77777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffcccccffcfcccfccfffffffffffffffffff
        fffffffffffffffffffffffcffffffffffffffffccccccccccccccccccccccccccccccccc777777bb77777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffccfccfffffffffffffffffffffff
        ffffffffffffffffffffccfffcccfffffffffffccc77eeeeeeeeeeeeeeeeeeeeeeee7e777777777777777777777eeeeeeeeeeeeeeeeeeeeeeee77eeffffffffffff77fffeeeffefffffffffffffffff
        fffffffffffffffffffcccffc7cffffffffffffccc77e7eeeeeeeeeeeeeeeeeee7ee7e7777777777777777777777eeeeeeeeeeeeeeeeeeeeeee7777ffffffffffffe77ffeeeefffffffffffffffffff
        ffffffffffffffffffffcffff7ffffffffffffcccc77777eeeeeeeeeeeeeeeeee777777777777777777777777777ee7ee77eeeeeeeeeeeee7e77777effffffffffff77fffcccfffffffffffffffffff
        fffffffffffffffcffffcfccffffffffffffcccccc777777eee77eeeeeeee777777777777777777777777777777777777777eeeee77eeee77777777eeeffffffffffff77fcfcfffffffffffffffffff
        fffffffffffffffffccffffffffffffffffccccc77777777777777ee7777777777777777777777777777777777777777777777777777ee777dd7777eeeeffffffffffffffffeeffffffffffffffffff
        fffffffffffffffffccffffffffffffffffcccccc77777777777777777777777777777777777777777777777777777777777777777777777bddb77eeeeeffffffffffffffffccffffffffffffffffff
        fffffffffffffffffffffffffffffffffffccccc77777777777777777777777777777777777777777777777777777777777777777777777777b7777eeeeefffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffcccccc77777777777777777777777777777777bbbbbbbbbbbbbb777777777777777777777777777777777eeeeeeffcfffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffccccccc7777777777777777777777777777777bddddddddddddddb77777777777777777777777777777777eeeeeeffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffcccccccc7777777777777777777777777777777bddddddddddddddb777777777777777777777777777777777eeeeeeeffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffcfffffffcccccccccc7777777777777777777777777777777bddddddddddddddb777777777777777777777777777777777eeeeeeeefffffffffffffffffffffffffffffff
        ffffffffffffffffffffffccccfffccccccccccc7777777777777777777777777777777bddddddddddddddb777777777777777777777777777777777eeeeeeeeefffeeeeeffffffffffffffffffffff
        fffffffffffffffffffffccccccccccccccccccc7777777777777777777777777777777bddddddddddddddb777777777777777777777777777777777eeeeeeeeeeeeeeeeeefffffffffffffffffffff
        ffffffffffffffffffffcccccccccceeeeeeee777777777777777777777777777777777bddddddddddddddb777777777777777777777777777777777777eeeeeeeeeeeeeeefffffffffffffffffffff
        ffffffffffffffffffccccccccccceeeeeeeeee7777777777777bb77777777777777777bddddddddddddddb777777777777777777b77777777777777777eeeeeeeee7eeeeeeeeffffffffffffffffff
        ffffffffffffffffffcccccccccceeeeeeeeeee777777777777bdde7777777777777777bddddddddddddddb7777777777777777ebdb7777777777777777eeeeeeeebe7eeeeeeeffffffffffffffffff
        ffffffffffffffffffcccccccccccceeeeee77777777777777bddddb777777777777777bddddddddddddddb7777777777777777bdddb777777777777777ee77eeeee7eeeeeeeeffffffffffffffffff
        fffffffffffffffffccccccccccccccccccc7777777777777bdddddb777777777777777bddddddddddddddb777777777777777ddddddb777777777777777777eeeeeeeeeeeeeeffffffffffffffffff
        fffccfffffffffffffccccccccccccccccc7777777777777bdddddddb77777777777777bddddddddddddddb7777777777777ebdddddddb77777777777777777eeeeeeeeeeeeeffffffffffffffcffff
        cffccff77ffffffffffcccccccccccc77e7777777777777bdddddddddb7777777777777bddddddddddddddb7777777777777bdddddddddb7777777777777777eeeeeeeeeeeeffffffffff77efeeffee
        effffff7ef7fffffffffeeeeeeeeeee777777777777777bdddddddddddbb77777777777bddddddddddddddb777777777777bdddddddddddb777777777777777eeeeeeeeeeeeffffffff7ff7ffffffcc
        fffffffcf77fffffffffccccccccccc77777777777777bbddddddddddddbe7777777777bddddddddddddddb7777777777ebdddddddddddddb777777777777777eeeeeeeeeeeffffffffe7feffffffff
        ffefff7777fff77ffffeeeeeeeeeeee7777777777777bddddddddddddddddb777777777bddddddddddddddb7777777777bdddddddddddddddbe77777777777777eeeeeeeeeefffff7fff7e77fffefff
        fe7fffe7effffefffffeeeeeee7e7e7777777777777bddddddddddddddddddb77777777ebbbbeeebbbbbeee77777777ebdddddddddddddddddb777777777777777777eeeeeefffff7cffff7cffc7cfc
        ff7ffff7ffffffffffffccccc77777777777777777bdddddddddddddddddddb777777777eeeeeeeee77eee777777777bdddddddddddddddddddb77777777777777777777eeffffffffffffeffff7fff
        ffffff777fffffffffffe77777777777777777777bdddddddddddddddddddddbe77777777777777777777777777777bdddddddddddddddddddddb77777777777777777777efffffffffffe77fffffff
        fe7fff777fffffffffffe777777777777777777777bdddddddddddddddddddb77777777777777777777777777777777bdddddddddddddddddddb7777777777777777777777fffffffffffe77fffeeff
        f777ef77777fffffffff7777777777777777777777ebdddddddddddddddddb777777777777777777777777777777777ebdddddddddddddddddbe7777777777777777777777effffffff77e77fe777ef
        f77ffffe777efffffffe777b7777777775577777777ebdddddddddddddddbe7777777777777777777777777777777777ebdddddddddddddddbe777777777777777777777777ffffffcf7777ffff77ff
        f77fffff777effffffff777777777777755777777777ebbddddddddddddbe777777777777777777777777777777777777ebdddddddddddddbe777777777777777777777777effffff7ee777ffff77ff
        ff77eee7fff7ffffffffe777777777777757777777777ebdddddddddddb777777777777777777777777777777777777777ebdddddddddddbe7777777777777777777777777ffffffff7fff7e7777efe
        ffe7e77fff77ffffffffe7777777777777777777777777ebbddddddddb777777777777777777777777777777777777777777bdddddddddbe77777777777777777777777777ffffffff77fff77e77fff
        fefffe7fff7effffffffc77777777777777777777777777eebddddddbe777777777777777777777777777777777777777777ebdddddddbe777777777777777777777777777ffffffffe7fff7effffef
        e7fffffffffffffffffcc777777777777777777777777777eedddddbe77777777777777777777777777777777777777777777ebdddddbe777777777777777777777777777777ffffffffffffffffc7f
        c77ffffffffffffffcccc7777777777777777777777777777ebdddbe7777777777777777777777777777777777777777777777ebdddbe77777777777777777777777777777777ffffffffffffff7777
        f7777ff7fffffffffcccc77777777777777777777777777777ebdbe777777777777777777777777777777777777777777777777ebdbe777777777777777777777777777777777fffffffff7ffe777ff
        fe777ffffffffffffccc7777777777777777777777777777777eee77777777777777777777777777777777777777777777777777ebe777777777777777777777777777777777efffffffffeff777eff
        ff777ffffffffffffeee777777777777777777777777777b777777777777777777777777777777777777777777777777777777777e77777777777777777777777777777777777ffffffffffff777cff
        ffffffffffffffffccccc777777777777777777777777bddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eefffffffffffffffff
        fffffffffffffffcccccc7777777777777777777777777dd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eeeeffffffffffffffff
        fffffffffffffffcccccc7777777bbbbbbbbbbbbbbb7777d7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eeeeffffffffffffffff
        fffffffffffffffccccccc777777ddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eeeeffffffffffffffff
        ffffffffffffffcccccccc777777bdddddddddddddde777777777777777777777777777777777777777777777777777777777777777777777777eeeeeeeeeeeee7777777777eeeeefffffffffffffff
        fffffffffffccccccccccc777777ddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777777777ddddddddddddddde777777777eeeeeeeffffffffffff
        ffffffffffffcccccccccc777777ddddddddddddddde77777777777777777777777777777777777777777777777777777777777777777777777ddddddddddddddde777777777eeeeeeeffffffffffff
        fffffffffffcccccccccc7777777ddddddddddddddde7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde7777777777eeeeeeefffffffffff
        ffffffffffcccccccccc77777777ddddddddddddddde7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde7777777777eeeeeeefffffffffff
        fffffcccccccccccccc777777777ddddddddddddddde7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde7777777777eeeeeeeeeeeeffffff
        fffffcccccccccccccc777777777dddddddddddddddb7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde777777777777eeeeeeeeeeefffff
        fffcccccccccccccccc777777777dddddddddddddddb77777777777777777777777777777777777777777777777777777777777775777777777ddddddddddddddde777777777777eeeeeeeeeeeeefff
        ffeeeecc7cccccccccc777777777ddddddddddddddde77777777777777777777777777777777777777777777777777777777777754577777777ddddddddddddddde777777777777eeee7b77eeeeffff
        fcccccccccccccccc77777777777ddddddddddddddde77777777777777777777777777777777777777777777777777777777777775777777777ddddddddddddddde777777777777777ee77eeeeeffff
        8ccccccccccccccce37777777777ddddddddddddddde7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde7777bb7777777777eeeeeeeefff8
        8ccccccccccccccebbb777777777bdddddddddddddde7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddbe777bbbb777777777eeeeeeeeef88
        ccccccccccccccc7b3b777777777ddddddddddddddde7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde77773b77777777777eeeeeeeff88
        cccc66cccccc7777777777777777bbbbbbbbbbbbbbbe7777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde7777777777777777ccc6c66cf888
        6ccc6666666c7777777777777777eeeeeeeeeeeeeee77777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde777777777777777e666c666ccc66
        66cc66666666777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eddddddddddddddde7b7777777777777e666c666cc666
        66c6666c666cc777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777beeeeebebbeeeee777777777777777ec66666666c666
        6666666666ccccc7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eeeeeeeeeeeeeee7777777777777eeecc66666666666
        666c66666666cc66c77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777c6686666666666666
        666666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e66666666666666666
        6666666666666666c7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ec666666666c666666
        66666c66666666cc777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777cc666666666666666
        666666666666666cccc777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eccc6666666666666668
        666666666666666c666c7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e66666666666666666666
        6666666666666666666c7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e66666666666666866666
        6668866666666666666c7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ec6666666666666886666
        8668666c6666666666cc77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777c6666666666866686686
        8666668c666666666cc777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ec666666666886666688
        866666866666c66666cc7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ec6c66666666886666686
        6666666666666666666c7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e66666666666666666666
        666866666666c666666c7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e86666686666666688666
        666688888666866666ccc77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ec86666666668888886666
        86668886686666666c666c777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e6668666666686888886688
        886688866666666666666c777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e6666666666666688866688
        866668866666888668886c777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e8888668886666688666888
        88866688866668888888c777777777777777777777777777777777777b7777777777777777777777777777777777777777777777777777777777777777777777777777777e888888886668886668f88
        fff88888666668888888c77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777e88868886666688888ffff
        8ffffff88686f8888666877777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777c6666888f88688ffffffff
        ffffffff86fffff88f66877777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777f66888fffff86fffffffff
        ffffff8888ffffffff88877777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777c88fffffff8888ffffffff
        fffffff888f888ffffffc777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777effffff888888ffffffff
        fffff8f88fffffffffffcc77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777effffffff8f88ffffffff
        ffffcff88fff8fffffffccc7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777effffff88ffffffffffff
        fffffcffffff88fffffcccc777777777777777777777777777777777777777777777777777dd77777777777777777777777777777777777777777777777777777777777777effffff8fffffffffffff
        ffffffffffffffffffccccc77777777777777777777777777777777777777777777777777dddd777777777777777777777777777777777777777777777777777777777777eeefffffffffffffffffff
        fffffffffffffffffcccccc777777777bb77777777777777777777777777777777777777777d77777777777777777777777777777777777777777777777777777777777777eefffffffffffffffffff
        fffffffffffffffffcccccc77777777bbbb7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eeeffffffffffffffffff
        fffffffffffffffffcccccc777777777b77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eeeeffffffffffffffffff
        ffffffffffffffffffcccccee77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777eefffffffffffffffffff
        ffffffffffffffffffffcc77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777fffffffffffffffffffff
        fffffffffffffffffffffcc777effe777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffe77777efffffffffffffffffffff
        ffffffffffffffffffffffcfffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ffffeffcfffffffffffffffffffffff
        fffffffffffffffffffffffffffffffc7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777effffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777efffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffc7777777777777777777777777777777777777777777777777777777777777777777777777bb777777777777777effffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777bbbb7777777777777efffffffffffffffffffffffffffffffffff
        fffffffffffffffffccffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777bb77777777777777ffffffffffffffffeeffffffffffffffffff
        fffffffffffffffffccffffffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777ee77777777777777ffffffffffffffff7eefffffffffffffffff
        ffffffffffffffffffffcfc7ffffffffffff77777777777777777777777777777777777777777777777777777777777777777777777777777777777777efffffffffff77fffcffffcffffffffffffff
        ffffffffffffffffffffcfffc7ffffffffffff777777777777777777777777777777777777777777777777777777777777777777777777777bbb777effffffffffff7cfffcccfffffffffffffffffff
        ffffffffffffffffffccccff77ccffffffffffcc777bb77777777777777777777777777777777777777777777777777777777777777777777bbb7e7efffffffffffe77ffeeeefffffffffffffffffff
        fffffffffffffffffcffcccffc7cffffffffffcc77bb7b777777777777777777777777777777777777777777777777777777777777777777777e7eeeffffffffffe77fffeeeffefffffffffffffffff
        fffffffffffffffffffffffcffcfffffffffffcc777bb7777777777777777777777777777777777777777777777777777777777777777eeeeeeeeeeefffffffffffcffcffffffffffffffffffffffff
        fffffffffffffffffffcffccfcffccc77ffffffcccceeeee77777777777777777777777777777777777777777777777777777777777eeeeeeeeeeeeefffffcccccffcfccffcffffffffffffffffffff
        fffffffffffffffffffcffcffcffcccffffffffccccccccc7eeeeee77777777777777777777777777777777777777777777777777eeeeeeeeeeeeeeffffffffccccfcffcfffffffffffffffffffffff
        ffffffffffffffffffffffccfffcccfffffffffccccccccccccccccccc77777777777777777777777777777777ee77777e777eeeeeeeeeeeeeeeeeefffffffffcccfffccfffffffffffffffffffffff
        ffffffffffffffffffffffccfffccffffffffffcccccccccccccccccccccccccc77777777777777777777777eebee77ee7eeeeeeeeeeeeeeeeeeeeefffffffffffcffffcfffffffffffffffffffffff
        ffffffffffffffffffffffffffffccffffffffffccccccccccccccccccccccccccccc77777777777777777eeebbbeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffccfffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffcfffffffffffccccccccccccccccccccccccccccccc77ee7e7e777777eeeeebeeeeeeeeeeeeeeeeeeeeeeeccccfffffffffffccffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffcccccffffccffffcccccccccccccccccceeeeeee7eeeeeeeeeeeeeeeeeeeeeeeeeeeeffeeeeeffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffccccfffffffffffffcccffcccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeefffffcfffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccccccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccccccccccccffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccccccccfcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffcccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbcfffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbbbcffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbbbbbcfffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbbcfffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcbffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.tipus_conversio_1)
    sprites.destroy_all_sprites_of_kind(SpriteKind.tipus_conversio_2)
    jugador.set_position(78, 85)
    patata = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . f f f f . . . . . .
            . . . . f f f 5 5 f f . . . . .
            . . . f f 5 5 5 5 5 f f . . . .
            . . f f 5 5 5 5 5 5 5 f f . . .
            . . f f 5 5 5 5 5 5 5 f f . . .
            . f f 5 5 5 5 5 5 5 5 5 f f . .
            . f f 5 5 5 5 5 5 5 5 5 f f . .
            . f f 5 5 5 5 5 5 5 5 5 f f . .
            . f f 5 5 5 5 5 5 5 5 5 f f . .
            . f f 5 5 5 5 5 5 5 5 5 f f . .
            . f f 5 5 5 5 5 5 5 5 5 f f . .
            . . f f 5 5 5 5 5 5 5 f f . . .
            . . f f 5 5 5 5 5 5 5 f f . . .
            . . . f f 5 5 5 5 5 f f . . . .
            . . . . f f f f f f f . . . . .
            """),
        SpriteKind.Canvi)
    patata.set_position(53, 48)
    gallina = sprites.create(img("""
            .......................
            .......................
            .............ffff......
            .............f222f.....
            ............ff222ff....
            ...........ff44444ff...
            ...........f4444f4bf...
            .ffff.....ff44422455...
            .fe4f.....f44444225f...
            .f444ffffff4444442ef...
            .f444444444444444fff...
            .f44444444444e4e4f.....
            .ff44e44444444444f.....
            ..f44e44444444444f.....
            ..ff44e4444444444f.....
            ...ff44e44ee44444f.....
            ....ff444444444fff.....
            .....ff4444444ff.......
            ......fff44eeff........
            ........fbeebff........
            ........fbeeeef........
            ........feb4bbf........
            ........fffffff........
            .......................
            """),
        SpriteKind.Canvi)
    gallina.set_position(80, 36)
    cabra = sprites.create(img("""
            .......................
            .......................
            ............cbbbb......
            ............bbbbbb.....
            ..............bbbcb....
            .............eebddd....
            .............bebdbdb...
            ...........d..bbdcdd...
            .............bddddddbb.
            .b.........bbd1dbbbbb..
            bbbbbddbbbdddd1dbcbbb..
            .bbbddbbddd1dddde..c...
            ..cddddddddddddde......
            ..bbddd1dddddddbb......
            ..bbdddddddddbbb.......
            ...bddbdddbddbbb.......
            ...bdbebbbeddec........
            ...bbebbbbbdbeb........
            ..bbee.....bee.........
            ..bbeb.....eee.........
            ..bbee.....beeb........
            ...bce.....bbee........
            ...bb..................
            .......................
            """),
        SpriteKind.Canvi)
    cabra.set_position(110, 46)
    ou = sprites.create(img("""
            .......................
            .......................
            ........fffff.......d..
            .......ffddddf.........
            .......fddddddf........
            ......fddddddddf.......
            .....fdddddddddf.......
            .....fdddddddddf.......
            ....fdddddddddddf......
            ....fdddddddddddf......
            ....fddddddddddddf.....
            ....fddddddddddddf.....
            ....fddddddddddddf.....
            ....fdddddddddddbf.....
            ....fdddddddddddbf.....
            ....fdddddddddddbf.....
            ....fddddddddddbf......
            .....fdddddddddbf......
            .....fbdddddddbf.......
            ......fbbdddbbbf.......
            .......fbbbbbbf........
            ........ffffff.........
            .......................
            .......................
            """),
        SpriteKind.Canvi)
    ou.set_position(36, 75)
    cavall = sprites.create(img("""
            .......................
            .................b.....
            ................cfcd...
            ...............cfffb...
            .............bcfcccc...
            .............cffceeb...
            ............bfffceeeb..
            ...........bfffefcecc..
            .....bcbbbbcffeef..cb..
            ..bceeeeeeeefceee......
            .cffeeeeeeeeeeecc......
            .cffeeeeeeeeeeecc......
            .cffeeeeeeeeeeecc......
            .cffeeefceeceeccb......
            .cffeecffcffcefc.......
            .cfceeffb...ecfe.......
            .cfceccc....eefb.......
            .cfccbfb....ecfb.......
            .ccebdc.....ebfb.......
            .b.bbdc.....cbcb.......
            ...bbdcb....edcb.......
            ...bedbf....ebcb.......
            ....cb.bb...bcbc.......
            .......................
            """),
        SpriteKind.Canvi)
    cavall.set_position(131, 64)
    mySprite = sprites.create(img("""
            . . . . f f f f f . . . . . . .
            . . . f e e e e e f . . . . . .
            . . f d d d d e e e f . . . . .
            . c d f d d f d e e f f . . . .
            . c d f d d f d e e d d f . . .
            c d e e d d d d e e b d c . . .
            c d d d d c d d e e b d c . f f
            c c c c c d d d e e f c . f e f
            . f d d d d d e e f f . . f e f
            . . f f f f f e e e e f . f e f
            . . . . f e e e e e e e f f e f
            . . . f e f f e f e e e e f f .
            . . . f e f f e f e e e e f . .
            . . . f d b f d b f f e f . . .
            . . . f d d c d d b b d f . . .
            . . . . f f f f f f f f f . . .
            """),
        SpriteKind.Sortida)
    mySprite.set_position(116, 102)
    mySprite.say_text("Sortir?")

def on_on_overlap3(sprite3, otherSprite):
    if otherSprite == patata:
        doSomething(game.ask_for_number("Quantes patates vols?"), 0)
    elif otherSprite == gallina:
        doSomething(game.ask_for_number("Quantes gallines vols?"), 1)
    elif otherSprite == cabra:
        doSomething(game.ask_for_number("Quantes cabres vols?"), 2)
    elif otherSprite == ou:
        doSomething(game.ask_for_number("Quants ous vols?"), 3)
    elif otherSprite == cavall:
        doSomething(game.ask_for_number("Quants cavalls vols?"), 4)
sprites.on_overlap(SpriteKind.player, SpriteKind.Canvi, on_on_overlap3)

def preparar_home():
    global conversio_1, conversio_2
    scene.set_background_image(img("""
        cccccccccccccccccceeeeeeeeeeeeecccfcccccccccccccccccccccc7777777777777777777444444444444444444444444444444ecccceeeeeeeecccceeeeeeeeeeeeecccceeeeeeeeeeccffccccc
        ccccccccccccccccccceeeeeeeeccccccfccccffccffccccccccccccce777777777777777777444444444444444444444444444444eccceeeeeeccccccceeeeeeeeeeeeeccceeeeeeeeeeeccccccccc
        ccccccccccccccccccceeeeeeeeccccccccccccfcccccccccccccccccce777777777777777777444444444444444444444444444444eccccccecccccccceeeeeeeeeeeeccceeeeeeeeeeeeccccceeee
        eeeeeeeecccccccccccceeeeeeeeeeeeeeeccccccccccccccccccccccce777777777777777777b44444444444444444444444444444ecccccceccccccccceeeeeeeeeeeccceeeeeeeeeeeeecccccccc
        cccccccccccccccceeeeeeeeeeeeeeeeeeeeceeccccccccccccccccccce7777777777777777777444444444444444444444444444444eccccccccccccccceeeeeeeeeecccceeeeeeeeeeeeecccccccc
        ccccccccccccccceeeeeeeeeeeeccccccccccceccccccccccccccccccce77777777777777777744444444444444444444444444444444eeeecccccceeeecceeeeeeeeeeccceeeeeeeeeeeeccccccccc
        cccccccccccccceeeeeeeeeeeeecccccccccccccccccccccccccccccce77777777777777777e444444444444444444444444444444444444eccccceeeeeceeeeeeeeeecccceeeeeeeeeeeeccccccccc
        ccccccccccccccceeeeeeeeeeecfcccccccccccccccccccccccccccce77777777777777777774444444444444444444444444444444444444eeecceeeeeeeeeeeeeeeccccceeeeeeeeeeeeccccccccc
        cccccccccccccccccccccccccccfcccccccccccccccccccccccccccc777777777777777777774444444444444444444444444444444444444eeecceeeeeeccceeeeecccccceeeeeeeeeeeeccccccccc
        ccccccccccccccccccccccccccffcccccccccee7eeeeeeeeeeeeeee7777777777777777777774444444444444444444444444444444444444eeccceeeeeecccccccccccccceeeeeeeeeeeeccccccccc
        ccccccccccccccccccccccccccfcccccccccce7777eeeeeeeeeeee77777777777777777777774444444444444444444444444444444444444eeeceeeeeeeeecccccccccccceeeeeeeeeeecccccccccc
        ccccccccffccccccccccccccccccccccccccc777777eeeeeeeee77777777777777777777777744444444444444444444444444444444444444eeeeeeeeeeeecccccccccccceeeeeeeeeeecccccccccc
        cccccccfffffccccccccccccccccccccccccce77777777777777777777777777777777777777444444444444444444444444444444444444444eeeeeeeeeeeeeeeecceeeccceeeeeeeecccccccccccc
        ccccccccfffcccccccccccffcccccccccccccce777777777777777777777777777777777777444444444444444444444444444444444444444444eeeeeeeeeeeeeecceeeeccceeeccccccccccccccce
        eeeeeeeecffcccccccccccccccccccccccccccce7777777777777777777777777777777777744444444444444444444444444444444444444444444eee4e44eeeeecceeeeecccccccccccccccccccee
        eeeeeeeeeccccccccccccccccccccceeeeeeeeee777777777777777777777777777777777777444444444444444444444444444444444444444444444444444eeeeceeeeeeeccccccccccccccceeeee
        eeeeeeeeeeecccccceeccccccccccccccceeeeee7777777777777777777777777777777777777444444444444444444444444444444444444444444444444444eeeeeeeeeeeeeccccccccccceeeeeee
        eeeeeeeeeeecfcccceecccccccccccccccccccce777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444eeeeeeeeeeeeceecccccceeeeeeee
        eeeeeeeeeeecfccccceccccccccccccccccccce777777777777777777777777777777777777777b444444444444444444444444444444444444444444444444444444eeeeeeeeeeeeecceeceeeeeeee
        eeeeeeeeeeeecfcccccccccccccccccccccccc777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444eeeeee44eeeecceeeeeeeeeee
        eeeeeeeeeeeeccccccccccccccccccccccccc77777777777777777777777777777777777777777e4444444444444444444444444444444444444444444444444444444444444444eeeeeeeeeeeeeeee
        eeeeeeeeeeecccccccceeeeeeeeeeeeeeeee77777777777777777777777777777777777777777e4444444444444444444444444444444444444444444b4444444444444444444444eeeeeeceeeeeeee
        eeeeeeeeeeecccccee7777eeeeeeeeeeeee77777777777777777777777777777777777777777774444444444444444444444444444444444444444444bbbbb4bbb44444444444444444eecceeeeeeee
        eeeeeeeeeeccccc777777777eeeeeeeee777777777777777777777777777777777777777777777b444444444444444444444444444444444444444444bbbbbdddbb4444444444444444eeceeeeeeeee
        eeeeeeeeeeccccce77777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444bb4bb4444444bbdbdddddbb44444444444444444eeeeeeeeeee
        eeeeeeeeeeeccccccee7777777777777777777777777777777777777777777777777777777777774444444444444444444444444444bbdddbb4444444bbbdddddb444444444444444444eeeeeeeeeee
        eeeeeeecccccffcccccce7777777777777777777777777777777777777777777777777777777777b444444444444444444444444444bddddbb4444444bebdddbbb444444444444444444eeceeeeeeee
        eeeeeeccccccfcccccccce777777777777777777777777777777777777777777777777777e77777e444444444444444444444444444bbdddbb44444444ebbbbbbee44444444444444444eecceeeeeee
        eeecccccccfffccccccccce777777777777777777777777777777777777777777777777777777777b44444444444444444444444444bbdddbe44444444eeeeeeeeee44444444444444444eccceeeeee
        ccccccccccfffcccccccccce77777777777777777777777777777777777777777777777777777777744444444444444444444444444bbbbbeee44444444eeeeeeeee44444444444444444eccceeeeee
        cccccccccfffcccccccccccce7777777777777777777777777777777777777777777777777777777b44444444444444444444444444bbeeeeee44444444eeeeeee4444444444444444444ecccccccec
        fccccffccfcccccccccccccce77777777777777777777ebbbbbbbb77777777777777777777777774444444444444444444444444444beeeeeee4444444444444444444444444444444444eecccccccc
        cccccffcccccccccccccccccc77777777777777777777ebbbbbbbb777777777777777777777777444444444444444444444444444444eeeeee4444444444444444444444444444444444444eccccccc
        ccccccccccccccccccccccccc77777777777777777777ebbbbbbbe7777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444eeeecccc
        cccceccccccccccccccccccce777777777777777777777bbbbbbbe777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444eeccee
        eeeeeecccccccccccccccccce777777777777777777777eeeeeee777777777777777777777777b44444444444444444444444444444444444444444444444444444444444444444444444444444eeee
        eeeeccccccccccccccccccce7777777777777777777777eeeeee77777777777777777777777777444444444444444444444444444444444444444444444444444444444444444444444444444444eee
        eeeeeeeeeeeeeeeeeeeeeee777777777777777777777777eeee77777777777777777777777777b444444444444444444444444444444444444444444444444444444444444444444444444444444eee
        eeeeeeeeeeeeeeeeeeeeee77777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444eee
        eeeeeeeeeeeeeeeeeeeee7777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444b44444444444444444444444444444ee
        eeeee777eeeeeeeeeeee77777777777777777777777777777777777777777777777777777777eb444444444444444444444444444444444444444444444444bbbb44bbb44444444444444444444444e
        eeeee7777eeeeeeeeee7777777777777777777777777777777777777777777777777777777777eb44444444444444444444444444444444444444444444444bdbbbddddb44444444444444444444444
        eeeee7777777777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444bbbddddddb44444444444444444444444
        eeeee7777777777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444bbbddddddb44444444444444444444444
        eeeeee7777777777777777777777777777777777777777777777777777777777777777777777777b44444444444444444444444444444444444444444444444ebdddddbb44444444444444444444444
        eeeeeee7777777777777777777777777777777777777777777777777777777777777777777777777b4444444444444444444444444444444444444444444444ebbbbbbbeeeee4444444444444444444
        eeeeeeee77777777777777777777777777777777777777777777777777777777777777777777777eb44444444444444444444444444444444444444444444444bbbeeeeeeeee4444444444444444444
        eeeeeeeee777777777777777777777ebbbbb777777777777777777777777777777777777777777e4444444444444444444444444444444444444444444444444eeeeeeeeeeee4444444444444444444
        eeeeeeeeee77777777777777777777bbbbbb77777777777777777777777777777777777777777e444444444444444444444bbbbbbbbb4444444444444444444444eeeeee44444444444444444444444
        eeeeeeeeeee7777777777777777777eeeeee7777777777777777777777777777777777777777eb444444444444444444444bdddbbbdb444444444444444444444444444444444444444444444444444
        eeeeeeeeeee7777777777777777777eeeeee777777777777777777777777777777777777777777774444444444444444444bddddbbdb444444444444444444444444444444444444444444444444444
        eeeeeeeeeee7777777777777777777eeeeee777777777777777777777777777777777777777777774444444444444444444bdddddbbb444444444444444444444444444444444444444444444444444
        eeeeeeeeccc7777777777777777777eeeee7777777777777777777777777777777777777777777744444444444444444444bbbbbbbeee4444444444444444444444444444444444444444444444444e
        eeeeeeeeecc777777777777777777777ee777777777777777777777777777777777777777777777444444444444444444444bbbebbeeeeee44444444444b444444b4444444444444444444444444eee
        eeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777777777744444444444444444444feeeeeeeeeeee4444444444bbbbbbbdbb44444444444444444444444eeee
        eeeeeeeeeccce777777777777777777777777777777777777777777777777777777777777777777444444444444444444444eeeeeeeeeee44444444444bdbbbddddb4444444444444444444444eeeee
        eeeeeeeecccccce77777777777777777777777777777777777777777777777777777777777777774b44444444444444444444444444444444444444444bbbbddddd4444444444444444444444eceeee
        eeeeeeeecccccccce7777777777777777777777777777777777777777777777ebbbbbe77777777744444444444444444444444444444444444444444444bbbddddb4444444444444444444444eeeeee
        eeeeeeeeccccccccce77777777777777777777777777777777777777777777eebbbbbe77777777744444444444444444444444444444444444444444444eebdbbbbe444444444444444444444eeeeee
        eeeeeeeccccccccccce777777777777777777777777777777777777777777eeebbebbe777777777444444444444444444444444444444444444444444444ebbeeeeeee444444444444444444eeeeeee
        ccccccccccccccccccc7777777777777777777777777777777777777777777eebbbbeee77777777444444444444444444444444444444444444444444444eeeeeeeeee4444444444444444444eeeeee
        ccccccccccccccccccc77777777777777777777777777777777777777777777eeeeeeee777777774444444444444444444444444444444444444444444444eeeeeeee44444444444444444444eeeeee
        cccccccccccccccccce77777777777777777777777777777777777777777777eeeeeeee777777774444444444444444444444444444444444444444444444444444444444444444444444444eeeeeee
        ccccccccccccccccccc77777777777777777777777777777777777777777777eeeeeee7777777774444444444444444444444444444444444444444444444444444444444444444444444444eeeeeee
        ccccccccccccccccccc77777777777777777777777777777777777777777777eeeeee777777777744444444444444444444444444444444444444444444444444444444444444444444444444ecceee
        cccccccccccccccccce77777777777777777777777777777777777777777777eeeeee777777777744444444444444444444444444444444444444444444444444444444444444444444444444eceeee
        ecccccccccccccccce77777777777777777777777777777777777777777777777eee7777777777744444444444444444444444444444444444444444444444444444444444444444444444444eceeee
        eecccccccccccccce7777777777777777777777777777777777777777777777777e77777777777444444444444444444444444444444444444444444444444444444444444444444444444444eeceec
        ccccccccccccccce777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444ecccc
        cccccccccccccce7777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444eeecc
        ce77eeeeeeeee77777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444eee
        e7777eeeeeee777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        e77777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444444
        77777777777777777777777777777777777777777777777777777777777777777777777777b744444444444444444444444444444444444444444444444444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444bb4444444444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777444444444444444444444444444444444444444444444444444bbbbbbbdbb44444444444444444444444444444
        77777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444bbbbbbdddbb44444444444444444444444444444
        77777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444bbbbbddddb444444444444444444444444444444
        777777777777777777777777777777777777777777777777777777777777777777777b44444444444444444444444444444444444444444444444444bebddddbb444444444444444444444444444444
        7777777777777777777777777777777777777777777777777777777777777777777777444444444444444444444444444444444444444444444444444ebbbbebee44444444444444444444444444444
        7777777777777777777777777777777777777777777777777777777777777777777777b44444444444444444444444444444444444444444444444444eebeeeeeeee444444444444444444444444444
        77777777777777777777777777777777777777777777777777777777777777777777777444444444444444444444444444444444444444444444444444eeeeeeeeee444444444444444444444444444
        7ee777777777777777777777777777777777777777777777777777777777777777777774444444444444444444444444b44444444444444444444444444eeeeeeee4444444444444444444444444444
        eeeeee7777777777777777777777777777777777777777777777777777777777777777444444444444444444444444bbbb4444444444444444444444444444444444444444444444444444444444444
        eeeeeee777777777777777777777777777777777777777777777777777777777777774444444444444444444444444bddb4444444444444444444444444444444444444444444444444444444444444
        eeeeeeee777777777777777777777777bbbbbbb7777777777777777777777777777744444444444444444444444444bdbb4444444444444444444444444444444444444444444444444444444444eee
        eeeeeeeee77777777777777777777777bbbbbbb77777777777777777777777777777b4444444444444444444444444ebbb444444444444444444444444444444444444444444444444444444444eeee
        eeeeeeeeee7777777777777777777777eeebbee777777777777777777777777777777eb44444444444444444444444eeeeeee44444444444444444444444444444444444444444444444444444eeeee
        eeeeeeeeee7777777777777777777777eeeeeee77777777777777777777777777777777b44444444444444444444444eeeee44444444444444444444444444444444444444444444444444444eeeeee
        eeeeeeeeee7777777777777777777777eeeeeee777777777777777777777777777777777444444444444444444444444444444444444444444444444444444444444444444444444444444444eeeeee
        eeeeeeeeeee777777777777777777777eeeeeee77777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444444444eeeeeee
        eeeeeeeeeee777777777777777777777eeeeeee77777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444444444eeeeeee
        eeeeeeeecc7777777777777777777777eeeeeee77777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444444444eeeeeee
        eeeeeeeecce7777777777777777777777eeeee777777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444444444eeeeeee
        eeeeeeeeccce77777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444444444eeeeeee
        eeeeeeeeecccce77777777777777777777777777777777777777777777777777777777774444444444444444444444444444444bbdd444444444444444444444444444444444444444444444eeeeeee
        eeeeeeeeccccccc77777777777777777777777777777777bbbbbbe7777777777777777774444444444444444444444444444444bbddb44444444444444444444444444444444444444444444eeeeeee
        eeeeeeeecccccccce777777777777777777777777777777bbbbbbbbe77777777777777777444444444444444444444444444444bbddbb4444444444444444444444444444444444444444444eeeeeee
        eeeeeeeccccccccccce7777777777777777777777777777bbbbbeeeee77777777777777777777444444444444444444444444444bbdbb44444444444444444444444444444444444444444444eeeeee
        eeeeeecfccccccccccc7777777777777777777777777777eeeeeeeeee77777777777777777777744444444444444444444444444eebeeee4444444444444444444444444444444444444444444eeeee
        eeeccccccccccccccce7777777777777777777777777777eeeeeeeeee777777777777777777777b44444444444444444444444444eeeeee4444444444444444444444444444444444444444444eeeee
        cccccccccccccccccce7777777777777777777777777777eeeeeeeeee77777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444eeec
        ccccccccccccccccccc77777777777777777777777777777eeeeeeeee7777777777777777777777b4444444444444444444444444444444444444444444444444444444444444444444444444444eee
        ccccccccccccccccccc77777777777777777777777777777eeeeeeeee777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444eee
        ccccccccccccccccce77777777777777777777777777777777eeeeeee7777777777777777777777b444444444444444444444444bbbbb44444444444444444444444444444444444bbb44444444444e
        ccccccccccccccccc777777777777777777777777777777777eeeeee77777777777777777777774444444444444444444444444bbdddbb44444444444444444444444444444444bddbb44444444444e
        cccccccccccccccce77777777777777bbbbb7777777777777777eee777777777777777777777774444444444444444444444444bbddddb4444444444444444444444444444444bddddb44444444444e
        eeeeeeeeeeeeeeee7777777777777ebbbbbbb777777777777777777777777777777777777777744444444444444444444444444bbdddbb4444444444444444444444444444444bddddb44444444444e
        eeeeeeeeeeeeee777777777777777ebbbbbbb777777777777777777777777777777777777777774444444444444444444444444bbbddbb4444444444444444444444444444444bbdbbb444444444444
        ee7eeeeeeeeee7777777777777777eeeeeeeeee777777777777777777777777777777777777777b4444444444444444444444444bbbbbee4444444444444444444444444444444bbbee444444444444
        e777eeeeeee777777777777777777eeeeeeeeeee77777777777777777777777777777777777777e4444444444444444444444444beeeeee4444444444444444444444444444444eeeeeeee444444444
        77777777777777777777777777777eeeeeeeeeee77777777777777777777777777777777777777e4444444444444444444444444eeeeeee44444444444444444444444444444444eeeeeeee44444444
        77777777777777777777777777777eeeeeeeeeee7777777777777777777777777777777777777774444444444444444444444444444eee44444444444444444444444444444444444ee444444444444
        77777777777e777777777777777777eeeeeeeeee77777777777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444444444
        77777777777e777777777777777777eeeeeeeeee77777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444444444444
        7eeeeeeee77777777777777777777777eeeeeee777777777777777777777777777777777777777777444444444444444444444444444444444444444444444444444444444444444444444444444eee
        eeeeeeeeee7777777777777777777777777e7777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444eeeee
        eeeeeeeeeee7777777777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444444444444444444444444444eeeeee
        eeeeeeeeeccc77777777777777777777777777777777777777777777777777777777777777777b4444444444444444444444444444444444bbbbbbbb4444444444444444444444444444444eeeeeeee
        eeeeeeeeeeecce777777777777777777777777777777777777777777777777777777777777777b444444444444444444444444444444444bdddbbbdb4444444444444444444444444444444eeeeeeee
        eeeeeeeeeeeccc7777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444bddddbbdb44444444444444444444444444444eeeeeeeeee
        eeeeeeeeeecccce777777777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444bbddddbbb4444444444444444444444444444eeeeeeeeeee
        eeeeeeeeeeeeccc7777777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444bbbddbe44444444444444444444444444444eeeeeeeeeee
        eeeeeeeeeeeeccc777777777777777777777777777777777777777777777777777777777777b444444444444444444444444444444444444beebbbee44444444444444444444444444444eeeeeeeeee
        eeeeeeeeeeecccce7777777777777777777777777777777777777777777777777777777777b44444444444444444444444444444b4444444eeebbeeeee44444444444444444444444444eeeeeeeeeee
        eeeeeeeeeeecccce7777777777777777777777777777777777777777777777777777777777b444444444444444444444b444444bbb444444eeeeeeeeee44444444444444444444444444eeeeeeeeeee
        eeeeeeeeeeccccc77777777777777777777777777777777777777777777777777777777777774444444444444444444bddbbbbbbdb44444444eeeeeee444444444444444444444444444eeeeeeeeeee
        eeeeeeeeeeccccc7777777777777777777777777777777777777777777777777777777777777744444444444444444bbdddddddddb444444444444444444444444444444444444444444eeeeeeeeeee
        eeeeeeeeeecccccce777777777777777777777777777777777777777777777777777777777777444444444444444444bdddddddbbb444444444444444444444444444444444444444444eeeeeeeeeee
        eeeeeeecccccccccccee777777777777777777777777777777777777777777777777777777777444444444444444444bbddddddbbb444444444444444444444444444444444444444444eeeeeeeeeee
        eeeeeeccccccfccccccce777777777777777777777777777777777777777777777777777777eb444444444444444444bbbbbbdbbee444444444444444444444444444444444444444444eeccceeeeee
        ccccccccccccfcccccccce77777777777777777777777777777777777777777777777777777b4444444444444444444beceeebbeeee444444444444444444444444444444444444444444eeeeeeeeee
        ccccccccccfffccccccccce777777777777777777777777777777777777777777777777777777444444444444444444beeeeeeeeee44444444444444bbbb4444444444444444444444444eeeeeeeeee
        cccccccccffcccccccccccce7777777777777777777777777777777777777777777777777777744444444444444444444444eeee4444444444444444bddbb444444444444444444444444eeeeeeeeee
        ccccccccffcccccccccccccce7777777777777777777777777777777777777777777777777777444444444444444444444444444444444444444444bbdddb4444444444444444444444444eeccccccc
        ccfccccccfcccccccccccccce77777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444bbdbb44444444444444444444444444eeeeeccc
        cccccccccccccccccccccccce77777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444bbbee4444444444444444444444444444eecccc
        eeececcccccccccccccccccce777777777777777777777777777777777777777777777777777444444444444444444444444444444444444444444444eeeee44444444444444444444444444444eeee
        eeeeeecccccccccccccccccc77777777777777777777777777777777777777777777777777777b44444444444444444444444444444444444444444444444444444444444444444444444444444eeee
        7eecccccccccccccccccccce777777777777777777777777777777777777777777777777777777b44444444444444444444444444444444444444444444444444444444444444444444444d44444eec
        eeeccccccccccccccccccce777777777777777777777777777777777777777777777777777777774444444444444444444444444444444444444444444444444444444444444444444444dd44444eee
        eeeeeeecccccccccccccce777777777777777777777777777777777777777777777777777777777744444444444444444444444444444444444444444444444444ee4444444444444444ddddd44eeee
        eeeeeeeecccccccccccce7777777eeeeeeeee7e777777777777777777777777777777777777777774444444444444444444444444444444444444444444444eeeeeee44444444e44eeeddddddbeceee
        eeeeeeeeeecccccccce7777777eeeeeeeeeeeeee777777777777777777777777777777777777777b444444444444444444444444444444444444444444444eeeeeeeeee4444eeeeeeeeebddbeeeeeee
        eeeeeeeeeecccccce777777777eeeeeeeeeeeeeeee7777777777777777777777777777777777777444444444444444444444444444444444444444444444eeeeeeeeeeee44eeeeeeeeeeebdeeeeeeee
        eeeeeeeeeecfcce77777777777eeeeeeeeeeeeeeeee77777777777777777777777777777777774444444444444444444444444444444444444444444444eeeeeeeeeeeeeeeeeeeeeeeeceebeeeeeeee
        eeeeeeeeeecccce77777777777eeeeeeeeeeeeeeeee77777777777777777777777777777777b4444444444444444444444444444444444444444444444eeeeeeeeeeeeeeecceeeeeeeeecceeeeeeeee
        eeeeeeeeeeccccc777777777eeeeeeeeeeeeeeeeeeee777777777777777777777777777777744444444444444444444444444444444444444444444444eeeeeeeeeeeeeeecceeeeeeeeeceeeeeeeeee
        eeeeeeeeeeccccc777777777eeeeeeeeeeeeeeeeeeee777777777777777777777777777777774444444444444444444444444444444444444444444444eeeeeeeeeeeeeeeccceeeeeeeecceeeeeeeee
        eeeeeeeeeeeccccc77777777eeeeeeeeeeeeeeeeeccc77777777777777777777777777777777744444444444444444444444444444444444444444444eeeeeeeeeeeeeeeeccceeeeeeeccceeeeeeeee
        eeeeeeeeeeeccccc7777777eeeeeeeeeeeeeeeeeeccc77777777777777777777777777777777744444444444444444444444444444444444444444444eeeeeeeeeeeeeeeeccceeeeeeeccceeeeeeeee
        """))
    conversio_1 = sprites.create(img("""
            . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            . b b b d 5 5 5 5 5 4 4 4 4 4 b
            b d d d b b d 5 5 4 4 4 4 4 b .
            b b d 5 5 5 b 5 5 5 5 5 5 b . .
            c d c 5 5 5 5 d 5 5 5 5 5 5 b .
            c b d c d 5 5 b 5 5 5 5 5 5 b .
            . c d d c c b d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.tipus_conversio_1)
    conversio_1.say_text("Animals a   Llenya")
    sprites.destroy_all_sprites_of_kind(SpriteKind.Canvi)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Sortida)
    conversio_1.set_position(121, 67)
    conversio_2 = sprites.create(img("""
            . . . . . b b b b b b . . . . .
            . . . b b d d d d d d b b . . .
            . . b b d d b b b b d d b b . .
            . e d b d b d d d d b d b d e .
            . f d b d d b b b b d d b d e .
            . f b d b b d d d d b b d b e .
            . f e d d d b b b b d d d e e .
            . f f e b d d d d d d b e e f .
            . f f e e e e e e e e e e e f .
            . f f e e e f e e e e e e e f .
            . f f e f e e e f f e e f e e f
            . f e e f e f e f e f e f e e e
            f f e e e e f e e f f e f f e e
            f e e e e f f e e e e e f f f e
            e e e e f f f e f e e e e f f f
            e e e e f f f e f e e e e f f f
            """),
        SpriteKind.tipus_conversio_2)
    conversio_2.set_position(33, 67)
    conversio_2.say_text("Llenya a   Animals")
def doSomething(cantidad: number, isprite: number):
    global resultado
    if cantidad <= 0:
        game.show_long_text("No es poden posar números negatius ni 0!",
            DialogLayout.BOTTOM)
    elif not (cantidad % 1 == 0):
        game.show_long_text("No pots partir aquest item per la meitat...",
            DialogLayout.BOTTOM)
    else:
        if tipus_conversio == 1:
            resultado = cantidad * conversions_productes[isprite]
            game.show_long_text("" + str(cantidad) + " " + productes[isprite] + " = " + ("" + str(Math.round(resultado))) + " kg llenya",
                DialogLayout.BOTTOM)
        else:
            resultado = cantidad / conversions_productes[isprite]
            game.show_long_text("" + str(cantidad) + " kg llenya = " + ("" + str(Math.round(resultado * 100) / 100)) + " " + productes[isprite],
                DialogLayout.BOTTOM)
        jugador.set_position(78, 85)

def on_on_overlap4(sprite22, otherSprite22):
    global tipus_conversio
    if game.ask("Entrar a la conversió?"):
        tipus_conversio = 2
        preparar_mercat()
sprites.on_overlap(SpriteKind.player,
    SpriteKind.tipus_conversio_2,
    on_on_overlap4)

resultado = 0
conversio_2: Sprite = None
conversio_1: Sprite = None
mySprite: Sprite = None
cavall: Sprite = None
ou: Sprite = None
cabra: Sprite = None
gallina: Sprite = None
patata: Sprite = None
tipus_conversio = 0
jugador: Sprite = None
conversions_productes: List[number] = []
productes: List[str] = []
productes = ["patata", "gallina", "cabra", "ou", "cavall"]
conversions_productes = [1.333, 6, 5, 0.25, 12]
jugador = sprites.create(img("""
        ...............................
        ...............................
        ...............................
        ...............................
        ..........ffffffffff...........
        .........f1111111111f..........
        ........f111111111111f.........
        .......f11111111111111f........
        ......f1111111111111111f.......
        .....f111111111111111111f......
        .....f11111f1111f1111111f......
        .....f1111fdf11fdf111111f......
        .....f1111fddf1fddf11111f......
        .....f111fddddffdddf1111f......
        .....f11fdd8dddddd8df111f......
        .....f11fdd8dddddd8df111f......
        .....f11fdddddddddddf111f......
        .....f11fdddddffddddf111f......
        .....f111fdddddddddf1111f......
        .....f1111fffffffff111111f.....
        ....f1111fcbffbbffbf11111f.....
        ....f111fbccccffccccc11111f....
        ...f1111fbccbfcebbcbbf1111f....
        ...f111ffbccb2bffbcbbbf1111f...
        ..f111fdfbcbbbbbbbbfbfdf111f...
        ..f1111fdccbbbbbbbbfcdf11ff....
        ...ff111ffcbbbbbbbbfff11f......
        .....f11f.fffffffffff11f.......
        ......ff..fddf.fddf..ff........
        ...........ff...ff.............
        ...............................
        ...............................
        """),
    SpriteKind.player)
controller.move_sprite(jugador)
jugador.set_stay_in_screen(True)
animation.run_image_animation(jugador,
    [img("""
            ...............................
            ...............................
            ...............................
            ...............................
            ..........ffffffffff...........
            .........f1111111111f..........
            ........f111111111111f.........
            .......f11111111111111f........
            ......f1111111111111111f.......
            .....f111111111111111111f......
            .....f11111f1111f1111111f......
            .....f1111fdf11fdf111111f......
            .....f1111fddf1fddf11111f......
            .....f111fddddffdddf1111f......
            .....f11fdd8dddddd8df111f......
            .....f11fdd8dddddd8df111f......
            .....f11fdddddddddddf111f......
            .....f11fdddddffddddf111f......
            .....f111fdddddddddf1111f......
            .....f1111fffffffff111111f.....
            ....f1111fcbffbbffbf11111f.....
            ....f111fbccccffccccc11111f....
            ...f1111fbccbfcebbcbbf1111f....
            ...f111ffbccb2bffbcbbbf1111f...
            ..f111fdfbcbbbbbbbbfbfdf111f...
            ..f1111fdccbbbbbbbbfcdf11ff....
            ...ff111ffcbbbbbbbbfff11f......
            .....f11f.fffffffffff11f.......
            ......ff..fddf.fddf..ff........
            ...........ff...ff.............
            ...............................
            ...............................
            """),
        img("""
            ...............................
            ...............................
            ...............................
            ...............................
            ..........ffffffffff...........
            .........f1111111111f..........
            ........f111111111111f.........
            .......f11111111111111f........
            ......f1111111111111111f.......
            .....f111111111111111111f......
            .....f11111f1111f1111111f......
            .....f1111fdf11fdf111111f......
            .....f1111fddf1fddf11111f......
            .....f111fddddffdddf1111f......
            .....f11fdddddddddddf111f......
            .....f11fddfddddddfdf111f......
            .....f11fdddddddddddf111f......
            .....f11fdddddffddddf111f......
            .....f111fdddddddddf1111f......
            .....f1111fffffffff111111f.....
            ....f1111fcbffbbffbf11111f.....
            ....f111fbccccffccccc11111f....
            ...f1111fbccbfcebbcbbf1111f....
            ...f111ffbccb2bffbcbbbf1111f...
            ..f111fdfbcbbbbbbbbfbfdf111f...
            ..f1111fdccbbbbbbbbfcdf11ff....
            ...ff111ffcbbbbbbbbfff11f......
            .....f11f.fffffffffff11f.......
            ......ff..fddf.fddf..ff........
            ...........ff...ff.............
            ...............................
            ...............................
            """)],
    1000,
    True)
preparar_home()
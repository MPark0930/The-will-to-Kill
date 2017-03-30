from gamelib import*

game = Game(1010,650,"The will kill")
bk = Image("images\\street2.jpg",game)
bk.resizeTo(game.width,game.height)
game.setBackground (bk)


gambitwalk = Anitmaion("images\\gambit\\gambit_walkforward",4,game) 
while not game.over:
     game.processInput()
     bk.draw()
     gambitwalk.draw()
     if keys.Pressed[K_LEFT]:
        gambitwalk.nextFrame()
        gambit.x -= 4
     if keys.Pressed[K_UP]:
        gambit.x -=4
     if keys.Pressed[K_DOWN]:
         gambit.x +=4      
     e
   
     



     game.update(50)
game.quit()


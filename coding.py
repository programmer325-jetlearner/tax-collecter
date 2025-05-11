import pgzrun
from random import randint

WIDTH=600
HEIGHT=600

money_man=Actor("money_man")
money_man.pos=300,300

money=Actor("money") 
money.pos=350,350


dollars=0

def draw():
   screen.clear()
   screen.fill("white")
   money_man.draw()
   money.draw()

   screen.draw.text(f"dollars: {dollars}",color="blue",topleft=(10,10))


def place_money():
   money.x=randint(50,WIDTH-50)
   money.y=randint(50,HEIGHT-50)

def update():
   global dollars
   if keyboard.up:
      money_man.y=money_man.y-2
   if keyboard.down:
      money_man.y=money_man.y+2
   if keyboard.right:
      money_man.x=money_man.x+2
   if keyboard.left:
      money_man.x=money_man.x-2


   if money_man.colliderect(money):
      place_money()
      dollars+=2000







pgzrun.go()
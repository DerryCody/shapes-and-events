import pygame

HEIGHT=500
WIDTH=500
TITLE="EVENTS"
 
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

class Ball():
  def __init__(self,r,c,x,y):
      self.radius=r
      self.color=c
      self.center=(x,y)
  def make(self):
    pygame.draw.circle(screen,self.color,self.center,self.radius,0)
  def grow(self):
    self.radius+=10
    
ball1=Ball(82,"Black",250,300)
ball2=Ball(57,"Pink",250,300)
ball3=Ball(34,"Yellow",250,300)
  


screen.fill('White')
run=True
while run==True:
  for event in pygame.event.get():
    if event.type==pygame.MOUSEBUTTONDOWN:
        ball1.make()
        ball2.make()
        ball3.make()
    if event.type==pygame.MOUSEBUTTONUP:
        ball1.grow()
        ball1.make()
        ball2.grow()
        ball2.make()
        ball3.grow()
        ball3.make()
    if event.type==pygame.MOUSEMOTION:
        pos=pygame.mouse.get_pos()
        ball4=Ball(5,"Blue",pos[0],pos[1])
        ball4.make()
    if event.type==pygame.QUIT:
        run=False
  pygame.display.update()

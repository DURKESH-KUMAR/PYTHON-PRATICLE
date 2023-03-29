#DURKESH KUMAR SAMPLE CODE  FOR BOUNCING BALL 

import pygame
pygame.init()
width,height=800,600
window=pygame.display.set_mode((width,height))
ball_x,ball_y=400,300
ball_speed_x,ball_speed_y=1,1
white=(225,225,225)
black=(0,0,0)
radius=50
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    ball_x+=ball_speed_x
    ball_y+=ball_speed_y
    if ball_x+radius>width or ball_x-radius<0:
        ball_speed_x*=-1
    if ball_y+radius>height or ball_y-radius<0:
        ball_speed_y*=-1
    window.fill(black)
    pygame.draw.circle(window,white,(int(ball_x),int(ball_y)),radius)
    pygame.display.update()
pygame.QUIT()

import vpython
from vpython import *

scene.caption

ball=sphere(pos=vector(0,10,0), radius=0.5, color=color.red)
floor=box(pos=vector(0,0,0),size=vector(10,0.5,10),color=color.white)
dt=1
ball.velocity=vector(0,-10,0)
t=0
while(t<20):
    rate(100)
    ball.pos=ball.pos+ball.velocity*dt
    if ball.pos.y<floor.pos.y:
        ball.velocity.y=-ball.velocity.y
    t=t+dt





'''r=vector(ball.pos)

while(r.y>0-10):
    rate(10)
    ball.pos=r
    r.y=r.y-0.5
'''
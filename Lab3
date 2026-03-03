Web VPython 3.2

# Constants
mcart = 0.8 # kg, mass of cart
mball = 0.05 # kg, mass of ball
rball = 0.02 # m, radius of the ball
deltat = 0.001 # s, time interval for updates
tf = 0.612 # s, final simulation time
F_gravity_ball = vector(0, mball*-9.8, 0) # N, force by earth on ball

# Objects
track = box(pos=vector(0, -0.05, 0), size=vector(2, 0.05, 0.1), color=color.white)
cart = box(pos=vector(track.pos.x, 0, 0), size=vector(0.1, 0.04, 0.06), color=color.yellow)
ball = sphere(pos=vector(cart.pos.x, cart.pos.y, cart.pos.z), radius=rball)

# Initial Conditions
cart_vix = 1 # m/s, initial x velocity of cart
ball_vix = cart_vix # assuming ball was moving with cart before, should have same starting velocity
ball_viy = 3 # m/s, initial y velocity of ball
pcart = mcart*vector(cart_vix,0,0) # kg*m/s
pball = mball*vector(ball_vix, ball_viy, 0) # kg*m/s
t = 0.00 # s, initial time

# Animation
while t < tf+0.001:
    rate(500)
    
    # Motion of Cart
    cart.pos = cart.pos + (pcart/mcart)*deltat
    
    # Motion of Ball
    pball = pball + F_gravity_ball*deltat
    ball.pos = ball.pos + (pball/mball)*deltat
    
    t = t + deltat

Web VPython 3.2

# Initial Conditions
vi = vector(0, 5.42, 0) # m/s, the initial speed of the ball
t = 0 # s

# Constants
g = -9.8 # m/s^2, gravitational acceleration constant
rho = 1.2 # kg/m^3, density of air
c = 0.47 # drag constant for a sphere
r = 1.3E-2 # m, radius of ball
m = 10E-3 # kg, mass of ball
A = pi*r**2 # m^2, cross-sectional area
deltat = 0.0001 # s, time interval for updates
tf = vi.y/(-g) # s, time to reach the maximum height without air resistance (added negative because g is -, time must be positive)
print(tf, ' s (time for max height without air resistance)')

# Objects
ball = sphere(pos=vector(0,0,0), radius=r, color=color.red)
floor = box(pos=vector(0, -r, 0), size=vector(2, 0.05, 0.1), color=color.white)

# Equations
v = vi
pball = m*v
F_drag = -0.5*rho*c*A*(v.mag**2)*(v.hat)
F_gravity = vector(0, m*g, 0)

scene.center = vector(0,0.75,0)

# Animation
while pball.y > 0:
    rate(10000)
    
    v = pball/m 
    F_drag = -0.5*rho*c*A*v.mag**2*v.hat  
    F_net = F_gravity + F_drag

    pball = pball + F_net*deltat
    ball.pos = ball.pos + (pball/m)*deltat

    t = t + deltat 

print(t, ' s (time for max height with air resistance)')
print((tf-t)/tf * 100, '% difference')


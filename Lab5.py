Web VPython 3.2

# Constants
G = 6.7E-11 # N*m**2/kg**2, gravitational constant
mEarth = 6.0E24 # kg, mass of Earth
mcraft = 15e3 # kg, mass of spacecraft
deltat = 60 # s
tfinal = 10*365*24*60*60 # s, 10 years
scalefactor1 = 9.0E3
scalefactor2 = 0.3

# Objects & Initial Values
Earth = sphere(pos=vector(0,0,0),radius=6.4E6,color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius,0,0),radius=1E6,color=color.yellow)
trail = curve(color=color.white)

# Equations
r = craft.pos-Earth.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
FGmag = (G*mcraft*mEarth)/(rmag**2)
rhat = r/rmag
FG = -FGmag*rhat
Fnet = FG

v_circular_orbit = sqrt((G*mEarth)/(10*Earth.radius))
print("speed necessary for circular orbit: ", v_circular_orbit, " m/s")

vcraft = vector(0,v_circular_orbit,0) # m/s, initial velocity
pcraft = mcraft*vcraft # kg*m/s, initial momentum
gravArrow = arrow(pos = craft.pos, axis = Fnet*scalefactor1, color = color.white)
pArrow = arrow(pos = craft.pos, axis = pcraft*scalefactor2, color = color.yellow)

# Iterative Calculations
t = 0
while t < tfinal:
    rate(1000) # animation rate (frames/second)
    r = craft.pos-Earth.pos
    rmag = r.mag #sqrt(r.x**2 + r.y**2 + r.z**2)
    FGmag = (G*mcraft*mEarth)/(rmag**2)
    rhat = r.hat #r/rmag
    FG = -FGmag*rhat
    Fnet = FG
    
    pcraft = pcraft + (Fnet*deltat)
    
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    trail.append(pos=craft.pos) 
    
    gravArrow.pos = craft.pos
    gravArrow.axis = Fnet*scalefactor1
    pArrow.pos = craft.pos
    pArrow.axis = pcraft*scalefactor2
    
    if(rmag < Earth.radius):
        break
    
    t = t + deltat

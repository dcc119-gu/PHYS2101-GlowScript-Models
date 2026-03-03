Web VPython 3.2

# Constants
G = 6.7E-11 # N*m**2/kg**2, gravitational constant
mEarth = 6.0E24 # kg, mass of Earth
mcraft = 9600 # kg, mass of spacecraft
mEffective = mEarth # kg, effective mass of the earth (useful for when spacecraft is inside the earth)
deltat = 60 # s
tfinal = 24*60*60 # s 10 years
scalefactor1 = 1.5E2
scalefactor2 = 0.5E-1

# Objects & Initial Values
Earth = sphere(pos=vector(0,0,0),radius=6.4E6,color=color.cyan,opacity=0.5)
craft = sphere(pos=vector(-Earth.radius,0,0),radius=1E6,color=color.yellow)
trail = curve(color=color.white) # trail object to show the craft's trajectory

# Equations
r = craft.pos-Earth.pos
rmag = sqrt(r.x**2 + r.y**2 + r.z**2)
FGmag = (G*mcraft*mEarth)/(rmag**2)
rhat = r/rmag
FG = -FGmag*rhat
Fnet = FG

vcraft = vector(0,0,0) # m/s, initial velocity
pcraft = mcraft*vcraft # kg*m/s, initial momentum
gravArrow = arrow(pos = craft.pos, axis = Fnet*scalefactor1, color = color.white)
pArrow = arrow(pos = craft.pos, axis = pcraft*scalefactor2, color = color.yellow)

# Iterative Calculations
t = 0 
while t < tfinal:
    rate(10)
    r = craft.pos-Earth.pos
    rmag = r.mag #sqrt(r.x**2 + r.y**2 + r.z**2)
    if(rmag < Earth.radius):
        mEffective = mEarth*((rmag/Earth.radius)**3)
    else:
        mEffective = mEarth
    
    FGmag = (G*mcraft*mEffective)/(rmag**2)
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
    
    t = t + deltat

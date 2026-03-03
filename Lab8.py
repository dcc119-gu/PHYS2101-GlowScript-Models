Web VPython 3.2

# Constants
G = 6.7E-11 # N*m**2/kg**2, gravitational constant
mEarth = 6.0E24 # kg, mass of Earth
mmoon = 7.0E22 # kg, mass of moon
mcraft = 15e3 # kg, mass of spacecraft
deltat = 0.1 # s, timestep for iterative calculation
tfinal = 60*24*60*60 # s, how much time is this?
scalefactor1 = 9.0E3
scalefactor2 = 0.3

# Objects & Initial Values
Earth = sphere(pos=vector(0,0,0),radius=6.4E6,color=color.cyan)
moon = sphere(pos=vector(Earth.pos.x+4.0E8,0,0),radius=1.75E6,color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius,0,0),radius=1E6,color=color.yellow)
trail = curve(color=color.white) # trail object to show the craft's trajectory

scene.center = (Earth.pos+moon.pos)/2

# Earth Force
rEarth = craft.pos-Earth.pos
rmagEarth = sqrt(rEarth.x**2 + rEarth.y**2 + rEarth.z**2)
FGmagEarth = (G*mcraft*mEarth)/(rmagEarth**2)
rhatEarth = rEarth/rmagEarth
FGEarth = -FGmagEarth*rhatEarth

# Moon Force
rmoon = craft.pos-moon.pos
rmagmoon = rmoon.mag #sqrt(rmoon.x**2 + rmoon.y**2 + rmoon.z**2)
FGmagmoon = (G*mcraft*mmoon)/(rmagmoon**2)
rhatmoon = rmoon/rmagmoon
FGmoon = -FGmagmoon*rhatmoon
# Net force on spacecraft
Fnet = FGEarth + FGmoon

# crash speed = 3.285E3 m/s, figure eight speed = 3.274E3 m/s

vcraft = vector(0,3281,0) # m/s, initial velocity
pcraft = mcraft*vcraft # kg*m/s, initial momentum
#gravArrow = arrow(pos = craft.pos, axis = Fnet*scalefactor1, color = color.white)
#pArrow = arrow(pos = craft.pos, axis = pcraft*scalefactor2, color = color.yellow)

K = (pcraft.mag**2)/(2*mcraft) # J, kinetic energy
U = (-G*mcraft*mEarth)/(rmagEarth) # J, potential energy
E = K + U # J, total system energy
print("initial energy = {:13.7E} J".format(E))

# HOMEWORK 8 CALCULATIONS
# Calculation (from pen and paper solution)
vf = sqrt((3281)**2 + 2*G*(((6E24)/(4E8-1.75E6) + (7E22)/(1.75E6)) - ((6E24)/(6.4E7) + (7E22)/(6.4E7+4E8))))
print("speed just before crash: ", vf, " m/s")

# vi = 2.3582993E+3 m/s, deltat=0.1s

# Iterative Calculations
t = 0 # initial time, in seconds
while t < tfinal:
    #rate(100000)
    rEarth = craft.pos-Earth.pos
    rmagEarth = rEarth.mag #sqrt(r.x**2 + r.y**2 + r.z**2)
    FGmagEarth = (G*mcraft*mEarth)/(rmagEarth**2)
    rhatEarth = rEarth.hat #r/rmag
    FGEarth = -FGmagEarth*rhatEarth
    
    rmoon = craft.pos-moon.pos
    rmagmoon = rmoon.mag #sqrt(r.x**2 + r.y**2 + r.z**2)
    FGmagmoon = (G*mcraft*mmoon)/(rmagmoon**2)
    rhatmoon = rmoon.hat #r/rmag
    FGmoon = -FGmagmoon*rhatmoon
    
    Fnet = FGEarth + FGmoon
    pcraft = pcraft + (Fnet*deltat)
    craft.pos = craft.pos + (pcraft/mcraft)*deltat

    K = (pcraft.mag**2)/(2*mcraft)
    U = (-G*mcraft*mEarth)/(rmagEarth)
    #Kgraph.plot(pos=(rEarth.mag,K)) # add a point to the kinetic energy graph
    #Ugraph.plot(pos=(rEarth.mag,U)) # add a point to the potential energy graph
    #KplusUgraph.plot(pos=(rEarth.mag,K+U)) # add a point to the K + U graph
    
    if(rmagEarth < Earth.radius):
        break
    
    if(rmagmoon < moon.radius):
        break
    
    t = t + deltat
    
print('time, speed{:13.7E} s, {:13.7E} m/s'.format(t,pcraft.mag/mcraft))
    
    

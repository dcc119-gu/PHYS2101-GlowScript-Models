Web VPython 3.2

# 1. momentum =  7.6132826E+7 kg*m/s
# 2. U(0) / U(R_E) = 1.50064

# Constants
G = 6.7E-11 # N*m**2/kg**2, gravitational constant
mEarth = 6.0E24 # kg, mass of Earth
mcraft = 9600 # kg, mass of spacecraft
mEffective = mEarth # kg, effective mass of the earth (useful for when spacecraft is inside the earth)
deltat = 60 # s
tfinal = 24*60*60 # s, 10 years
scalefactor1 = 1.5E2
scalefactor2 = 0.5E-1

# Objects & Initial Values
Earth = sphere(pos=vector(0,0,0),radius=6.4E6,color=color.cyan,opacity=0.5)
craft = sphere(pos=vector(-Earth.radius,0,0),radius=1E6,color=color.yellow)
trail = curve(color=color.white) # trail object to show the craft's trajectory

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

# ADDITIONS FROM LAB 7
U = (-G*mEarth*mcraft)/(r.mag) # calculate initial gravitational potential energy
KE = 0 # kinetic energy is 0 at the start because the craft moves from rest!
TE = KE + U # total energy is the sum of all energies in system (kinetic + potential)
U_rE = TE - ((1/2)*(pcraft.mag**2/mcraft)) # given energy principle, energy in system is conserved, so GPE can be derived by total energy - kinetic energy; calculate U_re here since it starts at surface of the earth

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
    
    # NEW ADDITIONS - LAB 7
    if (craft.pos.x >= Earth.pos.x): # when craft reaches center of earth
        U_0 = TE - ((1/2)*(pcraft.mag**2/mcraft)) # same idea as above - use the energy principle to find current potential energy from total energy and current kinetic energy
        print(U_0/U_rE)
    # To find |p| at center of earth:
        print("momentum = {:13.7E} kg*m/s".format(pcraft.mag))
        break
      
    t = t + deltat
    
    

    
    

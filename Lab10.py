Web VPython 3.2

# HOMEWORK COMMENTS AND OBSERVATIONS
# Same period measured in computational model,
# Calculated the period using mu (printed in window). To assess period of computational model, made another gcurve that plotted position of ball A.
# Using this graph, looked at the time when ball A completed one cycle and returned to original position. Period from this method was same as theoretical period (also printed out).
# Period obtained in both cases was 1.75E-14.

# Constants
g = 0 # N/kg
mballB =  2.32E-26 # kg, mass of single nitrogen atom
mballA = 2.32E-26 # kg
k = 1500 # N/m
L0 = 1.2E-10 # m, approximate bond length of nitrogen molecule

# Equations
mu = (mballA*mballB) / (mballA + mballB)
omega = sqrt(k / mu)
hbar = 1.054E-34 # joule seconds
Ki_vib = hbar * omega

v_rel = sqrt(2*Ki_vib / mu) # derived from equation K = 1/2 mu * v^2
p_rel = mu * v_rel

period = 2*pi*sqrt(mu/k) # s
print(period)
tfinal = 4*period # s
deltat = 1E-3*period # s

# Objects
ballA = sphere(pos=vector(0,0,0),radius=2E-11,axis=vector(0.2,0,0),color=color.red)
spring = helix(pos=ballA.pos,axis=vector(0,-L0,0),radius=2E-11,coils=20,color=color.white)
ballB = sphere(pos=spring.pos+spring.axis,radius=2E-11,color=color.blue)

trailA = curve()
trailB = curve()
trailCM = curve()

scene.center = ballB.pos
scene.range = 3*L0 

# Initial Values
spring.axis = ballB.pos - spring.pos
pballA = vector(0,-p_rel,0)
pballB = vector(0,p_rel,0)
t = 0

gKtot = gcurve(color=color.red)
gKCM = gcurve(color=color.green)
gUspr = gcurve(color=color.cyan)
gEint = gcurve(color=color.blue)
gE = gcurve(color=color.black)
gApos = gcurve(color=color.yellow)

# Iterative Calculations
while t < tfinal :
    rate(1000)
    
    L = spring.axis # or just spring.axis
    s = L.mag - L0

    Fs = k*s*(-L.hat)
    Fg = vector(0,-mballB*g,0)
    FnetB = Fs + Fg
    
    pballB = pballB + FnetB*deltat
    ballB.pos = ballB.pos + (pballB/mballB)*deltat

    FnetA = Fg - Fs
    pballA = pballA + FnetA*deltat
    ballA.pos = ballA.pos + (pballA/mballA)*deltat
    
    spring.pos = ballA.pos
    spring.axis = ballB.pos - spring.pos
    
    r_CM = ((mballA*ballA.pos)+(mballB*ballB.pos))/(mballA+mballB)
  
    trailA.append(pos=ballA.pos, color=color.red, radius=5E-12)
    trailB.append(pos=ballB.pos, color=color.blue, radius=5E-12)
    trailCM.append(pos=r_CM, color=color.green, radius=5E-12)
    
    # Energy Calculations & Subsequent Graph Updates
    Ktot = (pballA.mag**2/(2*mballA)) + (pballB.mag**2/(2*mballB))
    gKtot.plot(t, Ktot)
    
    KCM = ((((pballA) + (pballB)).mag**2) / (2*(mballA + mballB)))
    gKCM.plot(t, KCM)
    
    Uspr = k*(s**2) / 2
    gUspr.plot(t, Uspr)
    
    Eint = (Ktot - KCM) + Uspr # Ktot - K_CM is K relative
    gEint.plot(t, Eint)
    
    E = Ktot + Uspr
    gE.plot(t, E)
    
    gApos.plot(t, ballA.pos.y)
    
    t = t + deltat

Web VPython 3.2

# RESULT: T_model = 0.833 seconds

# Constants
g = 9.8 # m/s^2, acceleration constant for gravity on earth
k = 11.50 # N/m 
L0 = 0.15 # m, length of the relaxed spring
A = 0.04 # m, amplitude of spring's oscillation
m = 0.200 # kg, mass of bob on spring
ytop = 1.0 # m, y position of where spring hangs from
rspring = 0.02 # m, radius of spring

ybob = ytop - L 
rbob = 0.02 

# Equations
s = m*g/k + A 
L = L0 + s 

# Objects
spring = helix(pos=vector(0,ytop,0),axis=vector(0,-L,0),radius=rspring,coils=20,color=color.white)
bob = sphere(pos=vector(0,ybob,0),radius=rbob,color=color.red)

scene.center = vector(0,ybob,0) 
scene.range = 3*L0 

pbob = vector(0,0,0) # initial momentum of bob

print("initial location of bob =",bob.pos.y,"m")

# Animation & Updates
t = 0 
tfinal = 10 
deltat = 0.001 
while t < tfinal : 
    rate(1000) 
    L = ytop - bob.pos.y
    s = L - L0 
    Fs = k*s*vector(0,1,0) 
    Fg = m*g*vector(0,-1,0) 

    Fnet = Fs + Fg 
    pbob = pbob + Fnet*deltat 
    bob.pos = bob.pos + (pbob/m)*deltat 
    spring.axis = vector(0,-L,0) 

    t = t + deltat

print("final location of bob =",bob.pos.y,"m") 
print("elapsed time =",t,"s") 

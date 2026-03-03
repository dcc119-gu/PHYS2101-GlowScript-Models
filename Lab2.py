Web VPython 3.2

x = -2 
while (x < 2.5):
    x = x + 0.5 
    sphere(pos = vector(x, 0, 0), radius = 0.05, color = color.yellow) # 0.05 m radius corresponds to 0.1 m diameter, yellow spheres
    if (x < 2.5):
        arrow(pos = vector(x, 0, 0), axis = vector(0.5, 0, 0), color = color.green)

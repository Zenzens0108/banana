import math as m
    
for i in range(0, 181, 10):    
    print(f"sin({i}) = {m.sin(m.pi/180*i):.3f}, cos({i}) = {m.cos(m.pi/180*i):.3f}, tan({i}) = {m.tan(m.pi/180*i):.3f}")
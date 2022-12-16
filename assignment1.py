import math

# Input number of points
n = int(input("Enter number of polygon points: "))

# Lists that store all entered coordinates
xs = []
ys = []

print("\nEnter x and y coordinates for polygon points ...")
for i in range(n):
    print(f"\nPoint {i+1}: ")
    x = float(input(f"x{i+1}: "))
    xs.append(x)
    y = float(input(f"y{i+1}: "))
    ys.append(y)
ys.append(ys[0])
xs.append(xs[0])


# Print a table of entered data and calculated values
print()
print(f"{'point':>5} {'x':>10} {'y':>10} ")
print("-" * 30)
for i in range(n):
    print(f"Point{i + 1:5} {xs[i]:10.2f} {ys[i]:10.2f}")

# Calculate sum area
print()
Ax = 0.0
Sx = 0.0
Sy = 0.0
Ix = 0.0
Iy = 0.0
Ixy = 0.0


for i in range(n):
    Ax = Ax+(xs[i+1]+xs[i])*(ys[i+1]-ys[i])/2
    Sx = Sx-(xs[i+1]-xs[i])*(ys[i+1]**2+ys[i+1]*ys[i]+ys[i]**2)/6
    Sy = Sy+(ys[i+1]-ys[i])*(xs[i+1]**2+xs[i+1]*xs[i]+xs[i]**2)/6
    Ix = Ix-(xs[i+1]-xs[i])*(ys[i+1]**3+ys[i+1] **
                             2*ys[i]+ys[i+1]*ys[i]**2+ys[i]**3)/12
    Iy = Iy+(ys[i+1]-ys[i])*(xs[i+1]**3+xs[i+1] **
                             2*xs[i]+xs[i+1]*xs[i]**2+xs[i]**3)/12
    Ixy = Ixy-(ys[i+1]-ys[i])*(ys[i+1]*(3*xs[i+1]**2+2*xs[i+1]*xs[i] +
                                        xs[i]**2)+ys[i]*(3*xs[i]**2+2*xs[i+1]*xs[i]+xs[i+1]**2))/24

xt = Sy/Ax
yt = Sx/Ax
Ixt = Ix-yt**2*Ax
Iyt = Iy-xt**2*Ax
Ixyt = Ixy+xt*yt*Ax

# Geometric characteristics
print("Geometric characteristics:")
print()
print(f"Ax={Ax:.2f}")
print(f"Sx={Sx:.2f}")
print(f"Sy={Sy:.2f}")
print(f"Ix={Ix:.2f}")
print(f"Iy={Iy:.2f}")
print(f"Ixy={Ixy:.2f}")
print(f"xt={xt:.2f}")
print(f"yt={yt:.2f}")
print(f"Ixt={Ixt:.2f}")
print(f"Iyt={Ixt:.2f}")
print(f"Ixyt={Ixyt:.2f}")

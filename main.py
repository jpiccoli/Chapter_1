import matplotlib.pyplot as plt

def ball_trajectory(x):
    location = 10 *x - 5 * (x**2)
    return location

xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]

# Line 1
xs2 = [0.1,2]
ys2 = [ball_trajectory(0.1),0]

# Line 2
xs3 = [0.2,2]
ys3 = [ball_trajectory(0.2),0]

# Line 3
xs4 = [0.3,2]
ys4 = [ball_trajectory(0.3),0]

# Side 'A' of triangle
xs5 = [0.3,0.3]
ys5 = [0,ball_trajectory(0.3)]

# Side 'B' triangle
xs6 = [0.3,2]
ys6 = [0,0]

plt.plot(xs,ys,xs2,ys2,xs3,ys3,xs4,ys4,xs5,ys5,xs6,ys6)
plt.title('The Trajectory Of A Thrown Ball - Tangent Calculation')
plt.text(0.31, ball_trajectory(0.3)/2, 'A', fontsize = 16)
plt.text((0.3 + 2)/2, 0.05, 'B', fontsize = 16)
plt.xlabel('Horizontal Position Of Ball')
plt.ylabel('Vertical Position Of Ball')
plt.axhline(y = 0)
plt.show()

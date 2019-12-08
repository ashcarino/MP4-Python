import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v,h,thetaD,Ax,Ay):
    if Ay == 0:
        print ("Error: vertical acceleration is equal to 0")
        return
    theta = np.radians(thetaD)
    Vx = v*np.cos(theta)
    Vy = v*np.sin(theta)
    X = []
    Y = []
    
    t = 0
    x = 0
    y = h
    dt = 0.01
    X.append(x)
    Y.append(y)
    
    while(True):
        t = t + dt
        x = Vx * t + (0.5) * Ax * t * t
        y = Vy * t + (0.5) * Ay * t * t + h
        
        X.append(x)
        Y.append(y)
        
        if y < dt:
            break
        
    plt.plot(X,Y)
    Ax = plt.gca()
    Ax.set_ylim([0,max(Y)])
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title('Projectile motion')
    plt.grid()
    plt.show()
    
if __name__ == '__main__':
    v = 5 # in m/s
    h = 7 # in meters
    Ax = 0 # in m/s**2
    Ay = -9.81 # in m/s**2
    thetaD = 30 # in degree w.r.t to +x-axis
    projectile_motion(v,h,thetaD,Ax,Ay)

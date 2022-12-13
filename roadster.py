import matplotlib
import numpy as np
from scipy import interpolate
import roadster
import matplotlib.pyplot as plt

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    #raise NotImplementedError('consumption not implemented yet!')
    a = [546.8, 50.31, 0.2548, 0.008210]
    # a = np.array([546.8, 50.31, 0.2584, 0.008210])
    cons = a[0]*v**(-1) + a[1] + a[2]*v**1 + a[3]*v**2
    return cons

def plot_1a():
    # distance_km = load_route(route)
    # x = np.array(distance_km)
    # v = velocity(x, route)
    v = np.linspace(0,200,800)
    cons = consumption(v)
    plt.scatter(v, cons, s = 3)
    plt.xlabel('Speed (km/h)')
    plt.ylabel('Energy consumption')
    plt.show()

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

def plt_wointerpol(route):
    distance_km, speed_kmph = load_route(route)
    x=np.array(distance_km)
    v =np.array(speed_kmph)
    plt.scatter(x, v, s=1)
    plt.title("Dot Plot without Interpolation")
    plt.xlabel('Distance Traveled (km)')
    plt.ylabel('Recorded Speed(km/h)')
    plt.show()

def plot_interpol(route):
    distance_km, speed_kmph = load_route(route)
    x=np.array(distance_km)
    v = velocity(x, route)
    plt.plot(x, v)
    plt.title("Plot with Interpolation")
    plt.xlabel('Distance Traveled (km)')
    plt.ylabel('Velocity (km/h)')
    plt.show()
    

### PART 2A ###
def time_to_destination(x, route, n):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('time_to_destination not implemented yet!')

### PART 2B ###
def total_consumption(x, route, n):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('total_consumption not implemented yet!')

### PART 3A ###
def distance(T, route): 
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('distance not implemented yet!')

### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')


if __name__ == "__main__":
    #distance_km, speed_kmph = load_route('speed_anna')
    #x=np.array(distance_km)
    #print(velocity(x,'speed_anna'))
    #help(roadster.load_route)
    #plt_wointerpol('speed_anna')
    #plot_1a('Consumption as a function of speed')
    plot_1a()

import math
import matplotlib.pyplot as plt

def generate_v_formation(Z, X, formation_angle_deg=30):
   
    
    
    k = int(Z / X)
    positions = []
    
    
    leader = (0, 0)
    positions.append(leader)
    
   
    angle_rad = math.radians(formation_angle_deg)
    
    
    for i in range(1, k + 1):
       
        x_left = -i * X * math.cos(angle_rad)
        y_left = i * X * math.sin(angle_rad)
        positions.append((x_left, y_left))
        
       
        x_right = i * X * math.cos(angle_rad)
        y_right = i * X * math.sin(angle_rad)
        positions.append((x_right, y_right))
    
    return positions

def plot_formation(positions):
    xs, ys = zip(*positions)
    plt.figure(figsize=(8, 6))
    
    
    plt.scatter(xs, ys, c='blue')
    
    
    plt.scatter(xs[0], ys[0], c='red', marker='*', s=200, label="Lider")
    
   
    for i, (x, y) in enumerate(positions):
        plt.text(x, y, f" {i}", fontsize=12)
    
    plt.title("V Formasyon")
    plt.xlabel("X Koordinat (m)")
    plt.ylabel("Y Koordinat (m)")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
 
    Z = 5               
    X = 1.0             
    formation_angle_deg = 30  
    T = 10              

    positions = generate_v_formation(Z, X, formation_angle_deg)
    
 
    plot_formation(positions)
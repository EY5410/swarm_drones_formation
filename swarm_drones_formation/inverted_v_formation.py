import matplotlib.pyplot as plt

def generate_arrowhead_formation(Z, X):
   
    positions = []
    
   
    leader = (0, 0)
    positions.append(leader)
    
   
    k = int(Z / X)
    
    
    for row in range(1, k + 1):
       
        num_drones_in_row = 2 * row
        
    
        y = -row * X
        
        
        for i in range(num_drones_in_row):
            x = -(num_drones_in_row - 1) * X / 2 + i * X
            positions.append((x, y))
    
    return positions

def plot_formation(positions):
    xs, ys = zip(*positions)
    plt.figure(figsize=(8, 6))
    
    
    plt.scatter(xs, ys, c='blue')
    
    
    plt.scatter(xs[0], ys[0], c='red', marker='*', s=200, label="Lider")
    

    for i, (x, y) in enumerate(positions):
        plt.text(x, y, f" {i}", fontsize=12)
    
    plt.title("Ok Ucu Formasyon")
    plt.xlabel("X Koordinat (m)")
    plt.ylabel("Y Koordinat (m)")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    
    Z = 10               
    X = 1.5              
    
   
    positions = generate_arrowhead_formation(Z, X)
    
  
    plot_formation(positions)
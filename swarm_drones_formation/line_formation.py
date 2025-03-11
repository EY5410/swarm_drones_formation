import matplotlib.pyplot as plt

def generate_vertical_line_formation(N, X):
   
    positions = []
    
    
    start_y = -((N - 1) * X / 2)  
    for i in range(N):
        x = 0                 
        y = start_y + i * X   
        positions.append((x, y))
    
    return positions

def plot_formation(positions):
    
    xs, ys = zip(*positions)
    plt.figure(figsize=(4, 8)) 
    plt.scatter(xs, ys, c='blue', label="Drone")
    
    
    plt.scatter(xs[0], ys[0], c='red', marker='*', s=200, label="Lider")
    
    
    for i, (x, y) in enumerate(positions):
        plt.text(x + 0.1, y, f" {i}", fontsize=10)
    
    plt.title("Dikey Çizgi Formasyonu")
    plt.xlabel("X Koordinat (m)")
    plt.ylabel("Y Koordinat (m)")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()

if __name__ == '__main__':
    
    N = 10               
    X = 2                
    

    positions = generate_vertical_line_formation(N, X)
    

    plot_formation(positions)
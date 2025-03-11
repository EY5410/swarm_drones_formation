import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def line_formation_positions(X):
   
    return [(0, 0), (-X, 0), (X, 0)]

def arrowhead_formation_positions(X):
  
    
    return [(0, 0), (-X, -X), (X, -X)]

def v_formation_positions(X, formation_angle_deg=30):
  
    theta = math.radians(formation_angle_deg)
    left = (-X * math.sin(theta), X * math.cos(theta))
    right = (X * math.sin(theta), X * math.cos(theta))
    return [(0, 0), left, right]

def update(frame, dt, X, scatter_leader, scatter_others, ax):
   
    current_time = frame * dt
    period = 10.0        
    cycle = 3 * period   
    formation_idx = int((current_time % cycle) // period)
    
    if formation_idx == 0:
        formation_name = "Çizgi Formasyonu"
        positions = line_formation_positions(X)
    elif formation_idx == 1:
        formation_name = "Ok Ucu Formasyonu"
        positions = arrowhead_formation_positions(X)
    else:
        formation_name = "V Formasyonu"
        positions = v_formation_positions(X, formation_angle_deg=30)
        
    scatter_leader.set_offsets([positions[0]])
    scatter_others.set_offsets(positions[1:])
    
    ax.set_title(f"{formation_name} (t = {current_time:.1f} s)")
    return scatter_leader, scatter_others

def main():
    X = 2              
    T_total = 60        
    dt = 0.1            
    frames = int(T_total / dt)
    
    
    init_positions = line_formation_positions(X)
    
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)  
    ax.grid(True)
    
    
    scatter_leader = ax.scatter([init_positions[0][0]], [init_positions[0][1]],
                                c='red', marker='*', s=200, label="Lider")
    others_x = [pos[0] for pos in init_positions[1:]]
    others_y = [pos[1] for pos in init_positions[1:]]
    scatter_others = ax.scatter(others_x, others_y, c='blue', label="Drone")
    
    ax.legend()
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=frames,
        fargs=(dt, X, scatter_leader, scatter_others, ax),
        interval=dt * 1000,  
        blit=False,
        repeat=True
    )
    
    plt.show()

if __name__ == '__main__':
    main()
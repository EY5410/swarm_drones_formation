import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


num_drones = 3        
dt = 0.1             
max_speed = 2.0       
separation_distance = 1.0  
k_separation = 0.5    
k_alignment = 0.05   
k_cohesion = 0.01     


positions = np.random.uniform(-5, 5, (num_drones, 2))

velocities = np.random.uniform(-1, 1, (num_drones, 2))

def limit_speed(v, max_speed):
   
    speed = np.linalg.norm(v)
    if speed > max_speed:
        return (v / speed) * max_speed
    return v

def update_boids(positions, velocities):
   
    new_velocities = np.copy(velocities)
    
    for i in range(num_drones):
        pos_i = positions[i]
        vel_i = velocities[i]
        
        
        separation_force = np.zeros(2)
        alignment_force = np.zeros(2)
        cohesion_force = np.zeros(2)
        count_neighbors = 0
        
        for j in range(num_drones):
            if i == j:
                continue
                
            pos_j = positions[j]
            vel_j = velocities[j]
            distance = np.linalg.norm(pos_i - pos_j)
            
       
            if distance < separation_distance:
        
                separation_force += (pos_i - pos_j) / (distance + 1e-5)
            
     
            alignment_force += vel_j
            
       
            cohesion_force += pos_j
            count_neighbors += 1
        
        if count_neighbors > 0:
            alignment_force = alignment_force / count_neighbors - vel_i
            cohesion_force = (cohesion_force / count_neighbors - pos_i)
        
      
        steering = k_separation * separation_force + k_alignment * alignment_force + k_cohesion * cohesion_force
        
        new_velocities[i] = vel_i + steering
        new_velocities[i] = limit_speed(new_velocities[i], max_speed)
    

    new_positions = positions + new_velocities * dt
    return new_positions, new_velocities


fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Serbest Formasyon (Free Formation)")
ax.grid(True)


scatter = ax.scatter(positions[:, 0], positions[:, 1], c='blue', s=100)

def animate(frame):
    global positions, velocities
    positions, velocities = update_boids(positions, velocities)
    scatter.set_offsets(positions)
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=300, interval=dt*1000, blit=True, repeat=True)
plt.show()
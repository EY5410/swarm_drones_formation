import numpy as np
import math



def line_formation_positions_3D(X):
    
    return np.array([
        (0, 0, 0),
        (0, -X, 0),
        (0, X, 0)
    ])

def arrowhead_formation_positions_3D(X):
    
    return np.array([
        (0, 0, 0),
        (-X, -X, 0),
        (X, -X, 0)
    ])

def v_formation_positions_3D(X, formation_angle_deg=30):
   
    theta = math.radians(formation_angle_deg)
    left = (-X * math.sin(theta), X * math.cos(theta), 0)
    right = (X * math.sin(theta), X * math.cos(theta), 0)
    return np.array([
        (0, 0, 0),
        left,
        right
    ])



def update_free_formation_3D(positions, velocities, dt, max_speed,
                               separation_distance, k_separation,
                               k_alignment, k_cohesion):
    
    new_velocities = np.copy(velocities)
    num_drones = positions.shape[0]
    
    for i in range(num_drones):
        pos_i = positions[i]
        vel_i = velocities[i]
        separation_force = np.zeros(3)
        alignment_force = np.zeros(3)
        cohesion_force = np.zeros(3)
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
        
        steering = k_separation * separation_force \
                   + k_alignment * alignment_force \
                   + k_cohesion * cohesion_force
        
        new_velocities[i] = vel_i + steering
        
        
        speed = np.linalg.norm(new_velocities[i])
        if speed > max_speed:
            new_velocities[i] = (new_velocities[i] / speed) * max_speed

    new_positions = positions + new_velocities * dt
    return new_positions, new_velocities


def main():
    num_drones = 3
    dt = 0.1       
    T_total = 40.0 
    
    max_speed = 2.0
    separation_distance = 1.0
    k_separation = 0.5
    k_alignment = 0.05
    k_cohesion = 0.01
    X = 2.0      
    
    
    positions = np.random.uniform(-5, 5, (num_drones, 3))
    velocities = np.random.uniform(-1, 1, (num_drones, 3))
    
    t = 0.0
    step = 0
    print("Simülasyon Başladı:")
    print("-" * 40)
    
    while t < T_total:
        
        if t < 10:
            formation = "Serbest Formasyon (3D)"
            positions, velocities = update_free_formation_3D(positions, velocities, dt,
                                                             max_speed, separation_distance,
                                                             k_separation, k_alignment, k_cohesion)
        elif t < 20:
            formation = "Dikey Çizgi Formasyonu (3D)"
            positions = line_formation_positions_3D(X)
            velocities = np.zeros((num_drones, 3))
        elif t < 30:
            formation = "Ok Ucu Formasyonu (3D)"
            positions = arrowhead_formation_positions_3D(X)
            velocities = np.zeros((num_drones, 3))
        else:
            formation = "V Formasyonu (3D)"
            positions = v_formation_positions_3D(X, formation_angle_deg=30)
            velocities = np.zeros((num_drones, 3))
        
        
        if step % int(1 / dt) == 0:
            print(f"Time = {t:.1f} s, Formation: {formation}")
            for i, pos in enumerate(positions):
                print(f" Drone {i}: {pos}")
            print("-" * 40)
        
        t += dt
        step += 1

if __name__ == '__main__':
    main()
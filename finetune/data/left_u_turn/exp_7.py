def left_u_turn():
    duration = 5 # turning time (seconds) for a quarter turn
    radius = 3 # turning radius (meters)
    radian = math.pi/2 # 90 degrees in radians
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time() # current time in seconds
    
    # Do the left u-turn, which includes two left 90-degree turns
    for i in range(2):
        while (time.time() - start_time) - stopping_time < duration:
            if pedestrian_observed():
                stop()
                stopping_time += time.time() - start_time
            else:
                # Calculate velocities 
                angular = radian / duration # angular velocity (rad/s)
                linear = radius * angular # linear velocity (m/s)
                
                velocity_publisher(linear, angular) # Publish velocities to robot

def turn_right_30_degree():
    start_time = time.time()
    period = 5 # Duration to complete the turn, in seconds
    turn_radius = 3 # The radius of the turn, in meters
    radian = -math.pi / 6 # 30 degrees clockwise is -pi/6 radians
    angular = radian / period # Angular velocity in radians/second
    linear = turn_radius * angular # Linear velocity in meters/second
    stopping_time = 0 # Time spent stopped for pedestrians
    
    while (time.time() - start_time) < period + stopping_time:
        time_at = time.time()
        while pedestrian_observed():
            sleep(0.5) # Stop the vehicle if a pedestrian is observed
        stopping_time += time.time() - time_at # Accumulate stopping time
        if within_speed_limit(linear, angular):
            velocity_publisher(linear, angular) # Publish the velocity commands
        else:
            sleep(0.5)
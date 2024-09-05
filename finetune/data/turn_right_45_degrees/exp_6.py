def turn_right_45_degrees():
    turn_duration = 5     # Turning time/duration in seconds
    turn_radius = 3       # Turning radius in meters
    turn_angle_radians = math.pi / 4    # Turning angle in radians (45 degrees)
    
    angular_velocity = -turn_angle_radians / turn_duration # Angular velocity in radians/sec. Negative because it's a right turn.
    linear_velocity = turn_radius * angular_velocity    # Linear velocity in meters/sec
    
    stopping_time = 0     # Initial time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < turn_duration:
        time_at_vel_pub = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at_vel_pub
        else:
            velocity_publisher(linear_velocity, angular_velocity)

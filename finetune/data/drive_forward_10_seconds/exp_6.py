def drive_forward_10_seconds():
    duration = 10    # driving time/duration in seconds
    linear_velocity = 1  # One possible speed (m/s), change according to your needs
    angular_velocity = 0  # Car is moving straight, so no angular velocity
    stopping_time = 0    # Time spent stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        current_time = time.time() 

        if pedestrian_observed():
            stop()    
            stopping_time += time.time() - current_time
        else:
            velocity_publisher(linear_velocity, angular_velocity)

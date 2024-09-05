def drive_forward_10_seconds():
    duration = 10 # driving time (seconds)
    linear = 1 # Change according to car's capabilities and requirements (m/s)
    angular = 0 # Going straight so the angular velocity is 0 (rad/s)
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            # Increment the stopping time 
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)

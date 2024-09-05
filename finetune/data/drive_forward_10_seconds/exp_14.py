def drive_forward_10_seconds():
    drive_duration = 10  # driving time in seconds
    stopping_time = 0  # total time stopped for pedestrians
    linear_velocity = 1  # linear velocity (m/s)
    angular_velocity = 0  # angular velocity (rad/s) as the vehicle is going straight
    
    start_time = time.time()  # save the start time
    
    while (time.time() - start_time) - stopping_time < drive_duration:
        if pedestrian_observed():
            stop()  # a pedestrian is observed, stop the car
            stopping_time += time.time() - start_time
        else:
            velocity_publisher(linear_velocity, angular_velocity)  # pedestrian is not observed, continue to drive      

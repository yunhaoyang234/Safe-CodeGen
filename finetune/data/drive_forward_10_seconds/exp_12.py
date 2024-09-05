def drive_forward_10_seconds():
    
    forward_speed = 1.0  # meters per second (as an example, change as required)
    rotation_speed = 0.0  # no rotation as we are moving straight
    
    stopping_time = 0
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < 10:
        time_at_check = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at_check
        else:
            velocity_publisher(forward_speed, rotation_speed)
    stop()  # to ensure the robot is stopped at the end

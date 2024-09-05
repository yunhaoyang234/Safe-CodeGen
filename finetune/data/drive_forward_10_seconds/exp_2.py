def drive_forward_10_seconds():
    forward_speed = 1.0  # linear speed of 1 meter per second. Adjust as needed.
    spin_speed = 0.0  # no spinning, only forward motion
    duration = 10  # drive duration in seconds
    stopping_time = 0  # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        current_time = time.time()
        if pedestrian_observed():
            stop()  # stop the robot if a pedestrian is observed
            stopping_time += time.time() - current_time
        else:
            velocity_publisher(forward_speed, spin_speed)  # otherwise, keep driving forward

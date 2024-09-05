def drive_forward_10_seconds():
    duration = 10 # driving time/duration (seconds)
    linear = 1 # set any desired linear velocity (m/s). Here it's set to 1 for simplicity
    angular = 0 # no angular velocity since the robot needs to drive forward
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)

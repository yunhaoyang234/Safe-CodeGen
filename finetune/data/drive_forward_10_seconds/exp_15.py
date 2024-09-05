def drive_forward_10_seconds():
    duration = 10 # driving time/duration (seconds)
    linear = 1 # here 1 is taken as an example for the linear speed
    angular = 0 # no turn means 0 angular velocity
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)

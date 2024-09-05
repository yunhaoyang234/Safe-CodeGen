def drive_forward_10_seconds():
    duration = 10 # driving time/duration (seconds)
    linear = 1 # linear speed (m/s), adjust according to your need
    angular = 0 # no turning
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)
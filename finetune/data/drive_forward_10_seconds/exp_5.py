def drive_forward_10_seconds():
    # Specify speed you want the robot to travel at (in meters per second)
    speed = 1

    duration = 10 # running time/duration (seconds)
    linear_velocity = speed # moving forward speed (m/s)
    angular_velocity = 0 # staying straight without rotating

    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear_velocity, angular_velocity)

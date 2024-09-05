def drive_forward_10_seconds():
    duration = 10  # driving duration (seconds)
    stopping_time = 0  # total time stopped for pedestrians
    linear = 2  # linear velocity (m/s), here 2 is just an example, you can replace it with any appropriate value according to your requirement
    angular = 0  # no angular velocity because the robot is moving forward straight

    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()

        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)

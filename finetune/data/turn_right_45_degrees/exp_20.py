def turn_right_45_degrees():
    duration = 5  # rotation time/duration (seconds)
    radius = 3  # rotation radius (meters)

    radian = math.pi/4  # 45 deg clockwise = pi/4
    angular = -radian / duration  # because it's clockwise, the angular velocity is negative (rad/sec)

    linear = radius * abs(angular)  # linear velocity (m/s); the absolute value of angular is taken since the velocity can't be negative

    stopping_time = 0  # total time the robot has stopped because of pedestrians
    start_time = time.time()  # timestamp (in seconds) when the rotation started

    while (time.time() - start_time) - stopping_time < duration:  # continue while the effective rotation time is less than the desired duration
        time_at = time.time()  # timestamp (in seconds) when the cycle started

        if pedestrian_observed():  # if a pedestrian is observed
            stop()  # stop the robot
            stopping_time += time.time() - time_at  # increment the total time stopped by the duration of this stop
        else:
            velocity_publisher(linear, angular)  # otherwise, publish the velocity commands for a right turn

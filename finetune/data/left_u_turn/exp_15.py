def left_u_turn():
    import time
    import math

    duration = 5  # turning time/duration in seconds
    radius = 3  # turning radius in meters
    radian = math.pi  # 180 degrees = pi radians
    stopping_time = 0  # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        angular_velocity = radian / duration  # angular velocity in rad/sec
        linear_velocity = radius * angular_velocity  # linear velocity in m/s

        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear_velocity, angular_velocity)

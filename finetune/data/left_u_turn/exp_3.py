def left_u_turn():
    radius = 3  # the radius of the turn in meters
    duration = 5  # the duration of the turn in seconds

    # 180 degrees in radians for U-turn
    radian = math.pi
    # compute linear and angular velocities
    angular = radian / duration
    linear = radius * angular

    # Stopping time for pedestrians
    stopping_time = 0
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)

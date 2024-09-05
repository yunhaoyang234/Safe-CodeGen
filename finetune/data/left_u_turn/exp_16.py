def left_u_turn():
    duration = 5 # turning time/duration (seconds)
    radius = 3 # turning radius (meters)
    radian = math.pi # 180 deg = pi
    angular = radian / duration # angular velocity (rad/s)
    linear = radius * angular # linear velocity (m/s)
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)

    stop()

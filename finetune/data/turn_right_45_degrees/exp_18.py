def turn_right_45_degree():
    duration = 5 # turning time/duration (seconds)
    radius = 3 # turning radius (meters)
    radian = math.pi/4 # 45 deg cw = pi/4 (to make a right turn we should give a negative radian)
    angular = -radian / duration # angular velocity (rad/sec) (negative as rotating to the right)
    linear = radius * abs(angular) # linear velocity (m/s)
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)
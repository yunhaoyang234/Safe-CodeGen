def turn_right_45_degrees():
    duration = 5  # Turning time/duration (seconds)
    radius = 3  # Turning radius (meters)
    radian = math.pi/4  # 45 deg cw = pi/4
    angular = -radian / duration  # Negative for right turn, angular velocity (rad/sec)
    linear = radius * abs(angular)  # Linear velocity (m/s)
    stopping_time = 0  # Total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, angular)

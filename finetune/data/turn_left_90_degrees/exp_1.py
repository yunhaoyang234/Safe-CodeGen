def turn_left_90_degrees():
    turning_period = 5 # turning time/duration (seconds)
    turning_radius = 3 # turning radius (meters)
    radian_angle = math.pi/2 # 90 deg = pi/2
    angular_velocity = radian_angle / turning_period # angular velocity (rad/sec)
    linear_velocity = turning_radius * angular_velocity # linear velocity (m/s)
    total_stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - total_stopping_time < turning_period:
        current_time = time.time()
        if pedestrian_observed():
            stop()
            total_stopping_time += time.time() - current_time
        else:
            velocity_publisher(linear_velocity, angular_velocity)

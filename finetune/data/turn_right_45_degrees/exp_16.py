def turn_right_45_degrees():
    total_time = 5 # turning time/duration (seconds)
    radius = 3 # turning radius (meters)
    radian = math.pi/4 # 45 deg cw = pi/4
    angular_velocity = -radian / total_time # angular velocity (rad/sec), negative as it's a right turn
    linear_velocity = radius * abs(angular_velocity) # linear velocity (m/s)
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()

    while (time.time() - start_time) - stopping_time < total_time:
        time_at = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear_velocity, angular_velocity)

    stop() # ensure the car stops after turn

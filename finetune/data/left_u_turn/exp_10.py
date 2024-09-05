def left_u_turn():
    duration = 5  # turning time/duration (seconds)
    radius = 3  # turning radius (meters)
    radian = math.pi  # 180 deg = pi radian
    angular = radian / duration  # angular velocity (rad/s)
    linear = radius * angular  # linear velocity (m/s)
    stopping_time = 0  # total time stopped for pedestrians

    # First half of U-turn
    start_time = time.time()
    while (time.time() - start_time) - stopping_time < duration:
        current_time = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - current_time
        else:
            velocity_publisher(linear, angular) # angular put as positive for left turn

    # Reset stopping_time for second half of U-turn
    stopping_time = 0

    # Second half of U-turn
    start_time = time.time()
    while (time.time() - start_time) - stopping_time < duration:
        current_time = time.time()
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - current_time
        else:
            velocity_publisher(linear, angular)  # angular put as positive for left turn

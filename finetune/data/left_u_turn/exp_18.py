def left_u_turn():
    # Constants
    turn_radius = 3  # meters
    turn_period = 2 * 5  # seconds - the complete U-turn contains 2 right turns of 90 degrees.
    u_turn_angle = math.pi  # radians - 180 degree turn
    angular_speed = u_turn_angle / turn_period  # rad/sec
    linear_speed = turn_radius * angular_speed  # m/sec
    
    # Initial time stamp
    start_time = time.time()
    total_stop_time = 0

    while (time.time() - start_time - total_stop_time) < turn_period:
        if pedestrian_observed():
            stop()
            total_stop_time += time.time() - start_time - total_stop_time
        else:
            velocity_publisher(linear_speed, angular_speed)
        time.sleep(0.01)  # sleep for 10 ms

def left_u_turn():
    duration = 5.0  # turning duration (seconds)
    radius = 3.0  # turning radius (meters)
    radian = math.pi / 2  # 90 deg = pi/2
    angular = radian / duration  # angular velocity (rad/sec)
    linear = radius * angular  # linear velocity (m/s)
    stopping_time = 0  # total time stopped for pedestrians
    start_time = time.time()
    completed_turns = 0  # Track number of completed 90-degree turns

    while completed_turns < 2:  # While we haven't done 2 turns (180 degrees)
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - start_time
            start_time = time.time()
        else:
            end_time = start_time + duration
            while time.time() < end_time:  # Keep moving for the specified duration
                if pedestrian_observed():
                    stop()
                    break  # Break the loop and check the pedestrian again
                else:
                    velocity_publisher(linear, angular)  # Move with the specified linear and angular speeds
            completed_turns += 1  # Increase the number of completed turns 
            start_time = time.time()  # Start the time for the next turn

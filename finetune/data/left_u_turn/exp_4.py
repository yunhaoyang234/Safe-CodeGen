def left_u_turn():
    radius = 3  # turning radius (meters)
    duration = 5  # turning duration per half of the U-turn (seconds)
    radian = math.pi  # 180 degrees equals pi radians

    linear_velocity = radius * (2 * radian) / (2 * duration)  # linear velocity (m/s)
    angular_velocity = (2 * radian) / (2 * duration) # angular velocity (rad/sec)

    stopping_time = 0  # total stopped time for pedestrians
    start_time = time.time()

    # Execute u-turn
    for _ in range(2):  # Since u-turn requires two 180-degree turns
        while(time.time() - start_time) - stopping_time  < duration:
            if pedestrian_observed():
                stop()
                time_to_stop = time.time()
                stopping_time += time_to_stop - start_time 
                start_time = time_to_stop # reset the start_time
            else:
                velocity_publisher(linear_velocity, angular_velocity)
        start_time = time.time() # reset the start_time
        stopping_time = 0 # reset the stopping_time

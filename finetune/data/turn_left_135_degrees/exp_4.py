def turn_left_135_degrees():
    duration = 5  # turning time/duration (seconds)
    radius = 3  # turning radius (meters)
    radian = 3 * math.pi / 4  # 135 degree = 3*pi/4 radian
    angular = radian / duration  # angular velocity (rad/sec)
    linear = radius * angular  # linear velocity (m/s)
    
    stopping_time = 0  # Total time stopped for pedestrians
    start_time = time.time()  # Start time of the rotation
    
    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()  
        if pedestrian_observed():  # If a pedestrian is observed
            stop()  # stop the robot
            stopping_time += time.time() - time_at  # Add the time stopped for pedestrian
        else:  # If no pedestrian is observed
            velocity_publisher(linear, angular)  # robot continues to turn left

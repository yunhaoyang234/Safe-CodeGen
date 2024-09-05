def turn_left_135_degrees():
    rotation_period = 5  # Rotation period in seconds
    radius = 3  # Turn radius in meters
    degree = 135  # Degree to turn
    radian = degree * (math.pi / 180)  # Convert degree to radian
    
    angular_velocity = radian / rotation_period  # Calculate angular velocity
    linear_velocity = radius * angular_velocity  # Calculate linear velocity

    start_time = time.time()  # Get the current time
    time_stopped = 0  # Initialize the time stopped for pedestrians

    while (time.time() - start_time) - time_stopped < rotation_period:
        if pedestrian_observed():
            stop()  # Stop the robot if a pedestrian is observed
            wait_start = time.time()  # Start the stop/wait time counter
            while pedestrian_observed():  # Keep the robot stopped while a pedestrian is observed
                time.sleep(0.1)  # Check for pedestrian every 0.1 second
            time_stopped += time.time() - wait_start  # Calculate the total stop/wait time
        else:
            velocity_publisher(linear_velocity, angular_velocity)  # Continue the turn if no pedestrian is observed
    stop()  # Stop the robot after the turn

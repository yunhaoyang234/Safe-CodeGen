def drive_forward_10_seconds():
    linear_speed = 1 # You can adjust this speed as per your project requirement (m/s)
    angular_speed = 0 # No angular speed is required to drive forward.
    stop_time = 0 # Total time stopped for pedestrians.
    start_time = time.time() # Record when the operation started.
    ten_seconds = 10

    # Keep publishing velocity until 10s has elapsed, accounting for stop time.
    while (time.time() - start_time) - stop_time < ten_seconds:
        current_time = time.time() # Record current time.
        if pedestrian_observed(): # It checks whether a pedestrian is observed.
            stop() # If a pedestrian is observed, then it stops the robot.
            stop_time += time.time() - current_time # Increment total time robot stopped for pedestrians.
        else:
            velocity_publisher(linear_speed, angular_speed) # It keeps the robot moving forward.
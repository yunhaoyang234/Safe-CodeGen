def drive_forward_10_seconds():
    linear = 1 # Forward speed of the car
    angular = 0 # The car moves straight
    stop_duration = 0 # Total time stopped for pedestrians
    start_time = time.time() # Start time of the function

    while (time.time() - start_time) - stop_duration < 10: # While the total operation time is less than 10 seconds
        time_at = time.time() # Current time
        if pedestrian_observed(): # If a pedestrian is observed
            stop() # Stop the car
            stop_duration += time.time() - time_at # Increase the total stop time
        else:
            velocity_publisher(linear, angular) # If no pedestrian, move forward

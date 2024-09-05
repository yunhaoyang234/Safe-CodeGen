def turn_left_90_degrees():
    duration = 5 # rotation period in seconds
    radius = 3 # turn radius in meters
    radian = math.pi / 2 # Angle for 90 degrees in radian
    angular_velocity = radian / duration # Angular velocity
    linear_velocity = radius * angular_velocity # Linear velocity
    
    start_time = time.time() # Function start time
    total_stop_time = 0 # Initialization of total stop time

    while (time.time() - start_time) < duration:
        start_stop_time = time.time() # Begin stop time
        if pedestrian_observed(): # If pedestrian detected - stop car
            stop()
            total_stop_time += time.time() - start_stop_time # Calculate total stop time
        else:
            velocity_publisher(linear_velocity, angular_velocity) # Publish velocity to the car

    stop() # Stop at the end of turn

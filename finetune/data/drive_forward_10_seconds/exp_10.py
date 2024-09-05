def drive_forward_10_seconds():
    duration = 10  # driving time/duration (seconds)
    linear_velocity = 1  # You can set your preferred velocity here
    angular_velocity = 0  # as the car is driving straight, angular velocity=0
    stopping_time = 0 # total time stopped for pedestrians
  
    start_time = time.time()  # get the start time

    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()  # call 'stop()' method to stop the car
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear_velocity, angular_velocity) # publish the velocity commands to drive the car

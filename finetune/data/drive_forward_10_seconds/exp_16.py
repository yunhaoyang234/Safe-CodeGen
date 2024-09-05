def drive_forward_10_seconds():
    speed = 1.0 # Forward speed is arbitrary, you can adjust as needed.
    duration = 10 # Time the car needs to drive forward.
    stopping_time = 0 # Total time car has been stopped.
    start_time = time.time() 

    while (time.time() - start_time) - stopping_time < duration:
        
        # Check if a pedestrian is observed. If yes, stop the car.
        if pedestrian_observed():
            stop()
            stopping_time += time.time() - time_at
            
        # If no pedestrian is observed, move forward.
        else:
            time_at = time.time()
            velocity_publisher(speed, 0) # 0 because there is no need for angular velocity here as car is moving straight.

    # Make sure to stop the car after the loop finishes.
    stop()

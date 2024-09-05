def left_u_turn():
    radius = 3 # turning radius in meters
    duration = 2*(5) # time to complete a left U-turn, 2x of 90 degree turn
    angular = 2*math.pi / duration # angular velocity for 360 degree turn
    linear = radius * angular # linear velocity
    stopping_time = 0 # total time stopped for pedestrians
    start_time = time.time()
    while (time.time() - start_time) - stopping_time < duration:
        time_at = time.time()
        if pedestrian_observed():
            stop()  
            stopping_time += time.time() - time_at
        else:
            velocity_publisher(linear, -angular) # negative angular value for left turn

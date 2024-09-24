def task_program():
    start_loc = get_current_location()
    go_to("lounge")
    if is_in_room("backpack"):
        while True:
            if is_in_room("person"):
                response = ask("", "Could you please put my backpack in my basket?", ["Yes", "No"])
                if response == "Yes":
                    break
            time.sleep(1)
        go_to(start_loc)
        say("Your backpack has been brought back")
    else:
        go_to(start_loc)
        say("Your backpack is not in the lounge")
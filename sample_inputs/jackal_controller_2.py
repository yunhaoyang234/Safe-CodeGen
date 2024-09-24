def task_program():
    start_loc = get_current_location()
    go_to("lounge")
    while True:
        if is_in_room("backpack") and is_in_room("person"):
            response = ask("", "Could you please put my backpack in my basket?", ["Yes", "No"])
            if response == "Yes":
                go_to(start_loc)
                say("Your backpack has been brought back")
                return
        if not is_in_room("backpack"):
            go_to(start_loc)
            say("Your backpack is not in the lounge")
            return
        time.sleep(1)
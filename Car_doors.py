def door_open(s): # s is the sequence of values
    # Storing all the instructions into the respective variables.
    left_dashboard_switch = s[0]
    right_dashboard_switch = s[1]
    child_lock = s[2]
    master_unlock = s[3]
    left_inside_handle = s[4]
    left_outside_handle = s[5]
    right_inside_handle = s[6]
    right_outside_handle = s[7]
    gear_shift = s[8]
    doors = set() # Initialzing the set to store what doors open.
    # If the gear shift is park and master unlock shift is activated 
    # only then the doors can be opened.
    if gear_shift == 'P' and master_unlock == '1':
        # If the left dashboard switch is activated, left door opens
        if left_dashboard_switch == '1':
            doors.add('left')
        # If the right dashboard switch is activated, right door opens
        if right_dashboard_switch == '1':
            doors.add('right')
        # If the left outside handle is activated, left door opens
        if left_outside_handle == '1':
            doors.add('left')
        # If the right outside handle is activated, right door opens
        if right_outside_handle == '1':
            doors.add('right')
        # If child lock is activated, we cannot open the left inside handle.
        if child_lock == '0':
            if left_inside_handle == '1':
                doors.add('left')
            if right_inside_handle == '1':
                doors.add('right')
    doors = list(doors)
    return doors

instructions = input('Enter the sequence of instructions: ')
result = door_open(instructions)
if result:
    if len(result) == 1:
        if result[0] == 'left':
            print('Left door opens')
        else:
            print('Right door opens')
    else:
        print('Both the doors open')
else:
    print('No door opens')
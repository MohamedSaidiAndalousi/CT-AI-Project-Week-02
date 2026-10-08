def stopping_distance(speed, reaction_time, braking_deceleration):
    reaction_distance = speed * reaction_time
    braking_distance = speed ** 2 / (2 * braking_deceleration)
    
    return reaction_distance + braking_distance


speed = float(input("What is the speed? "))
reaction_time = float(input("What is the reaction time? "))
braking_deceleration = float(input("What is the braking deceleration? "))

distance = stopping_distance(speed, reaction_time, braking_deceleration)

print("The stopping distance is:", distance)
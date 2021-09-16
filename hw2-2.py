## Ryan Lugo: RJL 9/16/21


#For User
##Making life easier
free_throw_times_scored = 1
inside_times_scored = 1
outside_times_scored = 1

##Hard Coded values
free_throw = 1 * free_throw_times_scored
inside_three_point = 2 * inside_times_scored
outside_three_point = 3 * outside_times_scored

#All points added together for easier printing
final_points = free_throw + outside_three_point + inside_three_point

print("The Player scored",final_points,"points in the game!")
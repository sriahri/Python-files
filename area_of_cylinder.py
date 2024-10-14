def calculateArea(height, diameter) :
    pi = 3.14
    circumferene = 2 * pi * (diameter / 2)
    area_of_top_cylinder = pi * (diameter / 2) * (diameter / 2)
    area_of_walls_of_cylinder = circumferene * height
    # Generally cylinder consists of 2 circles at top and bottom and the wall.
    # To calculate the total surface area of the cyliner,
    # We need to add the area of 2 circles and the wall.
    total_surface_area = 2 * area_of_top_cylinder + area_of_walls_of_cylinder
    print('%.2f'%total_surface_area,'square metres') # For precision handling i.e; upto 2 numbers after the point.

height = 6
diameter = 5
calculateArea(6,5)
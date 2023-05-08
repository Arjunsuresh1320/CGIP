import matplotlib.pyplot as plt
original_shape = [ ]
while True:
    point_input = input("Enter a coordinate (x, y) or 'done' to finish: ")

    if point_input.lower() == 'done':
        break

    
    try:
        x, y = map(int, point_input.split(','))
        original_shape.append((x, y))
    except ValueError:
        print("Invalid input. Please enter a coordinate in the format (x, y).")

print("Coordinates:", original_shape)
def reflect_point(point):
    return (-point[0], -point[1])

reflected_shape = [reflect_point(point) for point in original_shape]
print("reflected coordinates:",reflected_shape)

x_orig, y_orig = zip(*original_shape)
x_refl, y_refl = zip(*reflected_shape)
plt.plot(x_orig, y_orig, 'r-', label='Original')
plt.plot(x_refl, y_refl, 'b-', label='Reflected')
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.legend()
plt.show()

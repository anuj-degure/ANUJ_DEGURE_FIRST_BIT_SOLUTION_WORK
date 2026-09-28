# Write a Program to input two angles from user and find third angle of the triangle

first_angle=int(input('first angle will be:'))
second_angle=int(input('second angle will be:'))

third_angle=180 - first_angle - second_angle
print('the third angle of the triangle is:',third_angle)
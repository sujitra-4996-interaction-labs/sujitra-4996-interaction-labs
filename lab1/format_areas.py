import math
print('radius height surface_area')
for i in range(1,11):
    print(f'     {i}     {i*2:}     {2*math.pi*i*(i+(i*2)):.2f}')

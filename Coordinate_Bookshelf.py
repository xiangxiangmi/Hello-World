X = 1079.5
Y = 3837.94
#BS for bookshelf
BS_length = 360.68
BS_width = 43.18
BS_space_X = 152.4
BS_space_Y = 116.84

x_left = [106.48 + (1 + 2*i)*BS_length/8 for i in range(4)]
x_right = [106.48 + BS_space_X + (9 + 2*i)*BS_length/8 for i in range(4)]

y_front = [144.78 + (BS_width + BS_space_Y)*i for i in range(23)]
y_back = [144.78 + BS_width + (BS_width + BS_space_Y)*i for i in range(23)]

coordinate_left_front = ['{:.5f} {:.5f}\n'.format(x_cor/X,y_cor/Y) for y_cor in y_front for x_cor in x_left]
coordinate_left_back = ['{:.5f} {:.5f}\n'.format(x_cor/X,y_cor/Y) for y_cor in y_back for x_cor in x_left]
coordinate_right_front = ['{:.5f} {:.5f}\n'.format(x_cor/X,y_front[22-i]/Y) for i in range(14) for x_cor in x_right]
coordinate_right_back = ['{:.5f} {:.5f}\n'.format(x_cor/X,y_back[22-i]/Y) for i in range(14) for x_cor in x_right]

coordinate_list = []
for i in range(23):
	for j in range(4):
		coordinate_list.append(coordinate_left_front[4*i+j])
	for j in range(4):
		coordinate_list.append(coordinate_left_back[4*i+j])
for i in range(14):
	for j in range(4):
		coordinate_list.append(coordinate_right_back[4*i+j])
	for j in range(4):
		coordinate_list.append(coordinate_right_front[4*i+j])

with open('Coordinate_Bookshelf.txt','w') as f:
	f.writelines(coordinate_list)

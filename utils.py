def read_data(train_file_path):
	# print("hi")
	columns = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']
	train_list = []
	train_files = open(train_file_path, 'r')
	train_lines = train_files.readlines()

	for i in range(len(train_lines)):
		row = train_lines[i]
		values = row.split(',')
		row_dict = {}
		for j in range(len(values)):
			row_dict[columns[j]] = values[j].strip()
		train_list.append(row_dict)
		
	# print(train_dict)
	train_files.close()
	return train_list


def read_test(test_file_path):
	columns = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']
	test_list = []
	test_files = open(test_file_path, 'r')
	test_lines = test_files.readlines()
	for i in range(len(test_lines)):
		row = test_lines[i]
		values = row.split(',')
		row_dict = {}
		for j in range(len(values)):
			row_dict[columns[j]] = values[j].strip()
		test_list.append(row_dict)
	# print(test_dict)
	test_files.close()

	return test_list






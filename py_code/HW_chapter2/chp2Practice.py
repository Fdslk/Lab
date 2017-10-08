import os
import sys
import csv
import pandas as pd
import glob
import re

input_file = sys.argv[1]
#output_file = sys.argv[2]
names = ['Fang', 'Ali']
pattern = re.compile(r'(?P<group_name>a)', re.I)
classer = 'Phd'
index_columns = [1,2,3]
index_names = ['name', 'class', 'age']
file_count = 0
first_file = True

# --- csv_to_pick_up ---
#with open(input_file, 'r') as csv_in_file:
#	with open(output_file, 'w') as csv_out_file:
#		filereader = csv.reader(csv_in_file)
#		filewriter = csv.writer(csv_out_file)
#		header = next(filereader)
#		filewriter.writerow(header)
#		for row in filereader:
#			age = float(row[3])
#			if age >= 30.0:
#				filewriter.writerow(row)

# --- pandas_to_pick_up
#data_frame = pd.read_csv(input_file)
#data_frame_meet_condition = data_frame.loc[(data_frame['age']>=30),:]
#data_frame_meet_condition.to_csv(output_file)

# --- csv_to_pick_up_accroding_to_sets
#with open(input_file, 'r') as csv_in_file:
#	with open(output_file, 'w') as csv_out_file:
#		filereader = csv.reader(csv_in_file)
#		filewriter = csv.writer(csv_out_file)
#		header = next(filereader)
#		filewriter.writerow(header)
#		for row in filereader:
#			name = row[1]
#			if name in names:
#				filewriter.writerow(row)

# --- pandas_to_pick_up_according_to_set
#data_frame = pd.read_csv(input_file)
#data_frame_meet_condition = data_frame.loc[data_frame['name'].isin(names), :]
#data_frame_meet_condition.to_csv(output_file)				

# --- csv_to_pick_up_accroding_to_matches_pattern
#with open(input_file, 'r') as csv_in_file:
	# with open(output_file, 'w') as csv_out_file:
		# filereader = csv.reader(csv_in_file)
		# filewriter = csv.writer(csv_out_file)
		# header = next(filereader)
		# filewriter.writerow(header)
		# for row in filereader:
			# name = row[1].strip()
			# class_level = row[2].strip()
			# if pattern.search(name) and class_level == classer:
				# filewriter.writerow(row)

# --- csv_to_pick_up_special_columns
# with open(input_file, 'r') as csv_in_file:
	# with open(output_file, 'w') as csv_out_file:
		# filereader = csv.reader(csv_in_file)
		# filewriter = csv.writer(csv_out_file)
		# header = next(filereader)
		# header_list = [];
		# for item in range(len(header)):
			# if item in index_columns:
				# header_list.append(header[item])
		# filewriter.writerow(header_list)
		# for row in filereader:
			# row_list = []
			# for index in range(len(row)):
				# if index in index_columns:
					# row_list.append(row[index])
			# filewriter.writerow(row_list)
			
# --- pandas_to_pick_up_specical_columns
#data_frame = pd.read_csv(input_file)
#data_frame_column_by_name = data_frame.loc[:, index_names]
#data_frame_column_by_name.to_csv(output_file)

# --- csv_veiw_the_file_detail ---
# files = glob.glob(os.path.join(input_file, 'test*'))
# for file in files:
	# row_count = 1
	# with open(file, 'r') as csv_in_file:
		# filereader = csv.reader(csv_in_file)
		# header = next(filereader);
		# for row in filereader:
			# row_count += 1
	# print('{0!s}: {1:d} rows, {2:d} columns'.format(os.path.basename(file\
	# ),row_count, len(header)))
	# file_count += 1
# print "Numbers of the test file:{0:d}".format(file_count)

# --- csv_merge_from_multiple_files ---
files = glob.glob(os.path.join(input_file, 'test*'));
# for file in files:
	# with open(file, 'r') as csv_in_file:
		# with open(output_file, 'a') as csv_out_file:
			# filereader = csv.reader(csv_in_file)
			# filewriter = csv.writer(csv_out_file)
			# if first_file:
				# for row in filereader:
					# filewriter.writerow(row)
			# else:
				# header = next(filereader, None)
				# for row in filereader:
					# filewriter.writerow(row)

# --- pandas_merge_multiple_files ---
# all_data_frame = []
# for file in files:
	# data_frame = pd.read_csv(file)
	# all_data_frame.append(data_frame)
# data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
# data_frame_concat.to_csv(output_file)

# --- csv_sum_average_from_multiple_files ---
Number_of_Phd = 0
Number_of_master = 0
Phd_total_age = 0
master_total_age = 0
total_age = 0
total_number = 0
for file in files:
	with open(file, 'r') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader, None)
		for row in filereader:
			age = int(row[3])
			class_level = row[2].strip()
			if class_level == 'Phd':
				Number_of_Phd += 1
				Phd_total_age += age
			else:
				Number_of_master += 1
				master_total_age += age
			total_age += age
			total_number += 1
print("phd_numbers:{0:d}, master_numbers:{1:d}\n".format(Number_of_Phd, Number_of_master))
print("phd_average_age:{0:2f}, master_average_age:{1:2f}\n".format(\
     (float(Phd_total_age)/float(Number_of_Phd)), (float(master_total_age)/float(Number_of_master))))
print("phd_rate:{0:2f}%,master_rate:{1:2f}%\n".format((float(Number_of_Phd)/float(total_number))*100.0,\
     (float(Number_of_master)/float(total_number))*100.0))	 

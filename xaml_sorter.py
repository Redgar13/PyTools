import os, sys, glob

##########
### Prints list of files of some extension in 
### specified directory  recursively and sorted ascending
###########

def get_lines_count(fname):
	with open(fname) as f:
		return len([0 for _ in f])

walk_dir = sys.argv[1]
extension = sys.argv[2]
print('walk_dir = ' + walk_dir)

xaml_dict = {}

for filename in glob.iglob(walk_dir + '**/*.'+extension, recursive=True):
	xaml_dict[filename] = get_lines_count(filename)

xaml_dict = sorted(xaml_dict.items(), key = lambda x : x[1])

for value in xaml_dict:
	print(str(value[1])+'\t:\t'+value[0])
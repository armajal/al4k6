from collections import OrderedDict

student_list = ['tom', 'brady', 'jon', 'sam', 'claire', 'armaja']
#class_dict = dict{'tom':'SWE1', 'brady':'SnrDesign', 'jon':'1050', 'claire':'SWE1', 'armaja':'SWE1'}
username = 'goggins'
password = 'givingeveryoneana'

ta_list = ['caleb']


def student_submission_type(submission):
		acceptable_types = ['pdf', 'doc']
		if submission not in acceptable_types:
			return False
		else:
			return True

def login(user_str, passw_str):
	if(user_str == username and passw_str == password):
	   return 'Passed'
	
	else:
		return 'Failed'


def ta_search_student(student_name):
	
	if student_name in student_list:
		return 'Passed'

	else:
		return 'Failed'

def student_can_view_assignment(student_name):
	if student_name in student_list:
		return True

	else:
		return False

def ta_can_view_assignment(ta_name):
	if ta_name in ta_list:
		return True

	else:
		return False


 
import mainfile as mainfile

#################### FAILING TESTS ####################
def test_login():
	assert mainfile.login('Sara', 'bad') == 'Passed', 'Wrong Username and Password'
     

def test_ta_search_student():
	assert mainfile.ta_search_student('MOM') == 'Passed', 'Test failed. Student not Found'

def test_student_submission_type():
 	assert mainfile.student_submission_type('xls') == True, 'Test failed. Not acceptable type. '

def test_student_can_view_assignment():
	assert mainfile.student_can_view_assignment('bobbby') == True, 'Test Failed. Student not in class, Cannot View.'


def test_ta_can_view_assignment():
	assert mainfile.ta_can_view_assignment('bobbby') == True, 'Test Failed. TA not over Course.'




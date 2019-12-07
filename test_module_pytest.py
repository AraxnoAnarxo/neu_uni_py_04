from main import name_n

list_temp_01 = ['Nathan']
list_temp_02 = ['Daniel', 'Daniel']
list_temp_03 = [0]
def test_01_pytest_name_n():
    assert name_n(list_temp_01, 2) == ['Nathan', 'Nathan']

def test_02_pytest_name_n():
    assert name_n(list_temp_02, 4) == ['Daniel', 'Daniel', 'Daniel', 'Daniel']

def test_03_pytest_name_n():
    assert name_n(list_temp_03, 2) == [0, 0]
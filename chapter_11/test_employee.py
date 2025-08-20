# # 11.03 Employee
import pytest
from employee import Employee

# Without Pytest fixture
def test_give_default_raise():
    mock_employee = Employee("John","Smith", 60_000)
    mock_employee.give_raise()
    assert mock_employee.annual_salary == 65_000

def test_give_custom_raise():
    mock_employee = Employee("John","Smith", 60_000)
    mock_employee.give_raise(40_000)
    assert mock_employee.annual_salary == 100_000


# With Pytest.fixture
# @pytest.fixture
# def mock_employee():
#     first = "John"
#     last = "Smith"
#     salary = 60_000
#     new_employee = Employee(first,last,salary)
#     return new_employee


# def test_give_default_raise(mock_employee):
#     mock_employee.give_raise()
#     assert mock_employee.annual_salary == 65_000


# def test_give_custom_raise(mock_employee):
#     mock_employee.give_raise(40_000)
#     assert mock_employee.annual_salary == 100_000

'''
@Author: Javeed
@Date: 2021-09-07
@Last Modified by: Javeed
@Last Modified time: 2021-09-07 12:25:12
@Title : Test cases to Quantity_Measurment
'''

import pytest
from quantity_measurment_F_to_Y import Quantity_Measurment

feets = Quantity_Measurment()
yards = Quantity_Measurment()

def test_feets_eqls_zero():
    '''
    Description: Function to test the feets by giving zero
    Return: return Pass/Fail
    '''
    result = feets.calculate_feet(0)
    assert result == 0

def test_feets_null_check():
    '''
    Description: Function to test the feets by giving null
    Return: return Pass/Fail
    '''
    result = feets.calculate_feet(None)
    assert result == 'null'

def test_feets_value_check():
    '''
    Description: Function to test the value
    Return: return Pass/Fail
    '''
    result = feets.calculate_feet(33)
    assert result == 11

def test_feets_ref_check():
    '''
    Description: Function to test with reference
    Return: return Pass/Fail
    '''
    result = feets.calculate_feet(1)
    assert result == round(1/3,2)

def test_feets_type_check():
    '''
    Description: Function to test the type of feet
    Return: return Pass/Fail
    '''
    result = feets.type_of_input(1)
    assert result == 'int'

'''================ Inch to feet ================='''

def test_yard_equals_zero():
    '''
    Description: Function to test the yard by giving zero
    Return: return Pass/Fail
    '''
    result = yards.calculate_yard(0)
    assert result == 0

def test_yard_null_check():
    '''
    Description: Function to test the yard by giving null
    Return: return Pass/Fail
    '''
    result = yards.calculate_yard(None)
    assert result == None

def test_yard_value_check():
    '''
    Description: Function to test the value of yard
    Return: return Pass/Fail
    '''
    result = yards.calculate_yard(3)
    assert result == 9

def test_yard_ref_check():
    '''
    Description: Function to test the reference
    Return: return Pass/Fail
    '''
    result = yards.calculate_yard(1)
    assert result == 3

def test_yard_type_check():
    '''
    Description: Function to test the type of yard
    Return: return Pass/Fail
    '''
    result = yards.type_of_input(0)
    assert result == 'int'
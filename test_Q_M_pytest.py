'''
@Author: Javeed
@Date: 2021-09-06 
@Last Modified by: Javeed
@Last Modified time: 2021-09-07 7:34:25
@Title : Test cases to Quantity_Measurment
'''

import pytest
import quantity_measurment

feets = quantity_measurment.Quantity_Measurment()
inches = quantity_measurment.Quantity_Measurment()

def test_feets_eqls_zero():
    '''
    Description: Function to test the feets by giving zero
    Return: return Pass/Fail
    '''    
    result = feets.calculate_feet(0)
    assert result == 0

def test_feets_null_check():
    '''
    Description: Function to test the null
    Return: return Pass/Fail
    '''
    result = feets.calculate_feet(None)
    assert result == 'null'

def test_feets_value_check():
    '''
    Description: Function to test the value of feets 
    Return: return Pass/Fail
    '''
    result = feets.calculate_feet(3)
    assert result == 36

def test_feets_ref_check():
    '''
    Description: Function to test the reference
    Return: return Pass/Fail
    '''
    result = feets.calculate_feet(1)
    assert result == 12

def test_feets_type_check():
    '''
    Description: Function to test the feets type
    Return: return Pass/Fail
    '''
    result = feets.type_of_input(1)
    assert result == 'int'

'''================ Inch to feet ================='''

def test_inch_equals_zero():
    '''
    Description: Function to test the inches by giving zero
    Return: return Pass/Fail
    '''
    result = inches.calculate_inch(0)
    assert result == 0

def test_inch_null_check():
    '''
    Description: Function to test the null
    Return: return Pass/Fail
    '''
    result = inches.calculate_inch(None)
    assert result == None

def test_inch_value_check():
    '''
    Description: Function to test the value
    Return: return Pass/Fail
    '''
    result = inches.calculate_inch(36)
    assert result == 3

def test_inch_ref_check():
    '''
    Description: Function to test the reference
    Return: return Pass/Fail
    '''
    result = inches.calculate_inch(1)
    assert result == 0.08

def test_inch_type_check():
    '''
    Description: Function to test the type of inch
    Return: return Pass/Fail
    '''
    result = inches.type_of_input(0)
    assert result == 'int'
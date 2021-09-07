'''
@Author: Javeed
@Date: 2021-09-06 
@Last Modified by: Javeed
@Last Modified time: 2021-09-07 7:34:25
@Title : Quantity_Measurment
'''

class Quantity_Measurment():
    
    def calculate_feet(self,feet):
        '''
    Description: Function to calculate the feets to inches
    Parameter : feet as parameter to calculate inches 
    Return: return inches
    '''

        # 1 feet = 12 inches
        inch = 12
        try:
            if ( feet is None):
                return 'null'
            elif ( feet >= 0):
                inches = feet * inch
                return inches
            else:
                raise Exception
        except Exception as e:
            print(e)
        
    def type_of_input(self,feet):
            try:
                if type(feet) is int:
                    type_of = 'int'
                else:
                    type_of = 'str'
                    raise Exception(TypeError)
            except Exception as e:
                print(e)
            print(type_of)
            return type_of

    def calculate_inch(self,inch):
        '''
    Description: Function to calculate the Inches to i
    Parameter : feet as parameter to calculate inches 
    Return: return inches
    '''

        # 1 inch = 1 / 12 feet
        try:
            if (inch is None):
                return None
            elif ( inch >= 0):
                feet = inch / 12
                return round(feet,2)
            else:
                raise Exception
        except Exception as e:
            print(e)

if __name__ == '__main__':
    value = int(input('Enter a number'))
    measurement = Quantity_Measurment()
    measurement.calculate_feet(value)
    measurement.calculate_inch(value)
    measurement.type_of_feet(value)

'''
@Author: Javeed
@Date: 2021-09-07
@Last Modified by: Javeed
@Last Modified time: 2021-09-07 11:24:06
@Title : Quantity_Measurment
'''

class Quantity_Measurment():

    def calculate_feet(self,feet):
        '''
        Description: Function to calculate the feets to yards
        Parameter : feet as parameter to calculate inches 
        Return: return inches
        '''

        # 1 feet = 1/3 yard
        yard = 1/3
        try:
            if ( feet is None):
                return 'null'
            elif ( feet >= 0):
                yards = feet * yard
                return round(yards,2)
            else:
                raise Exception
        except Exception as e:
            print(e)
        
    def type_of_input(self,feet):
        '''
        Description: Function to get the type of input
        Parameter : feet as parameter to calculate type
        Return: return type
        '''
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

    def calculate_yard(self,yard):
        '''
        Description: Function to calculate the yards to feets
        Parameter : yard as parameter to calculate inches 
        Return: return feets
        '''

        # 1 yard = 3 feet
        try:
            if (yard is None):
                return None
            elif ( yard >= 0):
                feet = yard * 3
                return round(feet,2)
            else:
                raise Exception
        except Exception as e:
            print(e)

if __name__ == '__main__':
    value = int(input('Enter a number'))
    measurement = Quantity_Measurment()
    print(value,"feet = ",measurement.calculate_feet(value),"yard")
    print(value,"yard = ",measurement.calculate_yard(value),"feet")
    measurement.type_of_input(value)

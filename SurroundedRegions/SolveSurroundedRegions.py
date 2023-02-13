from Solution import SurroundedRegions
from Validation import Valid
from InvalidInputExcept import InvalidInputException
from EmptyInputExcept import EmptyInputException
class Input(BaseException):
    try:
        #initialising board 
        board = []

        numOfRows = input("Enter number of rows. ")
        
        if numOfRows == "":
            raise EmptyInputException
        elif numOfRows.isdigit() == False:
            raise InvalidInputException

        numOfRows = int(numOfRows)

        numOfCols = input("Enter number of columns. ")
        
        if numOfCols == "":
            raise EmptyInputException
        elif numOfCols.isdigit() == False:
            raise InvalidInputException

        numOfCols = int(numOfCols)

        #rowCount to track current row
        rowCount = 1

        #flag to check if given input is valid
        flag = False

        #taking input in board
        for i in range(numOfRows):
            temp = []
            flag = False
            while(flag==False):
                print(f"Enter row number {rowCount}")
                currentRow = input()
                temp = currentRow.split(" ")

                #creating an object of validation class
                validator = Valid()

                #if user enters "quit" program execution will stop
                if currentRow=="quit":
                    break

                #checking if the input is invalid
                elif(len(temp)!=numOfCols or validator.validator(currentRow)==False):
                    print("Enter valid input.")

                #if corrent input then move to next iteration
                else:
                    flag = True    
            
            if(flag==False):
                break

            print(f"Added row number {rowCount}")
            rowCount+=1
            board.append(temp)

        #checking if user opted to quit the program
        if(flag):
            print("Your input: ")
            for i in board:
                print(i)

            #creating an object of SurroundedRegions class
            sol = SurroundedRegions()

            #calling elinateSurroundedRegions funtion from SurroundedRegions class
            sol.eliminateSurroundedRegions(board)
            print("After removing surrounded O regions: ")
            for i in board:
                print(i)

    
    except EmptyInputException as e:
        print("Empty input not allowed.")
    except InvalidInputException as e:
        print("String input not allowed.")
    except Exception as e:
        print(e)

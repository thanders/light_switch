class displayboard:

# Initializes instance of the displayboard class
    def __init__(self, start_row, finish_row, start_column, finish_column):
        self.__grid = []
        self.__start_row = start_row
        self.__finish_row = finish_row
        self.__start_column = start_column
        self.__finish_column = finish_column

    def size(self):
        return print("rows:",self.__start_row, "and columns:", self.__finish_column)

    def comprehension(self):

        for i in range(self.__start_row, self.__finish_row):
            self.__grid.append([])
            for j in range(self.__start_column, self.__finish_column):
                    self.__grid[i].append([j])

    def showboard(self):
        for i in self.__grid:
            print([i])

        print()
        print(self.__grid)


# L*L matrix (L rows and L lights in each matrix)
# Initalizes the displayboard with row and column inputs
start_row=0
finish_row=2
start_column=2
finish_column=5

x = displayboard(start_row, finish_row, start_row, finish_column)

# Returns the number of rows and columns
x.size()

# Appends items to the array based on the size
x.comprehension()

#prints the array
x.showboard()
import numpy




# divmod_mod calculates the 2-array div_rest such that numerator = 
# denominator*div_rest[0]+div_rest[1] and abs(div_rest[1]) is the
# smallest possible value.

def divmod_mod(numerator, denominator): 
    '\b'
    if ((not type(numerator) is int) or (not type(denominator) is int)) and ((not type(numerator) is numpy.int64) or (not type(denominator) is numpy.int64)):
        raise TypeError('Input must be of type int or numpy.int64')
    div_rest = numpy.array(numpy.divmod(numerator, denominator))
    if div_rest[1] > denominator / 2 and denominator > 0:
        div_rest[1] -= numpy.abs(denominator)
        div_rest[0] += 1
    if div_rest[1] < denominator / 2 and denominator < 0:
        div_rest[1] += numpy.abs(denominator)
        div_rest[0] += 1
    return div_rest


# Calculate the greatest common divisor of a numpy array of integers.
def gcd(array):
    '\b'
    if not type(array) is numpy.ndarray:
        raise TypeError('Input must be of type numpy.ndarray')
    if numpy.size(array) > 2:
        return gcd(numpy.append(array[:-2],gcd(array[-2:])))
    elif array[1] == 0:
        return abs(array[0])
    else:
        return gcd(numpy.array([array[1], array[0] % array[1]]))



def solve(coefficients, right_hand_side):
    """Finds all solutions to a linear inhomogeneous diophantine equation. The output is numpy compatible.
    
    Parameters
    ----------
    coefficients : numpy.array
        Coefficients c_1,...,c_n of the diophantine equation
            c_1x_1+...c_nx_n = d
        where n is the size of coefficients. The array must be 1-D
    right_hand_side : int
        Right-hand-side d of the diophantine equation
            c_1x_1+...c_nx_n = d
        Must be an integer.
    
    Returns
    -------
    out : [numpy.ndarray,numpy.ndarray]
        Numpy arrays with shape [[n,n-1],n]. 
        The first element gives the coefficients of the n parameters and the second element gives the constant terms.
    

    Notes
    -----
    The function attempts to find the simplest possible parameter dependence. 


    Examples
    --------
    
    Example 1:
    >>> import numpy,diophantine_solver
    >>> c=numpy.array([5,7,8])
    >>> d=1
    >>> diophantine_solver.solve(c,d)
    [array([[-1,  0],
           [ 3, -8],
           [-2,  7]]), array([ 3, -2,  0])]
    
    This means that the general solution to the diophantine equation
        5x_1 + 7x_2 + 8x_3 = 1
    is given by
        |---|   |--|     |--|     |--|
        |x_1|   |-1|     | 0|     | 3|
        |x_2| = | 3|*k + |-8|*l + |-2|
        |x_3|   |-2|     | 7|     | 0|
        |---|   |--|     |--|     |--|
    where k,l are arbitrary integers.
    
    Example 2:
    >>> import numpy,diophantine_solver
    >>> c=numpy.array([5,7,8])
    >>> d=1
    >>> general_solution = diophantine_solver.solve(c,d)
    >>> parameters = numpy.random.randint(-1000, 1001,2)
    >>> solution = general_solution[0]@parameters+general_solution[1]
    >>> print(\'\'\'\nA solution to the diophantine equation\n    5x_1 + 7x_2 +8_x3 = 1\nis given by x_1=\'\'\' + str(solution[0])+\', x_2=\'+ str(solution[1])+\', x_3=\'+str(solution[2])+\'.\')
    
    A solution to the diophantine equation
        5x_1 + 7x_2 +8_x3 = 1
    is given by x_1=-12, x_2=-6101, x_3=5346."""



    if not type(coefficients) is numpy.ndarray:
        raise TypeError('coefficients must be of type numpy.ndarray')
#    if numpy.size() ..............: 
#        return numpy.array([[]])
    if not type(right_hand_side) is int:
        raise TypeError('right_hand_side must be of type int')
    



    _dim = numpy.size(coefficients)

    abs_coefficients = numpy.abs(coefficients)
    if _dim > 1:

        order = numpy.flip(numpy.argsort(abs_coefficients), axis=0)

        tot_rows = 10
        tot_columns = _dim + 11  # Ta bort denna
        sys_of_eq = numpy.zeros([tot_rows, tot_columns], int)

        row_counter = 0
        nonzero_variables = numpy.count_nonzero(coefficients)
        coefficient_order = numpy.arange(_dim)

        coeff_geq_2 = numpy.size(coefficients[numpy.abs(coefficients) > 1])
        while coeff_geq_2 > 1 or nonzero_variables > 2:

            if row_counter >= tot_rows - 3:
                tot_rows += 10
                tot_columns += 10
                sys_of_eq_new = numpy.zeros([tot_rows, tot_columns], int)
                sys_of_eq_new[0:tot_rows - 10, 0:tot_columns - 10] = sys_of_eq
                sys_of_eq = sys_of_eq_new

            div_rest = divmod_mod(coefficients[order[0]],coefficients[order[1]])
            

            sys_of_eq[row_counter, coefficient_order[order[1]]] = 1  # Bokföring
            sys_of_eq[row_counter, row_counter + _dim] = -1
            sys_of_eq[row_counter, coefficient_order[order[0]]] = div_rest[0]

            coefficients[order[0]] = div_rest[1]
            abs_coefficients = numpy.abs(coefficients)
            coefficient_order[order[1]] = _dim + row_counter


            order = numpy.flip(numpy.argsort(abs_coefficients), axis=0)
            nonzero_variables = numpy.count_nonzero(coefficients)

            coeff_geq_2 = numpy.size(coefficients[numpy.abs(coefficients) > 1])
            row_counter += 1


        final_equation = numpy.concatenate((coefficients, numpy.array([-right_hand_side])))
        final_equation = numpy.array(final_equation/gcd(final_equation),int)
        if numpy.count_nonzero(final_equation) < 3 and right_hand_side % final_equation[order[0]] != 0:
            print('No solutions!')
            return
    elif _dim == 1 and right_hand_side % coefficients[0] == 0:
        solution = numpy.array([[int(right_hand_side / coefficients[0])]])
        return solution
    else:
        print('No solutions!')
        return


   # Make all solutions represented by new variables.
    while row_counter < _dim - 1:
        sys_of_eq[row_counter, row_counter] = 1
        sys_of_eq[row_counter, row_counter + _dim] = -1
        row_counter += 1

    # Adding final equation the system of equations
    row_counter += 1

    constant_column = row_counter + _dim - 1
    sys_of_eq[row_counter - 1, constant_column] = final_equation[-1]
    sys_of_eq[row_counter - 1, coefficient_order] = final_equation[:-1]

    column = 0
    while column < row_counter:
        row = column


        while row < row_counter:
            if sys_of_eq[row, column] == 1:
                sys_of_eq[[column, row], :] = sys_of_eq[[row, column], :]
                break
            elif sys_of_eq[row, column] == -1:
                sys_of_eq[row, :] = -sys_of_eq[row, :]
                sys_of_eq[[column, row], :] = sys_of_eq[[row, column], :]
                break
            elif row == row_counter - 1:
                if row_counter >= tot_rows - 4:
                    tot_rows += 10
                    tot_columns += 10
                    sys_of_eq_new = numpy.zeros([tot_rows, tot_columns], int)
                    sys_of_eq_new[0:tot_rows - 10, 0:tot_columns - 10] = sys_of_eq
                    sys_of_eq = sys_of_eq_new

                sys_of_eq[:, [constant_column, constant_column + 1]] = sys_of_eq[:,[constant_column + 1, constant_column]]
                constant_column += 1

                sys_of_eq[[column, row_counter], :] = sys_of_eq[[row_counter, column], :]
                sys_of_eq[column, column] = 1
                sys_of_eq[column, _dim + row_counter - 1] = -1

                row_counter += 1
                break
            row += 1
        for row in numpy.delete(numpy.arange(0, row_counter), column):

            sys_of_eq[row, :] = sys_of_eq[row, :] - sys_of_eq[row, column] * sys_of_eq[column, :]

        column += 1

    tot_rows = row_counter
    sys_of_eq = sys_of_eq[0:_dim, row_counter:row_counter + _dim]
    row_order = numpy.argsort(numpy.count_nonzero(sys_of_eq[:, _dim:_dim - 1], axis=1))

    for counter in numpy.arange(0, _dim - 1):
        row = row_order[counter]
        non_zero_entries = (sys_of_eq[row, counter:_dim - 1] != 0)

        non_zero_entries_count = numpy.count_nonzero(non_zero_entries)

        while non_zero_entries_count > 1:
            column_order = numpy.argsort(numpy.abs(sys_of_eq[row, counter:_dim - 1])) + counter
            column_order = column_order[non_zero_entries[column_order - counter]]


            div_rest = divmod_mod(sys_of_eq[row, column_order[non_zero_entries_count - 1]],sys_of_eq[row, column_order[non_zero_entries_count - 2]])

            sys_of_eq[:,column_order[non_zero_entries_count -1]] = sys_of_eq[:, column_order[non_zero_entries_count -1]] - div_rest[0] * sys_of_eq[:, column_order[non_zero_entries_count - 2]]

            non_zero_entries = (sys_of_eq[row, counter:_dim - 1] != 0)
            non_zero_entries_count = numpy.count_nonzero(non_zero_entries)

        sys_of_eq[:, [counter, int(numpy.nonzero(non_zero_entries)[0]) + counter]] = sys_of_eq[:, [int(numpy.nonzero(non_zero_entries)[0]) + counter, counter]]


        if 0 < counter and counter < _dim - 1:
            for column in numpy.arange(0, counter):
                div_rest = divmod_mod(sys_of_eq[row, column], sys_of_eq[row,counter])
                sys_of_eq[:, column] = sys_of_eq[:, column] - div_rest[0] * sys_of_eq[:, counter]
    return [-sys_of_eq[:,:-1],-sys_of_eq[:,-1]] 

def decode_boarding_pass(boarding_pass):
    """
    Decode a boarding pass to determine the seat ID, row, and column.

    Args:
        boarding_pass (str): The string representing the boarding pass.
            This string should be in the format 'FBFBBFFRLR' where F and B
            represent rows, and L and R represent columns.

    Returns:
        tuple: A tuple containing the seat ID, row, and column of the seat.

    Raises:
        Raises:
            ValueError: If the row code is not 7 characters long or contains invalid characters 
            or if the column code is not 3 characters long or contains invalid characters.

    Notes:
        The boarding pass string should be 10 characters long, with the first 
        7 characters indicating the row and the last 3 characters indicating the column.

        The function performs space partitioning to determine the row and column 
        of the seat, then calculates the seat ID by multiplying the row by 8 and 
        adding the column. The tuple returned contains the seat ID as the first element,
        followed by the row and column.
    """

    row_code = boarding_pass[:7]
    column_code = boarding_pass[7:]
    
    #Decoding to get the row and column numbers
    row = decode_row(row_code)
    column = decode_column(column_code)
    
    #Calculation of the seat ID
    seat_id = row * 8 + column
    
    return seat_id, row, column

def decode_row(row_code):
    """
    Decode the row code from a boarding pass to determine the row number.

    Args:
        row_code (str): The string representing the row code.
            This string should be 7 characters long and contain only 'F' and 'B' characters.

    Returns:
        int: The row number.

    Raises:
        ValueError: If the row code is not 7 characters long or contains invalid characters.
    """
    if len(row_code) != 7:
        raise ValueError("The row code must be 7 characters long.")

    lower = 0
    upper = 127
    
    for char in row_code:
        if char == 'F':
            upper = (lower + upper) // 2
        elif char == 'B':
            lower = (lower + upper) // 2 + 1
        else:
            raise ValueError("The row code must contain only 'F' and 'B' characters.")
    
    return lower

def decode_column(column_code):
    """
    Decode the column code from a boarding pass to determine the column number.

    Args:
        column_code (str): The string representing the column code.
            This string should be 3 characters long and contain only 'L' and 'R' characters.

    Returns:
        int: The column number.

    Raises:
        ValueError: If the column code is not 3 characters long or contains invalid characters.
    """

    if len(column_code) != 3:
        raise ValueError("The column code must be 3 characters long.")
        
    lower = 0
    upper = 7
    
    for char in column_code:
        if char == 'L':
            upper = (lower + upper) // 2
        elif char == 'R':
            lower = (lower + upper) // 2 + 1
        else:
            raise ValueError("The column code must contain only 'L' and 'R' characters.")
    return lower



def main():
    """Main Script Function. Tries to find the missing seat in scan.txt"""
    # Reading scan.txt
    with open("scan.txt", "r") as scanfile:
        boarding_passes = scanfile.read().splitlines()

    # Decoding boarding passes and obtaining occupied seats IDs, then sorting it.
    occupied_seats = [decode_boarding_pass(boarding_pass)[0] for boarding_pass in boarding_passes]
    occupied_seats.sort()

    # Looking for the missing seats between two IDs
    for i in range(len(occupied_seats) - 1):
        if occupied_seats[i] + 1 != occupied_seats[i + 1]:
            missing_seat_id = occupied_seats[i] + 1
            print("missing_seat_id :", missing_seat_id)
            break

    print("Your place's ID is :", missing_seat_id)

if __name__ == "__main__":
    main()
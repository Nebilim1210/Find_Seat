import math

"""

"""

#Define number of rows in the plane
rows_number = 128

#Define number of columns in the plane
cols_number = 8    

def decode_boarding_pass(boarding_pass):
    row_code = boarding_pass[:7]
    column_code = boarding_pass[7:]
    
    # Décode la rangée
    row = decode_row(row_code)
    
    # Décode la colonne
    column = decode_column(column_code)
    
    # Calcule l'ID du siège
    seat_id = row * 8 + column
    
    return row, column, seat_id

def decode_row(row_code):
    lower = 0
    upper = 127
    
    for char in row_code:
        if char == 'F':
            upper = (lower + upper) // 2
        elif char == 'B':
            lower = (lower + upper) // 2 + 1
    
    return lower

def decode_column(column_code):
    lower = 0
    upper = 7
    
    for char in column_code:
        if char == 'L':
            upper = (lower + upper) // 2
        elif char == 'R':
            lower = (lower + upper) // 2 + 1
    
    return lower

# Test des exemples donnés
boarding_passes = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
for boarding_pass in boarding_passes:
    row, column, seat_id = decode_boarding_pass(boarding_pass)
    print(f"Boarding Pass: {boarding_pass}, Row: {row}, Column: {column}, Seat ID: {seat_id}")


# Lire le contenu du fichier scan.txt
with open("scan.txt", "r") as file:
    boarding_passes = file.read().splitlines()

# Décoder les cartes d'embarquement et obtenir les ID des sièges occupés
occupied_seats = [decode_boarding_pass(boarding_pass)[2] for boarding_pass in boarding_passes]

print(occupied_seats[0])

# Trier la liste des ID des sièges occupés
occupied_seats.sort()

print(occupied_seats)

# Recherche de la place manquante entre deux ID consécutifs
for i in range(len(occupied_seats) - 1):
    if occupied_seats[i] + 1 != occupied_seats[i + 1]:
        missing_seat_id = occupied_seats[i] + 1
        print("missing_seat_id :", missing_seat_id)

print("Votre ID de place est :", missing_seat_id)
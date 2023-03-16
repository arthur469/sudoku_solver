import random
import copy


def solve_sudoku(grid):
    # Trouver la prochaine case vide
    row, col = find_empty_cell(grid)

    # Si toutes les cases sont remplies, le Sudoku est résolu
    if row is None:
        return True

    # Essayer les chiffres de 1 à 9 dans la case vide
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            # Si le chiffre est valide, l'ajouter à la grille
            grid[row][col] = num

            # Résoudre le Sudoku avec le chiffre ajouté
            if solve_sudoku(grid):
                return True

            # Si la solution n'a pas pu être trouvée avec ce chiffre, réinitialiser la case et essayer un autre chiffre
            grid[row][col] = 0

    # Si aucun chiffre ne fonctionne, le Sudoku ne peut pas être résolu
    return False


def get_solved_sudoku(puzzle):
    solution = solve_sudoku(puzzle)
    if solution is True:
        print("Solution found:")
        print_sudoku(puzzle)
        return puzzle
    else:
        print("No solution exists for this puzzle.")
        return None


def is_valid_move(grid, row, col, num):
    # Vérifier si le chiffre est dans la ligne
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Vérifier si le chiffre est dans la colonne
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Vérifier si le chiffre est dans la région
    region_row = (row // 3) * 3
    region_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[region_row + i][region_col + j] == num:
                return False

    # Si le chiffre est valide, retourner True
    return True


def generate_sudoku():
    # Créer une grille vide
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Remplir la grille en utilisant une combinaison de backtracking et de contrainte propagation
    fill_grid(grid)

    return grid


def fill_grid(grid):
    # Trouver la prochaine case vide
    row, col = find_empty_cell(grid)

    # Si toutes les cases sont remplies, la grille est valide
    if row is None:
        return True

    # Essayer de remplir la case vide avec un chiffre valide
    valid_numbers = get_valid_numbers(grid, row, col)
    random.shuffle(valid_numbers)
    for num in valid_numbers:
        grid[row][col] = num
        if fill_grid(grid):
            return True
        grid[row][col] = 0

    # Aucun chiffre valide n'a fonctionné, revenir en arrière
    return False


def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None


def get_valid_numbers(grid, row, col):
    # Créer un ensemble des chiffres invalides dans la même ligne, colonne et région
    invalid_numbers = set(grid[row][j] for j in range(9))
    invalid_numbers |= set(grid[i][col] for i in range(9))
    region_row = (row // 3) * 3
    region_col = (col // 3) * 3
    for i in range(region_row, region_row+3):
        for j in range(region_col, region_col+3):
            invalid_numbers.add(grid[i][j])

    # Créer un ensemble des chiffres valides
    valid_numbers = set(range(1, 10)) - invalid_numbers

    return list(valid_numbers)


def generate_puzzle(difficulty='hard'):
    # Générer une grille complète
    grid = generate_sudoku()

    # Créer une liste des cases à supprimer en fonction de la difficulté choisie
    if difficulty == 'easy':
        cells_to_remove = [random.randint(0, 80) for _ in range(40)]
    elif difficulty == 'medium':
        cells_to_remove = [random.randint(0, 80) for _ in range(50)]
    elif difficulty == 'hard':
        cells_to_remove = [random.randint(0, 80) for _ in range(60)]
    else:
        raise ValueError('difficulty must be "easy", "medium", or "hard"')

    # Copier la grille pour ne pas modifier la grille complète
    puzzle = copy.deepcopy(grid)

    # Supprimer les cases sélectionnées de la grille
    for cell in cells_to_remove:
        row = cell // 9
        col = cell % 9
        puzzle[row][col] = 0

    return puzzle


def print_sudoku(grid):
    print('+-------+-------+-------+')
    for i in range(9):
        row = ''
        for j in range(9):
            if j % 3 == 0:
                row += '| '
            if isinstance(grid[i][j], bool) or grid[i][j] == 0:
                row += '  '
            else:
                row += str(grid[i][j]) + ' '
        row += '|'
        print(row)
        if i == 2 or i == 5:
            print('|-------+-------+-------|')
    print('+-------+-------+-------+')


if __name__ == "__main__":
    sudoku = generate_puzzle()
    print_sudoku(sudoku)
    get_solved_sudoku(sudoku)
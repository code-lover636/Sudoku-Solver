from tkinter import *

# Setting up window
root = Tk()
root.title('sudoku solver')
root.resizable(0, 0)

# Grid corresponding sudoku tiles
grid = [[],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []]


# # Creating sudoku tiles
for i in range(9):
    for j in range(9):
        if (i in (0, 1, 2, 6, 7, 8) and j in range(3, 6)) or (j in (0, 1, 2, 6, 7, 8) and i in range(3, 6)):
            e = Entry(root, width=1, font=('ink free', 18, 'bold'), bg='sky blue', fg='blue', justify='center', cursor='center_ptr'
                      , insertbackground='blue', borderwidth=1)
            e.grid(row=i, column=j, ipadx=12, ipady=5)
        else:
            e = Entry(root, width=1, font=('ink free', 18, 'bold'), fg='green', justify='center', cursor='center_ptr',
                      insertbackground='blue', borderwidth=1)
            e.grid(row=i, column=j, ipadx=12, ipady=5)
        grid[i].append(e)

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j].get() == "":
                return i, j


def valid(grid, num, pos):
    for i in range(9):
        try:
            grid1 = int(grid[pos[0]][i].get())
        except ValueError:
            grid1 = ''
        if grid1 == num and pos[1] != i:
            return False

    for i in range(9):
        try:
            grid1 = int(grid[i][pos[1]].get())
        except ValueError:
            grid1 = ''
        if grid1 == num and pos[0] != i:
            return False

    grid_x = pos[1] // 3
    grid_y = pos[0] // 3
    for i in range(grid_y * 3, grid_y * 3 + 3):
        for j in range(grid_x * 3, grid_x * 3 + 3):
            try:
                grid1 = int(grid[i][j].get())
            except ValueError:
                grid1  = ''
            if grid1 == num and (i, j) != pos:
                return False
    return True


def solve(grid):
    do(2)
    find = find_empty(grid)
    if not find:
        return True
    else:
        (row, column) = find
    for i in range(1, 10):
        if valid(grid, i, (row, column)):
            grid[row][column].delete(0, END)
            grid[row][column].insert(0, i)
            if solve(grid):
                return True
            grid[row][column].delete(0, END)
            grid[row][column].insert(0,'')

    return False


def do(num):
    global grid
    for i in range(9):
        for j in range(9):
            # clear
            if num == 1:
                grid[i][j].delete(0, END)
            # make valid
            elif num == 2:
                try:
                    digit = grid[i][j].get()
                    digit = int(digit[0])
                    grid[i][j].delete(0, END)
                    if digit > 0:
                        grid[i][j].insert(0, digit)
                except Exception:
                    grid[i][j].delete(0, END)
                    grid[i][j].insert(0, '')


# # Creating drop down menu
menu_bar = Menu(root)
root.config(menu=menu_bar)
down_arrow = Menu(menu_bar)
down_arrow.add_command(label="solve", command=lambda: solve(grid))
down_arrow.add_separator()
down_arrow.add_command(label="new game", command=lambda: do(1))
down_arrow.add_separator()
down_arrow.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="▼", menu=down_arrow)

root.mainloop()


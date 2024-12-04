INPUT_FILE = 'input.txt'


def count_xmas_occurrences(grid: list[list], word: str="XMAS"):
    """
    Gets grid as input and uses helper functions to check for occurrences of the word.
    :param grid: list[list]
    :param word: the word to search for, default 'XMAS'
    :return: occurrences of word as integer.
    """
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (1, 1),  # Down-right (diagonal)
        (1, 0),  # Down
        (1, -1),  # Down-left (diagonal)
        (0, -1),  # Left
        (-1, -1),  # Up-left (diagonal)
        (-1, 0),  # Up
        (-1, 1),  # Up-right (diagonal)
    ]

    def is_valid(x: int, y: int) -> bool:
        """
        Check if a cell is within the grid bounds.
        :param x: current x coordinate
        :param y: current y coordinate
        :return: Boolean
        """
        return 0 <= x < rows and 0 <= y < cols

    def matches_word(x: int, y: int, dx: int, dy: int) -> bool:
        """
        Check if there is an occurrence of word.
        :param x: current x coordinate
        :param y: current y coordinate
        :param dx: x coordinate direction
        :param dy: y coordinate direction
        :return: Boolean
        """
        for i in range(word_len):
            nx = x + i * dx
            ny = y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if matches_word(r, c, dx, dy):
                    count += 1
    return count


def count_xmas_patterns(grid: list[list]) -> int:
    """
    Gets grid as input and uses helper functions to check for a valid pattern.
    :param grid: list[list].
    :return: valid patterns count as integer.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid(x: int, y: int) -> bool:
        """
        Check if a cell is within the grid bounds.
        :param x: current x coordinate
        :param y: current y coordinate
        :return: Boolean
        """
        return 0 <= x < rows and 0 <= y < cols

    def matches_mas(center_x: int, center_y: int) -> bool:
        """
        Check if the cell at (center_x, center_y) is the center of an X-MAS.
        :param center_x: x coordinate
        :param center_y: y coordinate
        :return: Boolean
        """
        # Define the positions for the diagonals
        top_left = (center_x - 1, center_y - 1)
        bottom_left = (center_x + 1, center_y - 1)
        top_right = (center_x - 1, center_y + 1)
        bottom_right = (center_x + 1, center_y + 1)

        mas_configurations = [
            ("M", "A", "S"),
            ("S", "A", "M"),
        ]

        center_grid = grid[center_x][center_y]

        top_left_grid = grid[top_left[0]][top_left[1]]
        bottom_right_grid = grid[bottom_right[0]][bottom_right[1]]

        top_right_grid = grid[top_right[0]][top_right[1]]
        bottom_left_grid = grid[bottom_left[0]][bottom_left[1]]

        for mas in mas_configurations:
            if (
                is_valid(*top_left) and top_left_grid == mas[0] and
                is_valid(*bottom_right) and bottom_right_grid == mas[2] and
                is_valid(center_x, center_y) and center_grid == mas[1]
            ):
                if (
                    is_valid(*top_right) and top_right_grid == mas[0] and
                    is_valid(*bottom_left) and bottom_left_grid == mas[2]
                ):
                    return True
                elif (
                    is_valid(*top_right) and top_right_grid == mas[2] and
                    is_valid(*bottom_left) and bottom_left_grid == mas[0]
                ):
                    return True
        return False

    # Iterate through every cell in the grid
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            #print(grid[1][2])
            if grid[r][c] == "A" and matches_mas(r, c):
                count += 1
    return count


def get_grid(filepath: str) -> list[list]:
    """
    Read the file and convert to a grid.
    :param filepath: file location as string.
    :return: file as a grid (list[list])
    """
    with open(filepath, 'r') as handle:
        grid = handle.readlines()

    grid = [list(row.strip()) for row in grid]
    return grid


def main():
    grid = get_grid(INPUT_FILE)

    result = count_xmas_occurrences(grid)
    print(f"Total 'XMAS' occurrences: {result}")

    result2 = count_xmas_patterns(grid)
    print(f"Total 'X-MAS' occurrences: {result2}")


if __name__ == '__main__':
    main()
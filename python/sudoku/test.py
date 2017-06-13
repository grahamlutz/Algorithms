import sudoku

def test():
    "A set of unit tests."
    assert len(sudoku.squares) == 81
    assert len(sudoku.unit_list) == 27
    assert all(len(sudoku.units[s]) == 3 for s in sudoku.squares)
    assert all(len(sudoku.peers[s]) == 20 for s in sudoku.squares)
    assert sudoku.units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert sudoku.peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    grid1 = '003020600900305001001806400008132900700000008006708200002609500800203009005010300'

    sudoku.display(sudoku.parse_grid(grid1))
    print 'All tests pass.'

test()
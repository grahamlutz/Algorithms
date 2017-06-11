import pprint

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

rows     = 'ABCDEFGHI'
cols     = '123456789'
squares  = cross(rows, cols)
row_list = [cross(rows, c) for c in cols]
col_list = [cross(r, cols) for r in rows]
box_list = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unit_list = row_list + col_list + box_list
# units is a dictionary where each square maps to the list of units that contain the square
units = dict((s, [u for u in unit_list if s in u]) for s in squares)
# peers is a dictionary where each square s maps to the set of squares formed by the union of the squares in the units of s, but not s itself
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

pp = pprint.PrettyPrinter(indent=4)

# print 'unit_list'
# print '\n'
# pp.pprint(unit_list)
# print '\n'
# print 'squares'
# print '\n'
# pp.pprint(squares)
# print '\n'
# print 'units'
# print '\n'
# pp.pprint(units)
# print '\n'
# print 'peers'
# print '\n'
# pp.pprint(peers)
# print '\n'

def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unit_list) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print 'All tests pass.'

test()
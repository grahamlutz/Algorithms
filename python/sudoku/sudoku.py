import pprint

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
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

print 'unit_list'
print '\n'
pp.pprint(unit_list)
print '\n'
print 'squares'
print '\n'
pp.pprint(squares)
print '\n'
print 'units'
print '\n'
pp.pprint(units)
print '\n'
print 'peers'
print '\n'
pp.pprint(peers)
print '\n'

from koala import Spreadsheet

sp = Spreadsheet("example.xlsx")
v = sp.cell_evaluate('Sheet 1!A1')

print("A1", v)

sp.cell_set_value('Sheet 1!B5', 15)

v = sp.cell_evaluate('Sheet 1!A1')

print("A1", v)

address = 'Sheet 1!B6'
if address not in sp.cellmap and address not in sp.named_ranges:
    set_value = sp.cell_add
else:
    set_value = sp.cell_set_value

set_value(address, value=15)

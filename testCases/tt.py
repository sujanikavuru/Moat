

from utilities import XlUtils

path = "../TestData/search.xlsx"

rows = XlUtils.getRowCount(path, 'Search1')
print("No of rows", rows)
for row in range(2, rows + 1):
    search_1 = XlUtils.readData(path, 'Search1', row, 1)
    print(search_1)

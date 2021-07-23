import xlrd


def read(path):
    wb = xlrd.open_workbook(path)
    print("number of sheet:",wb.nsheets)
    print("name:",wb.sheet_names())
    return wb


def readByIndex(path,index):
    wb = read(path)
    return wb.sheet_by_index(index)


def readAllSheet(path):
    wb = read(path)
    res = []
    for i in range(wb.nsheets):
        res.append(wb.sheet_by_index(i))
    return res

def readSheetAllContentByRow(sh):
    print("sheet info",sh.name,sh.nrows,sh.ncols)
    res = []
    for i in range(sh.nrows):
        res.append(sh.row_values(i))
    return res

def readSheetAllContentByCol(sh):
    print("sheet info",sh.name,sh.nrows,sh.ncols)
    res = []
    for i in range(sh.ncols):
        res.append(sh.col_values(i))
    return res

def readSheetAllContentByCell(sh):
    print("sheet info",sh.name,sh.nrows,sh.ncols)
    res = []
    for i in range(sh.nrows):
        temp = []
        for j in range(sh.ncols):
            temp.append(sh.cell_value(i,j))
        res.append(temp)
    return res


from __future__ import division
from xlrd import open_workbook,XL_CELL_TEXT

book = open_workbook('roomate_data.xls')
sheet = book.sheet_by_index(1)
people=[]
people_one=[]
score=0
dumb= ['trsf', 'asdfad', 'asdas', 'asd']
name_place=5
columns = (sheet.ncols)
rows = (sheet.nrows)

def cell_contents(sheet, row_x):
    result = []
    for col_x in range(1,sheet.ncols):
        cell = sheet.cell(row_x,col_x)
        result.append(cell.value)
def single_cell(sheet, row_x, col_x):
    cell = sheet.cell(row_x, col_x)
        
    return cell
print ' '
print "Comparisons"
print ' '
if rows >= 4:
    for row_x in range(0,sheet.nrows):
        score_list=[]
        name_list=[]
        name_person = str(sheet.cell(row_x,name_place))
        name_person= name_person[7:len(name_person)-1]
        person_row=row_x
        people.append(name_person)
        name = []
        for a in range(2,columns):
            name.append(sheet.cell(row_x, a))
        for row_xy in range(0,sheet.nrows):
            name_person_one = str(sheet.cell(row_xy,name_place))
            name_person_one= name_person_one[7:len(name_person_one)-1]
            if str(name_person) != str(name_person_one):
                name_one = []
                for b in range(1,5):
                    name_one.append(sheet.cell(row_xy,b))
                for c in range(0,14):
                    
                    if str(name[c]) == str(name_one[c]):
                        score +=1
                    
                score = (score/4)*100
                score = str(score)
                
                
                score_list.append(float(score))
                name_list.append(name_person_one)
                score=0
        comparison = zip(score_list,name_list)
        sorted_comparison = sorted(comparison)
        sorted_comparison = sorted_comparison[::-1]
        new_score_list = [point[0] for point in sorted_comparison]
        new_name_list = [point[1] for point in sorted_comparison]
        print "%s is most compatible with: %s;%s%%, %s;%s%%, %s;%s%%," % (name_person, new_name_list[0], new_score_list[0], new_name_list[1], new_score_list[1], new_name_list[2], new_score_list[2], )
        
        print ' '
else:
    print "Not enough data."

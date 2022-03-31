import openpyxl
import visualisation


def create_table(dict_numb: dict):
    book = openpyxl.Workbook()
    book.remove(book.active)

    ws = book.create_sheet('data')

    for key, value in dict_numb.items():
        temp = (key, value)
        ws.append(temp)

    visualisation.create_chart(ws)
    book.save('test.xlsx')
    
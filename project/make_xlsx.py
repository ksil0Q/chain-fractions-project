import openpyxl
import visualisation


def create_table(list_of_numbers: list):
    book = openpyxl.Workbook()
    book.remove(book.active)
    ws = book.create_sheet('data')
    for i, row in enumerate(list_of_numbers):
        temp = (i, row)
        ws.append(temp)

    visualisation.create_chart(ws, list_of_numbers)
    book.save('test.xlsx')
    
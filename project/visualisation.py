from openpyxl.chart import LineChart, BarChart


def create_chart(ws, list_of_numbers: list):
    chart = LineChart()
    _str = 'data!B1:B' + str(len(list_of_numbers))
    chart.add_data(_str)
    ws.add_chart(chart)


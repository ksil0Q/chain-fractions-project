from openpyxl.chart import LineChart, Reference


def create_chart(ws):
    chart = LineChart()

    keys = Reference(worksheet=ws, min_col=1, min_row=1, max_row=100)
    values = Reference(worksheet=ws, min_col=2, min_row=1, max_row=100)

    chart.width, chart.height = 45, 15

    chart.add_data(values)
    chart.set_categories(keys)

    ws.add_chart(chart, 'D2')

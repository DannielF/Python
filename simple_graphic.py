from bokeh.plotting import figure, output_file, show


if __name__ == "__main__":
    output_file('simple_graphic.html')
    fig = figure()

    total_values = int(input('How many values do you want to graphic? '))
    x_values = list(range(total_values))
    y_values = []

    for x in x_values:
        val = int(input(f'value y for {x} '))
        y_values.append(val)

    fig.line(x_values, y_values, line_width=2)
    show(fig)    
    
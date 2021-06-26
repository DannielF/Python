from bokeh.plotting import figure, output_file, show
#plotting == graficado

if __name__ == "__main__":
    output_file('simple_graphic.html') #en donde se genera el grafico
    fig = figure()
    # type(fig)
    # help(figure)

    total_values = int(input('How many values do you want to plot? '))
    x_values = list(range(total_values))
    y_values = [] #los valores de asignados a y se ponen aca

    for x in x_values:
        val = int(input(f'value y for {x} '))
        y_values.append(val)#append == adiccionar esos valores

    fig.line(x_values, y_values, line_width=2)
    show(fig)    
    

import matplotlib.pyplot as plt
def create_chart(data, x_column, y_column, chart_type):
    fig, ax = plt.subplots()

    if chart_type == "Bar":
        data.plot(x=x_column, 
                  y=y_column, 
                  kind="bar",
                    ax=ax)
    elif chart_type == "Line":
        data.plot(x=x_column, 
                  y=y_column, 
                  kind="line",
                    ax=ax)
    elif chart_type == "Scatter":
        data.plot(x=x_column,
                   y=y_column, 
                   kind="scatter",
                     ax=ax)

    ax.set_title(f"{x_column} vs {y_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)

    fig.tight_layout()
    return fig

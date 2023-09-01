import plotly.graph_objects as go


def collatz(number):
    number_list = [number]
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
            number_list.append(number)
        elif number % 2 != 0:
            number = int((number * 3) + 1)
            number_list.append(int(number))
    return number_list


def main():
    while True:
        try:
            plots_number = int(input("Ingrese la cantidad de numeros que quiere graficar con la Conjetura de Collatz: "))
            fig = go.Figure()
            for i in range(0, plots_number):
                while True:
                    try:
                        number_to_collatz = int(input(f"Ingrese el {i + 1}° numero a graficar: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                data = collatz(number_to_collatz)
                iterations = list(range(1, len(data) + 1))
                fig.add_trace(go.Scatter(
                    x=iterations,
                    y=data,
                    text=data,
                    textposition='top center',
                    mode='lines+markers+text',
                    marker=dict(size=6),
                    line=dict(width=3),
                    line_shape='linear',
                    name=f'Collatz {number_to_collatz}'
                ))
            fig.update_layout(
                title='Collatz Conjecture',
                xaxis_title='Iteration',
                yaxis_title='Number',
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#7f7f7f"
                )
            )
            fig.show()
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == '__main__':
    main()

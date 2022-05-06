import panel as pn
import asyncio
import warnings

warnings.filterwarnings("ignore")

pn.extension()


def fibonacchi(x):
    if x <= 2:
        return 1
    if x > 2:
        return fibonacchi(x - 1) + fibonacchi(x - 2)


def b(event):
    text.value = "Clicked {0} times".format(button.clicks)


text = pn.widgets.TextInput(name="Text Input", placeholder="Enter a string here...")
button = pn.widgets.Button(name="Click me", button_type="primary")
button.on_click(b)

row = pn.Row(button, text)
# print(row)
await pn.io.pyodide.show(row, "mytextbox")
# print("Hello Samar")

# for num in range(1, 3):
# print(f" {num} ==> {fibonacchi(num)}")

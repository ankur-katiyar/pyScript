import asyncio
import panel as pn

slider = pn.widgets.FloatSlider(start=0, end=10, name="Amplitude")


def callback(new):
    return f"Amplitude is: {new}"


row = pn.Row(slider, pn.bind(callback, slider))

await pn.io.pyodide.show(row, "myplot")

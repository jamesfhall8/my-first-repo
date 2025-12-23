import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, 1)
    return


@app.cell
def _():
    b = 2
    return (b,)


@app.cell
def _():
    a = 10
    return (a,)


@app.cell
def _(a, b):
    a + b
    return


if __name__ == "__main__":
    app.run()

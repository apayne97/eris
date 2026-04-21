import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Is life random or deterministic?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We don't know for sure. But at the quantum mechanics level it's certainly possible that there is inherent quantum randomness. However, a strange discovery in the last 100 years is that even deterministic systems exhibit *chaos*, or an appearance of randomness.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Quantifying Uncertainty in Deterministic Systems
    """)
    return


@app.cell
def _():
    import eris as e
    from importlib import reload
    import numpy as np
    reload(e)
    return (np,)


@app.cell
def _(mo):
    mo.md("""
    \[s(t) = s_0 + v_0 t + 0.5 g t^2\]
    """)
    return


@app.function
def flight_trajectory_1d(t, s_0, v_0, g=-9.81):
    return s_0 + v_0 * t + 0.5 * g * (t**2)


@app.cell
def _(np):
    g = np.matrix([0, -9.81]).T
    def flight_trajectory_2d(t, s_0, v_0, g=g):
        return s_0 + v_0 * t + 0.5 * g * np.square(t)

    return (flight_trajectory_2d,)


@app.cell
def _(np):
    times = np.matrix(np.linspace(0,6,40))
    return (times,)


@app.cell
def _():
    # angle = 45 / 360 * (2 * np.pi)
    # speed = 42 # m/s
    # y_s_0 = 4
    # y_v_0 = np.sin(angle)*speed
    # x_s_0 = 0
    # x_v_0 = np.cos(angle)*speed
    return


@app.cell
def _():
    # s_0 = np.matrix([x_s_0, y_s_0]).T
    # v_0 = np.matrix([x_v_0, y_v_0]).T
    return


@app.cell
def _():
    # xy = flight_trajectory_2d(times, s_0, v_0)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell
def _():
    # np.ravel(xy[0])
    return


@app.cell
def _(flight_trajectory_2d, np, times):
    data = []
    for _angle in [0, 15, 30, 45, 90]:
        angle = _angle / 360 * (2 * np.pi)
        speed = 42 # m/s
        y_s_0 = 4
        y_v_0 = np.sin(angle)*speed
        x_s_0 = 0
        x_v_0 = np.cos(angle)*speed
        s_0 = np.matrix([x_s_0, y_s_0]).T
        v_0 = np.matrix([x_v_0, y_v_0]).T
        data.append(flight_trajectory_2d(times, s_0, v_0))
    return (data,)


@app.cell
def _(data, np, plt):
    plt.scatter(np.ravel(data[0][0]), np.ravel(data[0][1]))
    return


@app.cell
def _(data, np, plt):
    plt.scatter(np.ravel(data[1][0]), np.ravel(data[1][1]))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

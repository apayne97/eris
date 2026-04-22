import marimo

__generated_with = "0.23.1"
app = marimo.App(width="columns")


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
    import sympy as sm
    from sympy import symbols, sqrt, cos, sin, pi, Eq, pretty_print, print_latex, Function, Matrix, lambdify, MatrixSymbol
    from sympy.vector import CoordSys3D
    import matplotlib.pyplot as plt
    from sympy.physics.units import meter, second, kilo, convert_to, radian, degrees
    sm.init_printing(use_latex=True, )
    reload(e)
    from sympy.stats import Normal, density, cdf
    import seaborn as sns

    return (
        Eq,
        Function,
        Matrix,
        convert_to,
        cos,
        degrees,
        lambdify,
        meter,
        np,
        plt,
        radian,
        second,
        sin,
        sm,
        sns,
        sqrt,
        symbols,
    )


@app.cell
def _(convert_to, degrees, radian):
    45*convert_to(degrees, radian)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We'll start with a relatively simple system - the 2D trajectory of a thrown ball.
    Our initial conditions are:
    """)
    return


@app.cell
def _():
    # C = CoordSys3D('C')
    # speed_sm, angle_sm, grav_accel= sm.symbols('r theta g')
    return


@app.cell
def _():
    # # Formulas for components
    # x_comp = speed_sm * cos(angle_sm)
    # y_comp = speed_sm * sin(angle_sm)

    # # Example: Magnitude of 10 at 45 degrees (pi/4 radians)
    # magnitude_val = 42 # m/s - the speed of a fast baseball pitch
    # angle_val_deg = 45
    # angle_val_rad = angle_val_deg/360 * (2 *pi)

    # # Initial Velocity
    # x_v_0 = float(x_comp.subs({speed_sm: magnitude_val, angle_sm: angle_val_rad}))
    # y_v_0 = float(y_comp.subs({speed_sm: magnitude_val, angle_sm: angle_val_rad}))

    # v_0 = Matrix([[x_comp, y_comp],[meter/second, meter/second]])

    # # Initial Position
    # x_s_0 = 's_x_0'
    # y_s_0 = 's_y_0'
    # s_0 = Matrix([[x_s_0, y_s_0], [meter, meter]])

    # # initial time
    # t_sym = symbols('t')
    # t = Matrix([[t_sym,0], [0, second]])
    return


@app.cell
def _():
    # t.subs({'t':0})
    return


@app.cell
def _():
    # v_0.subs({angle_sm: angle_val_deg, speed_sm: magnitude_val})
    return


@app.cell
def _():
    # s_0.subs({x_s_0: 0, y_s_0:2})
    return


@app.cell
def _():
    # s_0
    return


@app.cell
def _():
    # t *v_0
    return


@app.cell
def _():
    # s_t = s_0 + t * v_0
    # s_t
    return


@app.cell
def _():
    # times = np.matrix(np.linspace(0,6,40))
    return


@app.cell
def _():
    # func = lambdify('t', s_t.subs({angle_sm: angle_val_deg, speed_sm: magnitude_val, x_s_0: 0, y_s_0: 2}), 'numpy')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The unit version of this is a bit too complex for me not to pull my hair out. i'm going to keep them separate
    """)
    return


@app.cell
def _(Matrix, convert_to, cos, degrees, radian, sin, sm, symbols):
    # Initial variables
    speed_sm, theta, grav_accel= sm.symbols('r theta g')

    # Convert to rad
    # angle_val_rad = theta/360 * (2 *pi)
    # Formulas for components
    x_comp = speed_sm * cos(theta * convert_to(degrees, radian) / radian)
    y_comp = speed_sm * sin(theta * convert_to(degrees, radian) / radian)

    # Initial Velocity
    # x_v_0 = float(x_comp.subs({speed_sm: magnitude_val, angle_sm: angle_val_rad}))
    # y_v_0 = float(y_comp.subs({speed_sm: magnitude_val, angle_sm: angle_val_rad}))

    v_0 = Matrix([[x_comp, y_comp]])

    # Initial Position
    x_s_0 = symbols('s_x_0')
    y_s_0 = symbols('s_y_0')
    s_0 = Matrix([[x_s_0, y_s_0]])

    # initial time
    # t_sym = symbols('t')
    # t = Matrix([[t_sym,0], [0, second]])
    t = symbols('t')
    return s_0, speed_sm, t, theta, v_0, x_s_0, y_s_0


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the absence of gravity, the position and velocity of the ball at time (t) can be given by:
    """)
    return


@app.cell
def _(s_0, t, v_0):
    s_t = s_0 + v_0 * t
    return (s_t,)


@app.cell
def _(s_t):
    s_t.free_symbols
    return


@app.cell
def _(s_t):
    s_t
    return


@app.cell
def _(degrees, meter, s_t, second, speed_sm, t, theta, x_s_0, y_s_0):
    # simpler unit analysis - we can just subsitute in the values. 
    s_t.subs({theta: degrees, speed_sm:meter/second, y_s_0: meter, x_s_0: meter, t:second})
    return


@app.cell
def _(s_t, speed_sm, theta, x_s_0, y_s_0):
    s_t.subs({theta:45, speed_sm:42, y_s_0: 2, x_s_0: 0})
    return


@app.cell
def _(lambdify, s_t, speed_sm, t, theta, x_s_0, y_s_0):
    s_t_func = lambdify(t, s_t.subs({theta:45, speed_sm:42, y_s_0: 2, x_s_0: 0}), 'numpy')
    return (s_t_func,)


@app.cell
def _(np, s_t_func):
    times = np.linspace(0,6,40)
    x,y = s_t_func(times)[0,0], s_t_func(times)[0,1]
    return times, x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can plot the time-dependent arc by coloring by time
    """)
    return


@app.cell
def _(np, plt, sns):
    def plot_results(x, y, times, x_err=None, y_err=None):
        import matplotlib as mpl

        sns.set_theme(style="whitegrid")
        fig, ax = plt.subplots()

        norm = mpl.colors.Normalize(vmin=float(np.min(times)), vmax=float(np.max(times)))

        if x_err is not None or y_err is not None:
            ax.errorbar(
                x,
                y,
                xerr=x_err,
                yerr=y_err,
                fmt="none",
                ecolor="0.65",
                elinewidth=1,
                capsize=3,
                alpha=0.8,
                zorder=1,
            )

        sns.scatterplot(
            x=x,
            y=y,
            hue=times,
            palette="viridis",
            hue_norm=norm,
            legend=False,
            s=70,
            ax=ax,
            zorder=2,
        )

        ax.set_xlabel("Horizontal Distance (m)")
        ax.set_ylabel("Height (m)")

        scalar_map = mpl.cm.ScalarMappable(norm=norm, cmap="viridis")
        scalar_map.set_array([])
        fig.colorbar(scalar_map, ax=ax, label="Time (s)")
        plt.show()
        return fig, ax

    return (plot_results,)


@app.cell
def _(plot_results, times, x, y):
    plot_results(x, y, times)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## when we change the initial conditions slightly, we get a predictable, deterministic output.
    We can vizualize this by plotting the final y position as a function of the initial y position
    """)
    return


@app.cell
def _(s_t, speed_sm, t, theta, times, x_s_0):
    s_t.subs({theta:45, speed_sm:42, t: times[-1], x_s_0: 0})
    return


@app.cell
def _(lambdify, np, s_t, speed_sm, t, theta, times, x_s_0, y_s_0):
    y_initial = np.linspace(0,40, 10)
    y_init_test_func = lambdify(y_s_0, s_t.subs({theta:45, speed_sm:42, t: times[-1], x_s_0: 0}), 'numpy')
    y_final = [y_init_test_func(i)[0,1] for i in y_initial]
    return y_final, y_init_test_func, y_initial


@app.cell
def _(plt, times, y_final, y_initial):
    def plot_2d_states(x,y):
        import seaborn as sns

        fig, ax = plt.subplots()

        sns.scatterplot(
            x=x,
            y=y,
            ax=ax,
        )

        ax.set_xlabel("Initial height (m)")
        ax.set_ylabel(f"Height after {times[-1]} seconds (m)")

        plt.show()
    plot_2d_states(y_initial, y_final)
    return (plot_2d_states,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And as we analyze the results more closely, they continue to be predictable
    """)
    return


@app.cell
def _(
    lambdify,
    np,
    plot_2d_states,
    s_t,
    speed_sm,
    t,
    theta,
    times,
    x_s_0,
    y_init_test_func,
    y_s_0,
):
    _y_initial = np.linspace(0,40, 100)
    _y_init_test_func = lambdify(y_s_0, s_t.subs({theta:45, speed_sm:42, t: times[-1], x_s_0: 0}), 'numpy')
    _y_final = [y_init_test_func(i)[0,1] for i in _y_initial]
    plot_2d_states(_y_initial, _y_final)
    return


@app.cell
def _(mo):
    mo.md("""
    \[s(t) = s_0 + v_0 t + 0.5 g t^2\]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # It gets slightly more fun if we add the effect due to gravity
    """)
    return


@app.cell
def _(Matrix, s_0, symbols, t, v_0):
    g = Matrix([[0, symbols('g')]])
    # s_t = s_0 + v_0 * t
    s_t_g = s_0 + v_0 * t + 0.5 * g * t**2
    return (s_t_g,)


@app.cell
def _(s_t_g):
    s_t_g
    return


@app.cell
def _(s_t_g):
    with_g = s_t_g.subs({'g': -9.81})
    return (with_g,)


@app.cell
def _(with_g):
    with_g
    return


@app.cell
def _(speed_sm, theta, with_g, x_s_0, y_s_0):
    with_g.subs({theta:45, speed_sm:42, y_s_0: 2, x_s_0: 0})
    return


@app.cell
def _(lambdify, plot_results, speed_sm, t, theta, times, with_g, x_s_0, y_s_0):
    _func = lambdify(t, with_g.subs({theta:45, speed_sm:42, y_s_0: 2, x_s_0: 0}), 'numpy')
    _x,_y = _func(times)[0,0], _func(times)[0,1]
    plot_results(_x,_y,times)
    return


@app.cell
def _(
    lambdify,
    np,
    plot_2d_states,
    speed_sm,
    t,
    theta,
    times,
    with_g,
    x_s_0,
    y_s_0,
):
    _y_initial = np.linspace(0,40, 100)
    _y_init_test_func = lambdify(y_s_0, with_g.subs({theta:45, speed_sm:42, t: times[-1], x_s_0: 0}), 'numpy')
    _y_final = [_y_init_test_func(i)[0,1] for i in _y_initial]
    plot_2d_states(_y_initial, _y_final)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How can we prove this analytically?
    """)
    return


@app.cell
def _(with_g):
    with_g.diff('s_x_0')
    return


@app.cell
def _(with_g):
    with_g.diff('s_y_0')
    return


@app.cell
def _(s_t):
    s_t.diff('s_y_0')
    return


@app.cell
def _(s_t):
    s_t.diff('s_x_0')
    return


@app.cell
def _(s_t, speed_sm):
    s_t.diff(speed_sm)
    return


@app.cell
def _(speed_sm, with_g):
    with_g.diff(speed_sm)
    return


@app.cell
def _(theta, with_g):
    with_g.diff(theta)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The final state depends linearly on the initial conditions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # We can evaluate this by using error propagation
    The general formulat for error propagation for multiple independent variables is
    """)
    return


@app.cell
def _(Function, sqrt, symbols):
    _x,_y,_z = symbols('x y z')
    ux, uy, uz, uf = symbols('sigma_x sigma_y sigma_z sigma_f')
    f = Function('f')(_x, _y, _z)
    vf = sqrt((f.diff(_x)*ux)**2 + (f.diff(_y)*uy)**2 + (f.diff(_z)*uz)**2)
    f
    return uf, vf


@app.cell
def _(Eq, uf, vf):
    Eq(uf, vf)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can automate this somewhat
    """)
    return


@app.cell
def _():
    u_s = 1 # meter
    u_r = 2 # meter / second
    u_theta = 5 # degrees
    return u_r, u_s, u_theta


@app.cell
def _(with_g):
    with_g.free_symbols
    return


@app.cell
def _(theta, with_g):
    with_g.diff(theta)
    return


@app.function
def get_partial_uncertainty(expr, var, u_var):
    return (expr.diff(var)*u_var).applyfunc(lambda x: x**2)


@app.cell
def _():
    return


@app.cell
def _(speed_sm, sqrt, theta, u_r, u_s, u_theta, with_g, x_s_0, y_s_0):
    u_s_t = (get_partial_uncertainty(with_g, theta, u_theta) + get_partial_uncertainty(with_g, speed_sm, u_r)+get_partial_uncertainty(with_g, x_s_0, u_s)+ get_partial_uncertainty(with_g, y_s_0, u_s)).applyfunc(lambda x: sqrt(x))
    return (u_s_t,)


@app.cell
def _(u_s_t):
    u_s_t
    return


@app.cell
def _(mo):
    initial_speed = mo.ui.slider(5, 80, value=42, step=1, label="Initial speed (m/s)")
    launch_angle = mo.ui.slider(5, 85, value=45, step=1, label="Launch angle (deg)")
    initial_x = mo.ui.slider(-10, 10, value=0, step=0.5, label="Initial x (m)")
    initial_y = mo.ui.slider(0, 20, value=2, step=0.5, label="Initial y (m)")
    position_uncertainty = mo.ui.slider(0, 5, value=1, step=0.25, label="Position uncertainty (m)")
    speed_uncertainty = mo.ui.slider(0, 10, value=2, step=0.25, label="Speed uncertainty (m/s)")
    angle_uncertainty = mo.ui.slider(0, 15, value=5, step=0.5, label="Angle uncertainty (deg)")

    mo.vstack(
        [
            mo.md("""
            ### Interactive uncertainty analysis
            Adjust the launch conditions and uncertainty values to see how the final trajectory and propagated uncertainty change.
            """),
            initial_speed,
            launch_angle,
            initial_x,
            initial_y,
            position_uncertainty,
            speed_uncertainty,
            angle_uncertainty,
        ]
    )
    return (
        angle_uncertainty,
        initial_speed,
        initial_x,
        initial_y,
        launch_angle,
        position_uncertainty,
        speed_uncertainty,
    )


@app.cell
def _(
    angle_uncertainty,
    initial_speed,
    initial_x,
    initial_y,
    lambdify,
    launch_angle,
    plot_results,
    position_uncertainty,
    speed_sm,
    speed_uncertainty,
    sqrt,
    t,
    theta,
    times,
    with_g,
    x_s_0,
    y_s_0,
):
    _subs_dict = {
        theta: launch_angle.value,
        speed_sm: initial_speed.value,
        y_s_0: initial_y.value,
        x_s_0: initial_x.value,
    }
    _func = lambdify(t, with_g.subs(_subs_dict), 'numpy')
    _x,_y = _func(times)[0,0], _func(times)[0,1]

    _interactive_u_s_t = (
        get_partial_uncertainty(with_g, theta, angle_uncertainty.value)
        + get_partial_uncertainty(with_g, speed_sm, speed_uncertainty.value)
        + get_partial_uncertainty(with_g, x_s_0, position_uncertainty.value)
        + get_partial_uncertainty(with_g, y_s_0, position_uncertainty.value)
    ).applyfunc(lambda value: sqrt(value))

    _err_func = lambdify(t, _interactive_u_s_t.subs(_subs_dict), 'numpy')
    _x_err, _y_err = _err_func(times)[0,0], _err_func(times)[0,1]
    plot_results(_x, _y, times, x_err=_x_err, y_err=_y_err)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Predictable outcomes are possible because we can easily calculate partial differential equations for each variable.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

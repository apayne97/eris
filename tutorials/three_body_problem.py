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
    # The 3 Body Problem
    ----------------------------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. Introduction
    The 3-body problem is a classical problem in celestial mechanics that describes the motion of three massive bodies interacting with each other under the influence of gravity. This problem has significant applications in understanding the orbits of planets, moons, and artificial satellites.

    The goal is to predict the future **positions and velocities** of the three bodies given their initial states.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Assumptions and Simplifications
    * **Isolated System**: The system consists only of the two interacting bodies, with no external forces acting on them.
    * **Point Masses**: The bodies are treated as point masses, having all their mass concentrated at a single point.
    * **Newtonian Gravity**: The force between the two bodies is described by Newton's law of universal gravitation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Mathematical formulation
    A planet is presented as a particle that has a position $\vec{p}$. $F_{p_i \ / \ p_j}$ is the gravitational force that $p_i$ is exerting on $p_j$

    $$ \vec{F}_{p_i \ / \ p_j} = G \frac{m_i \ m_j}{|\vec{p}_i - \vec{p}_j|^3} \left(\vec{p}_i - \vec{p}_j \right) $$

    Here $\vec{p} = [p_x, p_y, p_z]$ contains the coordinates of the planet.

    By using Newton's second law of motion on each planet:

    * On planet 1 ($\vec{p}_1$):
    $$ m_1 \frac{d^2 \vec{p}_1}{dt^2} = G \left(\frac{m_3 \ m_1}{|\vec{p}_3 - \vec{p}_1|^3} \left(\vec{p}_3 - \vec{p}_1 \right)  +   \frac{m_2 \ m_1}{|\vec{p}_2 - \vec{p}_1|^3} \left(\vec{p} _2 - \vec{p}_1 \right) \right)$$

    resulting in:

    $$\boxed{ \frac{d^2 \vec{p}_1}{dt^2} = G m_3 \frac{\vec{p}_3 - \vec{p}_1}{|\vec{p}_3 - \vec{p}_1|^3} +  G m_2 \frac{\vec{p}_2 - \vec{p}_1}{|\vec{p}_2 - \vec{p}_1|^3} } $$

    The work is repeated for the remaining planets ($\vec{p}_2$ and $\vec{p}_3$), finally obtaining the system of odinary differential equations ODE's:

    $$
    \boxed{
    \begin{array}{c}
    \displaystyle \frac{d^2 \vec{p}_1}{dt^2} = G m_3 \frac{\vec{p}_3 - \vec{p}_1}{|\vec{p}_3 - \vec{p}_1|^3} +  G m_2 \frac{\vec{p}_2 - \vec{p}_1}{|\vec{p}_2 - \vec{p}_1|^3} \\[0.2cm]
    \displaystyle \frac{d^2 \vec{p}_2}{dt^2} = G m_3 \frac{\vec{p}_3 - \vec{p}_2}{|\vec{p}_3 - \vec{p}_2|^3} +  G m_1 \frac{\vec{p}_1 - \vec{p}_2}{|\vec{p}_2 - \vec{p}_2|^3}\\[0.2cm]
    \displaystyle \frac{d^2 \vec{p}_3}{dt^2} = G m_1 \frac{\vec{p}_1 - \vec{p}_3}{|\vec{p}_1 - \vec{p}_3|^3} +  G m_2 \frac{\vec{p}_2 - \vec{p}_3}{|\vec{p}_2 - \vec{p}_3|^3}
    \end{array}
    }
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. Packaging our problem for Python
    #### Dimensionless version
    We might need to rescale our problem to simplify and allowing more stability. This by defining new variables:

    - $\vec{p'} = \vec{p}/L$
    - $m' = m/M$
    - $t' = t \sqrt{GM/L^3}$

    Were $\vec{p'}$, $m'$ and $t'$ are dimensionless variables, and $L$ and $M$ are reference values.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By replacing the rescaled variables we obtain the following equation:

    $$
    \displaystyle \frac{d^2 (L \vec{p'}_1)}{d(\frac{t'}{\sqrt{GM/L^3}})^2} = G m_3 \frac{L(\vec{p'}_3 - \vec{p'}_1)}{|L(\vec{p'}_3 - \vec{p'}_1)|^3} +  G m_2 \frac{L(\vec{p'}_2 - \vec{p'}_1)}{|L(\vec{p'}_2 - \vec{p'}_1)|^3}
    $$

    Leading to:

    $$\displaystyle \frac{L \ GM}{L^3}\frac{d^2 \vec{p'}_1}{dt'^2} = G m_3 \frac{L}{L^3} \frac{\vec{p'}_3 - \vec{p'}_1}{|\vec{p'}_3 - \vec{p'}_1|^3} +  G m_2 \frac{L}{L^3} \frac{\vec{p'}_2 - \vec{p'}_1}{|\vec{p'}_2 - \vec{p'}_1|^3}$$

    After simplifying:

    $$
    \boxed{
    \displaystyle \frac{d^2 \vec{p'}_1}{dt'^2} = \frac{m_3}{M} \frac{\vec{p'}_3 - \vec{p'}_1}{|\vec{p'}_3 - \vec{p'}_1|^3} + \frac{m_2}{M}  \frac{\vec{p'}_2 - \vec{p'}_1}{|\vec{p'}_2 - \vec{p'}_1|^3}
    }
    $$

    Finally we obtain the rescaled system of ODE:

    $$
    \boxed{
    \begin{array}{c}
    \displaystyle \frac{d^2 \vec{p'}_1}{dt'^2} = m_3' \frac{\vec{p'}_3 - \vec{p'}_1}{|\vec{p'}_3 - \vec{p'}_1|^3} + m_2'  \frac{\vec{p'}_2 - \vec{p'}_1}{|\vec{p'}_2 - \vec{p'}_1|^3} \\[0.2cm]
    \displaystyle \frac{d^2 \vec{p'}_2}{dt'^2} = m_3' \frac{\vec{p'}_3 - \vec{p'}_2}{|\vec{p'}_3 - \vec{p'}_2|^3} + m_1'  \frac{\vec{p'}_1 - \vec{p'}_2}{|\vec{p'}_1 - \vec{p'}_2|^3}\\[0.2cm]
    \displaystyle \frac{d^2 \vec{p'}_3}{dt'^2} = m_1' \frac{\vec{p'}_1 - \vec{p'}_3}{|\vec{p'}_1 - \vec{p'}_3|^3} + m_2'  \frac{\vec{p'}_2 - \vec{p'}_3}{|\vec{p'}_2 - \vec{p'}_3|^3}
    \end{array}
    }
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Transforming into a system of first ODE's

    By defining new functions $\vec{f}_1$, $\vec{f}_2$ and $\vec{f}_3$ defined by:

    $$ \vec{f}_1 = \frac{d \vec{p'}_1}{dt} $$
    $$ \vec{f}_2 = \frac{d \vec{p'}_2}{dt} $$
    $$ \vec{f}_3 = \frac{d \vec{p'}_3}{dt} $$

    The system of first order ODE is obtained:
    $$
    \boxed{
    \begin{array}{l}
    \vec{f}_1 & = & \displaystyle \frac{d \vec{p'}_1}{dt}\\
    \vec{f}_2 & = & \displaystyle \frac{d \vec{p'}_2}{dt}\\
    \vec{f}_3 & = & \displaystyle \frac{d \vec{p'}_3}{dt}\\
    \displaystyle \frac{d \vec{f}_1}{dt} & = & \displaystyle m_3' \frac{\vec{p'}_3 - \vec{p'}_1}{|\vec{p'}_3 - \vec{p'}_1|^3} +  m_2' \frac{\vec{p'}_2 - \vec{p'}_1}{|\vec{p'}_2 - \vec{p'}_1|^3} \\[0.2cm]
    \displaystyle \frac{d \vec{f}_2}{dt} & = & \displaystyle m_3' \frac{\vec{p'}_3 - \vec{p'}_2}{|\vec{p'}_3 - \vec{p'}_2|^3} +  m_1' \frac{\vec{p'}_1 - \vec{p'}_2}{|\vec{p'}_2 - \vec{p'}_2|^3}\\[0.2cm]
    \displaystyle \frac{d \vec{f}_3}{dt} & = & \displaystyle m_1' \frac{\vec{p'}_1 - \vec{p'}_3}{|\vec{p'}_1 - \vec{p'}_3|^3} +  m_2' \frac{\vec{p'}_2 - \vec{p'}_3}{|\vec{p'}_2 - \vec{p'}_3|^3}
    \end{array}
    }
    $$

    We are looking to solve for $\vec{p'}_1$, $\vec{p'}_2$ and $\vec{p'}_3$. Where at $t' = 0$, we have informations about the initial position and velocities of the planets (Initial Conditions | IVP):

    * $\displaystyle \vec{p'}_{i_{t'=0}} = \vec{p'}_{i_{0}} = \left[p'_{_i{x_0}}, p'_{_i{y_0}}, p'_{_i{z_0}} \right]$
    * $\displaystyle \vec{v'}_{i_{t'=0}} = \vec{v'}_{i_{0}} = \left[v'_{_i{x_0}}, v'_{_i{y_0}}, v'_{_i{z_0}} \right]$
    * $\vec{p'}_i$ position vector, $\vec{v'}_i$ velocity vector for $i=1, 2, 3$ (3 here representing the number of planets interacting with each other.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python Implementation
    -----------------------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 1. Importing the Libraries
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import solve_ivp

    return np, plt, solve_ivp


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2. Interactive Controls
    Use the sliders and inputs below to configure the simulation. The plot will update automatically.
    """)
    return


@app.cell
def _(mo):
    # --- Masses ---
    mass_header = mo.md("**Masses**")
    m1_slider = mo.ui.slider(0.1, 5.0, value=1.0, step=0.1, label="m₁")
    m2_slider = mo.ui.slider(0.1, 5.0, value=1.0, step=0.1, label="m₂")
    m3_slider = mo.ui.slider(0.1, 5.0, value=1.0, step=0.1, label="m₃")

    # --- Time span ---
    time_header = mo.md("**Simulation time**")
    time_end_slider = mo.ui.slider(1, 50, value=10, step=1, label="t end")

    # --- Initial Positions ---
    pos_header = mo.md("**Initial Positions**")
    p1x = mo.ui.number(value=1.0, step=0.1, label="p1x")
    p1y = mo.ui.number(value=0.0, step=0.1, label="p1y")
    p1z = mo.ui.number(value=1.0, step=0.1, label="p1z")
    p2x = mo.ui.number(value=1.0, step=0.1, label="p2x")
    p2y = mo.ui.number(value=1.0, step=0.1, label="p2y")
    p2z = mo.ui.number(value=0.0, step=0.1, label="p2z")
    p3x = mo.ui.number(value=0.0, step=0.1, label="p3x")
    p3y = mo.ui.number(value=1.0, step=0.1, label="p3y")
    p3z = mo.ui.number(value=1.0, step=0.1, label="p3z")

    # --- Initial Velocities ---
    vel_header = mo.md("**Initial Velocities**")
    v1x = mo.ui.number(value=0.0, step=0.1, label="v1x")
    v1y = mo.ui.number(value=0.0, step=0.1, label="v1y")
    v1z = mo.ui.number(value=-1.0, step=0.1, label="v1z")
    v2x = mo.ui.number(value=0.0, step=0.1, label="v2x")
    v2y = mo.ui.number(value=0.0, step=0.1, label="v2y")
    v2z = mo.ui.number(value=1.0, step=0.1, label="v2z")
    v3x = mo.ui.number(value=0.0, step=0.1, label="v3x")
    v3y = mo.ui.number(value=0.0, step=0.1, label="v3y")
    v3z = mo.ui.number(value=-0.6, step=0.1, label="v3z")

    mo.vstack([
        mo.hstack([mass_header, m1_slider, m2_slider, m3_slider], justify="start"),
        mo.hstack([time_header, time_end_slider], justify="start"),
        mo.hstack([pos_header,
                   mo.vstack([p1x, p1y, p1z]),
                   mo.vstack([p2x, p2y, p2z]),
                   mo.vstack([p3x, p3y, p3z])], justify="start"),
        mo.hstack([vel_header,
                   mo.vstack([v1x, v1y, v1z]),
                   mo.vstack([v2x, v2y, v2z]),
                   mo.vstack([v3x, v3y, v3z])], justify="start"),
    ])
    return (
        m1_slider,
        m2_slider,
        m3_slider,
        p1x,
        p1y,
        p1z,
        p2x,
        p2y,
        p2z,
        p3x,
        p3y,
        p3z,
        time_end_slider,
        v1x,
        v1y,
        v1z,
        v2x,
        v2y,
        v2z,
        v3x,
        v3y,
        v3z,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 3. Defining our system of first order ODE's in Python:
    """)
    return


@app.cell
def _(np):
    def system_odes(t, S, m1, m2, m3):
        p1, p2, p3 = S[0:3], S[3:6], S[6:9]
        dp1_dt, dp2_dt, dp3_dt = S[9:12], S[12:15], S[15:18]

        f1, f2, f3 = dp1_dt, dp2_dt, dp3_dt

        df1_dt = m3*(p3 - p1)/np.linalg.norm(p3 - p1)**3 + m2*(p2 - p1)/np.linalg.norm(p2 - p1)**3
        df2_dt = m3*(p3 - p2)/np.linalg.norm(p3 - p2)**3 + m1*(p1 - p2)/np.linalg.norm(p1 - p2)**3
        df3_dt = m1*(p1 - p3)/np.linalg.norm(p1 - p3)**3 + m2*(p2 - p3)/np.linalg.norm(p2 - p3)**3

        return np.array([f1, f2, f3, df1_dt, df2_dt, df3_dt]).ravel()

    return (system_odes,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 4. Solving our problem numerically
    """)
    return


@app.cell
def _(
    m1_slider,
    m2_slider,
    m3_slider,
    np,
    p1x,
    p1y,
    p1z,
    p2x,
    p2y,
    p2z,
    p3x,
    p3y,
    p3z,
    solve_ivp,
    system_odes,
    time_end_slider,
    v1x,
    v1y,
    v1z,
    v2x,
    v2y,
    v2z,
    v3x,
    v3y,
    v3z,
):
    m1 = m1_slider.value
    m2 = m2_slider.value
    m3 = m3_slider.value
    time_e = time_end_slider.value

    initial_conditions = np.array([
        [p1x.value, p1y.value, p1z.value],
        [p2x.value, p2y.value, p2z.value],
        [p3x.value, p3y.value, p3z.value],
        [v1x.value, v1y.value, v1z.value],
        [v2x.value, v2y.value, v2z.value],
        [v3x.value, v3y.value, v3z.value],
    ]).ravel()

    t_points = np.linspace(0, time_e, 1001)

    solution = solve_ivp(
        fun=system_odes,
        t_span=(0, time_e),
        y0=initial_conditions,
        t_eval=t_points,
        args=(m1, m2, m3),
        method='RK45',
        rtol=1e-8,
        atol=1e-8,
    )

    p1x_sol = solution.y[0]
    p1y_sol = solution.y[1]
    p1z_sol = solution.y[2]
    p2x_sol = solution.y[3]
    p2y_sol = solution.y[4]
    p2z_sol = solution.y[5]
    p3x_sol = solution.y[6]
    p3y_sol = solution.y[7]
    p3z_sol = solution.y[8]
    return (
        p1x_sol,
        p1y_sol,
        p1z_sol,
        p2x_sol,
        p2y_sol,
        p2z_sol,
        p3x_sol,
        p3y_sol,
        p3z_sol,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 5. Plotting the results
    """)
    return


@app.cell
def _(
    p1x_sol,
    p1y_sol,
    p1z_sol,
    p2x_sol,
    p2y_sol,
    p2z_sol,
    p3x_sol,
    p3y_sol,
    p3z_sol,
    plt,
):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.plot(p1x_sol, p1y_sol, p1z_sol, 'green', label='Planet 1', linewidth=1)
    ax.plot(p2x_sol, p2y_sol, p2z_sol, 'red',   label='Planet 2', linewidth=1)
    ax.plot(p3x_sol, p3y_sol, p3z_sol, 'blue',  label='Planet 3', linewidth=1)

    ax.plot([p1x_sol[-1]], [p1y_sol[-1]], [p1z_sol[-1]], 'o', color='green', markersize=7)
    ax.plot([p2x_sol[-1]], [p2y_sol[-1]], [p2z_sol[-1]], 'o', color='red',   markersize=7)
    ax.plot([p3x_sol[-1]], [p3y_sol[-1]], [p3z_sol[-1]], 'o', color='blue',  markersize=7)

    ax.set_title("The 3-Body Problem")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.grid()
    plt.legend()
    plt.gca()
    return


if __name__ == "__main__":
    app.run()

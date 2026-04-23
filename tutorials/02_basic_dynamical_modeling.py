import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from sympy import symbols, Matrix, Function, Symbol, pprint
    from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame, Point, Particle, KanesMethod, init_vprinting
    init_vprinting()
    return (
        KanesMethod,
        Matrix,
        Particle,
        Point,
        ReferenceFrame,
        dynamicsymbols,
        mo,
        symbols,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Higher Order ODE Systems modeled with Linear Algebra
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## System of N Coupled 1st order ODEs
    each ODE has only 1st order dependency on time
    """)
    return


@app.cell
def _():
    # y, x= dynamicsymbols('y x')
    # t = symbols('t')
    return


@app.cell
def _():
    # x.diff()
    return


@app.cell
def _():
    # # Enable dot notation printing
    # init_vprinting()

    # # Define a time-dependent variable x(t)
    # x = dynamicsymbols('x')
    # t = Symbol('t')

    # # First derivative: prints as ẋ
    # mo.output.append(x.diff(t))

    # # Second derivative: prints as ẍ
    # mo.output.append(x.diff(t, 2))

    return


@app.cell
def _(
    KanesMethod,
    Matrix,
    Particle,
    Point,
    ReferenceFrame,
    dynamicsymbols,
    mo,
    symbols,
):
    q1 = dynamicsymbols('q1')                     # Angle of pendulum
    u1 = dynamicsymbols('u1')                     # Angular velocity
    q1d = dynamicsymbols('q1', 1)
    L, m, t, g = symbols('L, m, t, g')
    mo.output.append([q1, u1, q1d])

    # Compose world frame
    N = ReferenceFrame('N')
    pN = Point('N*')
    pN.set_vel(N, 0)

    # A.x is along the pendulum
    A = N.orientnew('A', 'axis', [q1, N.z])
    A.set_ang_vel(N, u1*N.z)

    # Locate point P relative to the origin N*
    P = pN.locatenew('P', L*A.x)
    vel_P = P.v2pt_theory(pN, N, A)
    pP = Particle('pP', P, m)

    # Create Kinematic Differential Equations
    kde = Matrix([q1d - u1])

    # Input the force resultant at P
    R = m*g*N.x

    # Solve for eom with kanes method
    KM = KanesMethod(N, q_ind=[q1], u_ind=[u1], kd_eqs=kde)
    fr, frstar = KM.kanes_equations([pP], [(P, R)])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

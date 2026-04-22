import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sm
    from sympy import symbols, Matrix, Eq, evaluate

    return Eq, Matrix, evaluate, sm, symbols


@app.cell
def _(sm):
    sm.init_printing(use_latex=True)
    return


@app.cell
def _(symbols):
    x, y = symbols('x y')
    return x, y


@app.cell
def _(x, y):
    expr = x + 2*y
    return (expr,)


@app.cell
def _(expr):
    expr
    return


@app.cell
def _():
    return


@app.cell
def _(sm):
    sm.beta
    return


@app.cell
def _(Matrix, symbols):
    from sympy.physics.control import StateSpace, TransferFunction
    m, k, b = symbols('m k b')
    A = Matrix([[0, 1], [-k/m, -b/m]])
    B = Matrix([[0], [1/m]])
    C = Matrix([[1, 0]])
    D = Matrix([[0]])
    ss = StateSpace(A, B, C, D)
    tf = ss.rewrite(TransferFunction)[0][0]
    tf
    return


@app.cell
def _(symbols):
    p_a, p_b, beta, E_A, E_B = symbols("p_A p_B beta E_A E_B")
    return E_A, E_B, beta, p_a, p_b


@app.cell
def _(E_A, E_B, Eq, beta, evaluate, p_a, p_b, sm):
    with evaluate(False):
        boltzmann = Eq(p_b / p_a, sm.exp(-(beta * E_B)) / sm.exp(- (beta * E_A)))
    boltzmann
    return


@app.cell
def _(E_A, E_B, Eq, beta, p_a, p_b, sm):
    _boltzmann = Eq(p_b / p_a, sm.exp(-(beta * E_B)) / sm.exp(- (beta * E_A)))
    _boltzmann
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

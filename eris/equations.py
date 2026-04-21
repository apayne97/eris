from pydantic import BaseModel
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

def make_minimal_equation(latex_code, output_name='equation.png'):
    # Create figure with no axes or whitespace
    fig = plt.figure(figsize=(1, 0.5))  # Small initial figure size
    fig.text(0.5, 0.5, f'${latex_code}$',
             ha='center', va='center', fontsize=20)
    fig.show()
    # # Save with tight bounding box to minimize padding
    # plt.savefig(output_name, dpi=300, transparent=True,
    #             bbox_inches='tight', pad_inches=0.1)
    # plt.close(fig

class Equation(BaseModel):
    equation: str
    def __str__(self):
        return self.equation

    def display(self):
        make_minimal_equation(self.equation)

    def solve(self):
        pass

class FlightTrajectory(Equation):
    equation: str = "s(t) = s_0 + v_0 t + 0.5 g t^2"
    def solve(self):
        pass
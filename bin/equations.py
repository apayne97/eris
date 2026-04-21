from pydantic import BaseModel

class Equation(BaseModel):
    equation: str
    def __str__(self):
        return self.equation

    def solve(self):
        pass

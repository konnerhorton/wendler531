from wendler531.units import Quantity
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

"""from https://en.wikipedia.org/wiki/One-repetition_maximum"""

def adams(weight: float, reps: int) -> float:
    return weight * (1 / (1-0.02*reps))

def baechle(weight: float, reps: int) -> float:
    return weight * (1+ 0.033*reps)

def berger(weight: float, reps: int) -> float:
    return weight * 1 / (1.0261* np.exp(-0.0262*reps))

def brown(weight: float, reps: int) -> float:
    return weight * (0.9849 + 0.0328 * reps)

def brzycki(weight: float, reps: int) -> float:
    return weight * (36 / (37-reps))

def epley(weight: float, reps: int) -> float:
    return weight * (1 + reps / 30)

def kemmler(weight: float, reps: int) -> float:
    return weight * (0.988+0.0104*reps+0.00190*reps**2-0.0000584*reps**3)

def kellner(weight: float, reps: int) -> float:
    """This one might be wrong, need to check. Not included in calcs"""
    return weight* (102 * np.exp(-0.0338*reps))

def landers(weight: float, reps: int) -> float:
    return weight* (1 / (1.013 - 0.0267123 * reps))

def lombardi(weight: float, reps: int) -> float:
    return weight* reps ** 0.1

def mayhew(weight: float, reps: int) -> float:
    return weight * (1 / (0.522 + 0.419 * np.exp(-0.055 * reps)))

def naclerio(weight: float, reps: int) -> float:
    return weight * (1 / (0.951 * np.exp(-0.021 * reps)))

def oconner(weight: float, reps: int) -> float:
    return weight * (1 + 0.025 * reps)

def wathen(weight: float, reps: int) -> float:
    return weight * (1 /(0.4880+0.538*np.exp(-0.075 * reps)))

def lift_curve(func, weight: float, reps: int = 20):
    x = np.arange(start=0, stop=reps, step=1)
    y = [func(weight,r) for r in x]
    return x, y

class OneRepMax:
    def __init__(self, weight: float, reps: int, unit='pound', ):
        self.weight = np.float64(weight)
        self.reps = reps
        self.unit= unit
        self.calculations = [adams, baechle, berger, brown, brzycki, epley, kemmler, landers, lombardi, mayhew, naclerio, oconner, wathen]
        self.calculated_one_rep_maxes ={func.__name__: round(func(self.weight, self.reps), 2) for func in self.calculations}

    @property
    def values(self):
        return list(self.calculated_one_rep_maxes.values())

    @property
    def mean(self):
        return Quantity(np.mean(self.values), self.unit)
    
    @property
    def min(self):
        return Quantity(np.min(self.values), self.unit)
    
    @property
    def max(self):
        return Quantity(np.max(self.values), self.unit)
    
    @property
    def box(self):
        return px.box(self.values, points='all')
    
    def get_lift_curves(self,):
        return {func.__name__: lift_curve(func, weight=self.weight,) for func in self.calculations}
        
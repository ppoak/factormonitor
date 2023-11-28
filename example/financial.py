import numpy as np
import pandas as pd
import dataforge as forge
from .base import BackTestFactor


class PE(BackTestFactor):

    def __init__(self, profit: pd.Series, equity: pd.Series):
        super().__init__(
            name = "pe",
            table = forge.AssetTable("/home/data/factor/"),
            profit = profit,
            equity = equity,
        )
    
    def compute(self):
        self.profit: pd.Series; self.equity: pd.Series
        self.factor = self.profit / self.equity
        self.factor = self.factor.dropna().sort_index()
        return self

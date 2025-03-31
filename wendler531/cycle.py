import pandas as pd

from wendler531.utilities import round_to_nearest_5

WENDLER_REP_SCHEME = {
        "week-1": ((5, 0.65), (5, 0.75), (5, 0.85)),
        "week-2": ((3, 0.70), (3, 0.80), (3, 0.90)),
        "week-3": ((5, 0.75), (3, 0.85), (1, 0.95)),
        "week-4": ((5, 0.40), (5, 0.50), (5, 0.60)),
    }

class Cycle:
    def __init__(self, wendler_one_rep_max: float) -> pd.DataFrame:
        self.worm = wendler_one_rep_max


    def build_records(self):
        columns = {}
        for week, scheme in WENDLER_REP_SCHEME.items():
            columns[week] = [str(i[0]) + "x" + str(round_to_nearest_5(self.worm * i[1])) for i in scheme]
        return columns
    
    @property
    def table(self):
        return pd.DataFrame.from_dict(self.build_records(),)
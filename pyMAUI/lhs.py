from smt.sampling_methods import LHS
import pandas as pd


def lhs_sample(x_names, x_limits, num, file_name):
    sampling = LHS(xlimits=x_limits)
    x = sampling(num)

    df = pd.DataFrame(data=x, columns=x_names)

    df.to_csv(file_name, index=False)

    return df

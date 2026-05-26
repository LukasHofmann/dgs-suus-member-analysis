import pandas as pd
import os


def load_members():
    """Loads the DGS section member list from local CSV and returns a DataFrame."""

    # Build path relative to this file's location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'data', 'members.csv')

    df = pd.read_csv(file_path, sep=';')


    return df
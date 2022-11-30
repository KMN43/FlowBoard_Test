import pandas as pd


def pandas_format():

    options = {
        "display": {
            "max_columns": None,
            "max_colwidth": 100,
            "expand_frame_repr": False,
            "max_rows": 1000,
            "max_seq_items": 1000,
            "precision": 4,
            "show_dimensions": False
        },
        "mode": {
            "chained_assignment": None
        }
    }

    for category, option in options.items():
        for op, value in option.items():
            pd.set_option(f"{category}.{op}", value)


if __name__ == "__main__":
    pandas_format()
    del pandas_format
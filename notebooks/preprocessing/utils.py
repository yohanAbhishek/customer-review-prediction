import pandas as pd
import json

def load_json_data(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))

    df = pd.DataFrame(data)
    return df
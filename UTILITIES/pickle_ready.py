import mmcv, pickle
import json
import numpy as np


# convert pickle to json.
with open("results.pkl", "rb") as f:
    results = pickle.load(f)

def convert(o):
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"Object type {o.__class__.__name__} is not json serializable")


# Save to a JSON file
with open("results.json", "w") as f:
    json.dump(results, f, default=convert, indent=4)

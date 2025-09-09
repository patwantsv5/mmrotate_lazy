import mmcv, pickle
import json
import numpy as np
import math

# Load Pickle
with open("UTILITIES/demo_results.pkl", "rb") as f:
    results = pickle.load(f)

# Recursive converter
def clean(obj):
    if isinstance(obj, np.ndarray):
        obj = obj.tolist()
    if isinstance(obj, list):
        # If detection format: [cx, cy, w, h, angle, score]
        if len(obj) == 6 and all(isinstance(x, (int, float)) for x in obj):
            obj[4] = obj[4] * 180.0 / math.pi  # rad → deg
            return obj
        else:
            return [clean(x) for x in obj]
    if isinstance(obj, dict):
        return {k: clean(v) for k, v in obj.items()}
    return obj

# Convert results safely
cleaned_results = clean(results)

# Save as JSON
with open("UTILITIES/demo_result_results.json", "w") as f:
    json.dump(cleaned_results, f, indent=4)

import argparse
import pandas as pd
import joblib

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input_csv", type=str, required=True)
parser.add_argument("--model_path", type=str, required=True)
parser.add_argument("--output_csv", type=str, required=True)
args = parser.parse_args()

# Load model
model = joblib.load(args.model_path)

# Load new data
df = pd.read_csv(args.input_csv)
X = df[["hours_studied", "attendance_percentage"]]

# Predict
predictions = model.predict(X)
df["prediction"] = ["pass" if p == 1 else "fail" for p in predictions]

# Save result
df.to_csv(args.output_csv, index=False)
print(f"✅ Predictions saved to {args.output_csv}")

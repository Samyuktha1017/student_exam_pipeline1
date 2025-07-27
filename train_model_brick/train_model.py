import argparse
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Parse CLI args
parser = argparse.ArgumentParser()
parser.add_argument("--input_csv", type=str, required=True)
parser.add_argument("--model_output", type=str, required=True)
args = parser.parse_args()

# Load dataset
df = pd.read_csv(args.input_csv)

# Convert label to binary
df["label"] = df["label"].map({"pass": 1, "fail": 0})

X = df[["hours_studied", "attendance_percentage"]]
y = df["label"]

# Train/test split (optional but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, args.model_output)
print(f"✅ Model saved to {args.model_output}")

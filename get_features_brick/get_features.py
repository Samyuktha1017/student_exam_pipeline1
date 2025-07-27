import argparse
import pandas as pd
from feast import FeatureStore

parser = argparse.ArgumentParser()
parser.add_argument("--entity_csv", type=str, required=True)
parser.add_argument("--feature_view_name", type=str, required=True)
parser.add_argument("--repo_path", type=str, required=True)
parser.add_argument("--output_csv", type=str, required=True)
args = parser.parse_args()

entity_df = pd.read_csv(args.entity_csv)
store = FeatureStore(repo_path=args.repo_path)

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[f"{args.feature_view_name}:hours_studied", f"{args.feature_view_name}:attendance_percentage"]
).to_df()

training_df.to_csv(args.output_csv, index=False)
print("✅ Features saved to:", args.output_csv)

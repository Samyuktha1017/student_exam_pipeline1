 Student Exam Pass Prediction Pipeline (Feast + Kubeflow + Elyra)

This repository demonstrates an end-to-end (E2E) ML pipeline using modular, Dockerized components (bricks), centered around **Feast Feature Store** for historical feature retrieval.


 Objective

Predict whether a student will pass or fail based on:
- `hours_studied`
- `attendance_percentage`


 Bricks (Components)

| Brick Name         | Description                                                  | Docker Image                                               |
|--------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| `get_features`     | Uses **Feast** to retrieve historical features                | `samyukthagudiya17/get_features:latest`                    |
| `train_model`      | Trains logistic regression model using retrieved features     | `samyukthagudiya17/train_model:latest`                     |
| `predict_student`  | Predicts student outcome (`pass`/`fail`) using trained model  | `samyukthagudiya17/predict_student:latest`                 |


GitHub Raw Links (for Elyra or Kubeflow)

| Brick             | component.yaml (Raw GitHub URL) |
|------------------|----------------------------------|
| `get_features`   | [🔗 Click here](https://raw.githubusercontent.com/Samyuktha1017/student_exam_pipeline1/main/get_features_brick/component.yaml) |
| `train_model`    | [🔗 Click here](https://raw.githubusercontent.com/Samyuktha1017/student_exam_pipeline1/main/train_model_brick/component.yaml) |
| `predict_student`| [🔗 Click here](https://raw.githubusercontent.com/Samyuktha1017/student_exam_pipeline1/main/predict_student_brick/component.yaml) |



Elyra Pipeline Flow
graph TD
    A[get_features] --> B[train_model]
    B --> C[predict_student]

| Parameter           | Type   | Description                           |
| ------------------- | ------ | ------------------------------------- |
| `entity_csv`        | String | Path to CSV with student IDs + labels |
| `feature_view_name` | String | Name of feature view in Feast         |
| `repo_path`         | String | Path to Feast feature repo            |
| `output_csv`        | Output | Output file with full feature vectors |


| Parameter      | Type   | Description                      |
| -------------- | ------ | -------------------------------- |
| `input_csv`    | String | Feature CSV (from get\_features) |
| `model_output` | Output | Trained model file (`.joblib`)   |


| Parameter    | Type   | Description           |
| ------------ | ------ | --------------------- |
| `input_csv`  | String | New student records   |
| `model_path` | String | Path to trained model |
| `output_csv` | Output | Predicted labels CSV  |


Tools used:

| Tool                     | Purpose                                    |
| ------------------------ | ------------------------------------------ |
| **Feast**                | Feature registration, retrieval            |
| **Docker**               | Containerization of ML pipeline components |
| **Elyra**                | Pipeline orchestration with drag & drop    |
| **GitHub**               | Hosting component YAMLs via raw URLs       |
| **Kubeflow**             | Pipeline deployment and execution          |
| **Postman** *(optional)* | API testing (for future inference)         |

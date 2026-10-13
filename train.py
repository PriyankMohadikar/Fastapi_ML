import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Read the dataset
def load_data():
    return pd.read_csv("rag_data/Q2_Car_Data.csv")


# Encode all categorical columns
def encode_data(df):

    X = df.drop("class", axis=1)
    y = df["class"]

    label_encoders = {}

    # Encode input columns
    for column in X.columns:
        encoder = LabelEncoder()
        X[column] = encoder.fit_transform(X[column])
        label_encoders[column] = encoder

    # Encode output column
    target_encoder = LabelEncoder()
    y = target_encoder.fit_transform(y)

    return X, y, label_encoders, target_encoder


# Scale features using only training data
def scale_data(X_train, X_test):

    scaler = StandardScaler()

    # Learn scaling values from training data
    X_train = scaler.fit_transform(X_train)

    # Apply same scaling on test data
    X_test = scaler.transform(X_test)

    return X_train, X_test, scaler


# Train all three models
def train_models(X_train, y_train):

    models = {
        "AdaBoost": AdaBoostClassifier(n_estimators=100),
        "RandomForest": RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            random_state=42
        ),
        "SVM": SVC(kernel="rbf")
    }

    trained_models = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model

    return trained_models


# Compare all models and return the best one
def evaluate_models(models, X_test, y_test):

    best_model = None
    best_accuracy = 0

    print("\nModel Comparison\n")

    for name, model in models.items():

        prediction = model.predict(X_test)

        accuracy = accuracy_score(y_test, prediction)
        precision = precision_score(y_test, prediction, average="weighted")
        recall = recall_score(y_test, prediction, average="weighted")
        f1 = f1_score(y_test, prediction, average="weighted")

        print(name)
        print("Accuracy :", round(accuracy, 4))
        print("Precision:", round(precision, 4))
        print("Recall   :", round(recall, 4))
        print("F1 Score :", round(f1, 4))
        print("-" * 30)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model

    print("\nBest Model Saved.")

    return best_model


# Save model and preprocessing objects
def save_objects(best_model, label_encoders, scaler, target_encoder):

    with open("models/best_model.pkl", "wb") as file:
        pickle.dump(best_model, file)

    with open("models/label_encoders.pkl", "wb") as file:
        pickle.dump(label_encoders, file)

    with open("models/scaler.pkl", "wb") as file:
        pickle.dump(scaler, file)

    with open("models/target_encoder.pkl", "wb") as file:
        pickle.dump(target_encoder, file)

    print("All pickle files saved inside models folder.")


# Execute complete training pipeline
def main():

    df = load_data()

    X, y, label_encoders, target_encoder = encode_data(df)

    # Split data into 80:20
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Prevent data leakage by fitting scaler only on training data
    X_train, X_test, scaler = scale_data(X_train, X_test)

    models = train_models(X_train, y_train)

    best_model = evaluate_models(models, X_test, y_test)

    save_objects(best_model, label_encoders, scaler, target_encoder)


# Run training only when train.py is executed
# if __name__ == "__main__":
#     main()
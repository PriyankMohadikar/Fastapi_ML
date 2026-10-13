# logic for CURD operation using database insert eg
from db import get_connection
import pickle
import pandas as pd


def insert_product_service(product):
    entry = (product.product_id, product.product_name, product.category, product.price, product.stock_quantity)
    sql = "INSERT INTO product_info (product_id, product_name, category, price, stock_quantity) VALUES (%s, %s, %s, %s, %s)"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql, entry)
    print("Rows inserted:", cur.rowcount)
    print("Committed")
    conn.commit()
    cur.close()
    conn.close()


# Load pickle files once when FastAPI starts
with open("models/best_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/label_encoders.pkl", "rb") as file:
    label_encoders = pickle.load(file)

with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("models/target_encoder.pkl", "rb") as file:
    target_encoder = pickle.load(file)


# Convert input into prediction
def predict_car(car_data):

    df = pd.DataFrame([car_data])

    # Encode user input
    for column in df.columns:
        df[column] = label_encoders[column].transform(df[column])

    # Apply saved scaling
    scaled_data = scaler.transform(df)

    # Predict
    prediction = model.predict(scaled_data)

    # Convert prediction back to original label
    result = target_encoder.inverse_transform(prediction)
    return result[0]




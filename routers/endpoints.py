from fastapi import APIRouter

from schemas.sample_schema import Product, CarInput
from services.allservices import insert_product_service, predict_car

# Calling Function from the services like insert Update delete

router = APIRouter(tags=["Rag"])

@router.post("/insertproduct")
def insert_product(product: Product):
    try:
        insert_product_service(product)
        return {"Message": "Product inserted successfully"}
    except Exception as e:
        return {"Message": str(e)}


# Prediction endpoint
@router.post("/predict")
def prediction(car: CarInput):
    result = predict_car(car.model_dump())
    return {
        "Predicted Class": result
    }
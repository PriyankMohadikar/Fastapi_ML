# Car Evaluation API

This project uses machine learning to predict a car's acceptability
based on six details: buying price, maintenance cost, number of doors,
passenger capacity, luggage boot size, and safety.

I trained three classification models and compared their results before
saving the best-performing model. The saved model is then used by a
FastAPI endpoint, so predictions can be tested through Swagger without
training the model every time the API starts.

## What the project does

-   Trains and compares AdaBoost, Random Forest, and SVM.
-   Splits the dataset into 80% training data and 20% testing data.
-   Measures each model using accuracy, precision, recall, and F1 score.
-   Encodes the categorical values and scales the input features.
-   Saves the selected model and preprocessing objects as pickle files.
-   Accepts car details as JSON and returns a predicted class through
    FastAPI.
-   Uses Pydantic to validate the request body.

## Project structure

``` text
Fastapi_Rag/
├── models/
│   ├── best_model.pkl
│   ├── label_encoders.pkl
│   ├── scaler.pkl
│   └── target_encoder.pkl
├── rag_data/
│   └── Q2_Car_Data.csv
├── routers/
│   └── endpoints.py
├── schemas/
│   └── sample_schema.py
├── services/
│   └── allservices.py
├── main.py
├── train.py
└── requirements.txt
```

The `.pkl` files are created when `train.py` runs. They should be
available before starting the API.

## Setup

You will need Python and pip installed.

1.  Clone the repository and open its folder:

    ``` bash
    git clone https://github.com/PriyankMohadikar/Fastapi_ML.git
    cd Fastapi_ML
    ```

2.  Create and activate a virtual environment on Windows:

    ``` bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  Install the packages:

    ``` bash
    pip install -r requirements.txt
    ```

## Train the model

Run the training script when you want to create or update the saved
model files:

``` bash
python train.py
```

The script prints the evaluation results for all three models and saves
the selected model and preprocessing objects in the `models` folder. You
do not need to run this script each time you start the API. Run it again
only when you want to retrain the model, for example after changing the
dataset or training code.

## Start the API

After the pickle files have been created, start FastAPI:

``` bash
uvicorn main:app --reload
```

Open the Swagger page in your browser:

<http://127.0.0.1:8000/docs>

Choose `POST /predict`, click **Try it out**, enter the JSON below, and
click **Execute**.

## Example request

``` json
{
  "buying": "med",
  "maint": "low",
  "doors": "3",
  "persons": "more",
  "lug_boot": "med",
  "safety": "high"
}
```

The API returns the predicted car class. The possible classes in the Car
Evaluation dataset are `unacc`, `acc`, `good`, and `vgood`.

Use the values shown in the example or other values present in the
dataset. Empty strings and unsupported category values should be
rejected by input validation.

## Model results

In my training run, the models gave these results on the test split:

  Model             Accuracy   Precision   Recall   F1 score
  --------------- ---------- ----------- -------- ----------
  AdaBoost            83.53%      82.05%   83.53%     80.94%
  Random Forest       95.95%      96.83%   95.95%     96.14%
  SVM                 90.17%      90.02%   90.17%     90.07%

Random Forest performed best in this run, so it was selected and saved
as `best_model.pkl`. Your results may differ if the dataset or training
settings change.

## Files saved in `models`

-   `best_model.pkl`: the selected trained classifier.
-   `label_encoders.pkl`: encoders used to convert input categories into
    numbers.
-   `scaler.pkl`: the fitted scaler used during training.
-   `target_encoder.pkl`: converts the predicted class back to its
    original label.

The API loads these files and reuses them for predictions. This keeps
model training separate from serving API requests.

## Built with

-   Python
-   pandas
-   scikit-learn
-   FastAPI
-   Pydantic
-   Uvicorn
-   pickle

## Notes

This is a learning project built to practise model evaluation,
preprocessing, saving a trained model, and serving predictions through a
REST API.

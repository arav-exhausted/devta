from fastapi import FastAPI
from fastapi import HTTPException
import joblib
from schema import DeliveyInput,display_result
from reasons import reasons_for_too_much_late
from preprocess import preprocess


RMSE = 3.8912
app = FastAPI()



model = joblib.load("../model/model.pkl")

@app.get("/")
def root():
    return{
        "Mesasge":"Delivery time prediction model is ready!"
    }


@app.post("/predict",response_model=display_result)
def predict(data:DeliveyInput):

    try: 
        input_data = data.model_dump()
        processed_data = preprocess(input_data)
        
        prediction = float(model.predict(processed_data)[0])
        
        predicted_time = round(prediction)
    
        expected_min = max(0, round(prediction - RMSE))
        expected_max = round(prediction + RMSE)
        reasons_for_late = reasons_for_too_much_late(input_data)
        return {
        "predicted_delivery_time_min": predicted_time,
        "expected_min": expected_min,
        "expected_max": expected_max,
        "reasons":reasons_for_late
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f'Prediction failed: {str(e)}'
        )



@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": True
    }
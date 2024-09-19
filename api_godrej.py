from fastapi import FastAPI
from pydantic import BaseModel
import os

if __name__ == "__main__":
    # Get the port from the environment variable or default to 8000 for local testing
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

app = FastAPI()

price_list = {
    "1A": 55,  # Price for item 1
    "1B": 55,  # Price for item 2
    "1C": 55,  # Price for item 3
    "2A": 80,  # Price for item 4
    "2B": 315,  # Price for item 5
    "3A": 110,  # Price for item 6
    "3B": 200,  # Price for item 7
    "3C": 290   # Price for item 8
}

class QuantityRequest(BaseModel):
    quantity_1A: int
    quantity_1B: int
    quantity_1C: int
    quantity_2A: int
    quantity_2B: int
    quantity_3A: int
    quantity_3B: int
    quantity_3C: int
    

@app.get('/test')
async def read_root():
    return {'Message': 'Successful API'}

@app.post("/calculate_total")
async def calculate_total(quantity: QuantityRequest):
    total = (quantity.quantity_1A * price_list["1A"] +
             quantity.quantity_1B * price_list["1B"] +
             quantity.quantity_1C * price_list["1C"] +
             quantity.quantity_2A * price_list["2A"] +
             quantity.quantity_2B * price_list["2B"] +
             quantity.quantity_3A * price_list["3A"] +
             quantity.quantity_3B * price_list["3B"] +
             quantity.quantity_3C * price_list["3C"])
    
    return {"totalAmount": total}

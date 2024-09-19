from fastapi import FastAPI
from pydantic import BaseModel

price_list = {
    "1A": 55,  # Price for item 1A
    "1B": 55,  # Price for item 1B
    "1C": 55,  # Price for item 1C
    "2A": 80,  # Price for item 2A
    "2B": 315,  # Price for item 2B
    "3A": 110,  # Price for item 3A
    "3B": 200,  # Price for item 3B
    "3C": 290   # Price for item 3C
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
    
app = FastAPI()

@app.post("/calculate_total")
def calculate_total(quantity: QuantityRequest):
    total = (
        quantity.quantity_1A * price_list["1A"] +
        quantity.quantity_1B * price_list["1B"] +
        quantity.quantity_1C * price_list["1C"] +
        quantity.quantity_2A * price_list["2A"] +
        quantity.quantity_2B * price_list["2B"] +
        quantity.quantity_3A * price_list["3A"] +
        quantity.quantity_3B * price_list["3B"] +
        quantity.quantity_3C * price_list["3C"]
    )
    
    return {"totalAmount": total}

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class SumResponse(BaseModel):
    OriginalNumber: int
    Sum: int
    
@app.get("/sum/{num}", response_model=SumResponse)
def CalculateSum(num: int):
    print(f"Running the square function in backend with request value of {num}")
    return{
        "OriginalNumber" : num,
        "Sum" : num + num,
        "extra_feild" : "ignored"
    }


# extra_field return kiya,
# lekin response_model usko remove kar dega
from fastapi import FastAPI,Depends
from pydantic import BaseModel
import asyncio  #Python's Asynchronous programming library hai jo multiple tasks ko non-blocking way me manage karti hai. Isme event loop hota hai jo wait karte 
# waqt doosre tasks run kar deta hai (jaise API calls, DB calls)
# For Example: Agar 10 API Calls ayi hn to asyncio unhe parallel-like handle kar sakta hai instead of one-by-one

app = FastAPI()
@app.get("/hello/{name}")
def sayHello(name: str):
    print("Backend function executed successfully!")
    return {"message" : f"Hello {name}"}
    #return {"f"Hello {name}"}
    #return {"message": f"Hello {name}"} correct hai — ye dictionary (JSON object) return kar raha hai
    # return {f"Hello {name}"} ye dictionary nahi, set bana raha hai
    # FastAPI normally JSON (dict) return karta hai — isliye key-value format best practice hai


#------------------------------------------------------------------------------------------------
#------------------------------------Response Model ---------------------------------------------
class SumResponse(BaseModel):
    OriginalNumber: int
    Sum: int
    
@app.get("/sum/{num}", response_model=SumResponse)
def CalculateSum(num: int):
    print(f"Running the square function in backend with request value of {num}")
    return{
        "OriginalNumber" : num,
        "Sum" : num + num,
        "extra_feild" : "ignored"  # extra_field return kiya, lekin response_model usko remove kar dega

    }


#------------------------------------------------------------------------------------------------
#------------------------------------ Dependency Injection ---------------------------------------------
def get_multiplier():
    print("Called Multiplier Function and providing dependency to multiply function")
    return 3

@app.get("/multiply/{num}")
def multiply(num:int, multiplier: int = Depends(get_multiplier)):
    print("Running Multiply Function")
    result = num * multiplier
    return{
        "number" : num,
        "multiplier": multiplier,
        "result": result
    }






#------------------------------------- Asynchronization ---------------------------


@app.get("/delay/{seconds}")
async def delay(seconds: int):
    print("Waiting.....")
    await asyncio.sleep(seconds)
    print("Done Waiting")
    return{
        "waited_seconds" : seconds
    }
    






if __name__ == "__main__":
    import uvicorn
    
    try:
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            log_level="info",
            reload=False
        )
    except Exception as e:
        print(f"\n Failed to start server: {e}")
        print("\n Quick Fix Checklist:")
        print("1. Install missing packages:")
        print("   pip install jellyfish fuzzywuzzy python-Levenshtein")
        print("2. Make sure PostgreSQL is running")
        print("3. Check if port 8000 is available")
        print("4. Try: python -m backend (if saved as backend.py)")
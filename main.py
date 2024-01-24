from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

class ServiceCreationRequest(BaseModel):
    description: str

@app.post("/createService")
async def create_service(request: ServiceCreationRequest):
    if not request.description:
        raise HTTPException(status_code=400, detail="Description is required.")
    
    # 여기서 서비스 생성 로직을 구현합니다. 예시로는 UUID를 사용합니다.
    result_uuid = str(uuid.uuid4())
    result_url = f"https://gpts.msaez.io/result/{result_uuid}"
    
    return {"resultUrl": result_url}

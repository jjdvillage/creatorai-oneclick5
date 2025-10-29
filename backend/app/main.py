from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .config import CLIENT_URL
from .auth.router import router as auth_router
from .providers.llm_openai import generate_script_pack

app = FastAPI()
origins = [CLIENT_URL] if CLIENT_URL not in ['*',''] else ['*']
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
@app.get('/health')
def health(): return {'ok': True}
app.include_router(auth_router)
class ScriptRequest(BaseModel):
    topic: str
    channel: str = 'tiktok'
    tone: str = 'fun'
    length_sec: int = 30
@app.post('/api/generate')
async def api_generate(req: ScriptRequest):
    return await generate_script_pack(req.topic, req.channel, req.tone, req.length_sec)

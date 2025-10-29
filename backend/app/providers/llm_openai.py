import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY','')
async def generate_script_pack(topic:str, channel:str, tone:str, length_sec:int):
    if not OPENAI_API_KEY:
        return {'hook': f'Hook for: {topic}','script_timestamps':[{'t':0,'line':'Intro'}],'captions':['Caption'],'hashtags':['#ai']}
    return {'hook': f'(AI) Hook for: {topic}','script_timestamps':[{'t':0,'line':'Intro (AI)'}],'captions':['(AI) Caption'],'hashtags':['#ai']}

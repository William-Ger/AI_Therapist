from fastapi import FastAPI, Request
import main  # Replace with the name of your script
import json
from mangum import Mangum

app = FastAPI()

@app.post("/generate_report")
async def generate_report(user_input_text: str,request: Request):
    # Call the function in your script to generate the report (replace 'your_script' and 'generate_therapy_report' accordingly)
    report = main.generate_therapy_report(user_input_text)
    return_data = {}
    return_data['response'] = report
    return json.dumps(return_data, indent=4, default=str)

handler = Mangum(app, lifestyle ="off")
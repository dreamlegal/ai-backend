# main.py

import os
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import openai
from compatibility_test import check_compatibility
from utils import extract_json_from_string  
from fastapi.responses import JSONResponse
from utils import SAMPLE_REPORT
# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

app = FastAPI()

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(messages: dict):

    product_profile = messages['product_profile']
    user_profile = messages['user_profile']
    if not messages or not isinstance(messages, dict):
        return {"error": "Invalid message format. Message must be a non-empty string."}
    
    try:
        # Process the message with OpenAI
        response = await get_openai_response(product_profile, user_profile, messages)
        response_json= extract_json_from_string(str(response))
        # Return the response
        return JSONResponse(content={"response": response_json})
    except Exception as e:
        return {"error": "An error occurred while processing your message"}
    
@app.post("/compatibility")
async def compatibility_endpoint(user_profile: dict, product_profile: dict):
    # Validate that both profiles are dictionaries
    if not isinstance(user_profile, dict) or not isinstance(product_profile, dict):
        return {"error": "Both user_profile and product_profile must be dictionaries"}
    
    # Validate required fields in user profile
    required_user_fields = ["Location", "CompanyType", "PrimaryLanguage", "Industry", "TeamSize", "Goals"]
    missing_user_fields = [field for field in required_user_fields if field not in user_profile]
    if missing_user_fields:
        return {"error": f"Missing required fields in user_profile: {', '.join(missing_user_fields)}"}
    
    # Validate required fields in product profile
    required_product_fields = ["focusCountries", "languages", "userCategory", "industry", "teamSize"]
    missing_product_fields = [field for field in required_product_fields if field not in product_profile]
    if missing_product_fields:
        return {"error": f"Missing required fields in product_profile: {', '.join(missing_product_fields)}"}
    
    try:
        response = check_compatibility(product_profile, user_profile)
        return {"response": response}
    except Exception as e:
        return {"error": "An error occurred while processing your request"}




workflow_report_json = {}

@app.post("/workflow_report")
# workflow report
async def workflow_report(workflow_report: dict):
    try:

        # workflow report
        messages = [
            {"role": "system", "content": f"Here is the sample report: {SAMPLE_REPORT}"},
            {"role": "user", "content": f"Here is the workflow report in json format captured from legal operation team: {workflow_report} You are a legal operation expert who analyzes the workflow with heads like current status,current losses, red flags ,green flags, , possibilities of automation, possibilities of efficiency, scope of improvement, future steps.  use the metrics and numbers to make the report more accurate and meaningful. IMPORTANT: return the report in json format"}
        ]
        response = openai.chat.completions.create(
            model="gpt-4o",  # or "gpt-3.5-turbo"
            messages=messages,
        )


        html_response = response.choices[0].message.content.strip()

        return JSONResponse(content={"response": extract_json_from_string(html_response)})
    except Exception as e:
        return {"error": "An error occurred while processing your request"}



async def get_openai_response(product_profile: dict, user_profile: dict, messages: dict) -> str:
    try:

        # Convert messages to list if it's not already
        # Validate messages format

        # set system context messages
        system_messages = [
            {"role": "system", "content": "You are a helpful assistant that helps users find the best product/software/solution for their needs and return only json format with message and suggestive_questions as keys."},
            {"role": "system", "content": f"Product profile: {json.dumps(product_profile)}"},
            {"role": "system", "content": f"User profile: {json.dumps(user_profile)}"},
            {"role": "system", "content": f"Also give suggestive questions that user can ask about product profile based on the product profile and user profile in  clean json format: with message and suggestive_questions as keys based on previous conversation the suggesive questions should be based only on user or product profile"},
        ]

        # add system messages to the beginning of the messages list
        messages['messages'] = system_messages + messages['messages']

        response = openai.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=messages['messages'],
            stop=None,
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return "Sorry, I couldn't process that."
    



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

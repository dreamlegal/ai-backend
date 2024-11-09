# main.py

import os
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import openai
from compatibility_test import check_compatibility

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
    print(f"Received messages: {messages}")
    if not messages or not isinstance(messages, dict):
        return {"error": "Invalid message format. Message must be a non-empty string."}
    
    try:
        print(f"Received message: {messages}")
        # Process the message with OpenAI
        response = await get_openai_response(product_profile, user_profile, messages)
        # Return the response
        return {"response": response}
    except Exception as e:
        print(f"Error: {e}")
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
        print(f"Error: {e}")
        return {"error": "An error occurred while processing your request"}

async def get_openai_response(product_profile: dict, user_profile: dict, messages: dict) -> str:
    print(f"Received messages: {messages}")
    try:

        # Convert messages to list if it's not already
        print(f"Messages type: {type(messages)}")
        # Validate messages format

        # set system context messages
        system_messages = [
            {"role": "system", "content": "You are a helpful assistant that helps users find the best product/software/solution for their needs."},
            {"role": "system", "content": f"Product profile: {json.dumps(product_profile)}"},
            {"role": "system", "content": f"User profile: {json.dumps(user_profile)}"},

        ]

        # add system messages to the beginning of the messages list
        print(f"System messages: {system_messages}")
        messages['messages'] = system_messages + messages['messages']

        print(f"Sending messages to OpenAI: {messages['messages']}")
        response = openai.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=messages['messages'],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I couldn't process that."

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

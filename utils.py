import json
import re
def extract_json_from_string(string):
    # Use regex to find the JSON object in the string
    match = re.search(r'\{[^{}]*\}', string)
    if match:
        try:
            print(f"Match: {match.group(0)}")
            return json.loads(match.group(0))
        except json.JSONDecodeError as e:
            return {}
    return {}


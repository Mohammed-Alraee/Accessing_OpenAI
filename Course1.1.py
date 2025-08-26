import os 
import datetime

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from openai import RateLimitError # Testing API Key only. 

#Accesing openAI API 
_ = load_dotenv(find_dotenv()) # read local .env file
OpenAI.api_key = os.getenv('OPENAI_API_KEY') #same like .os.getenv (safer )

print("API Key:", OpenAI.api_key)


#model choosing
current_date = datetime.datetime.now().date()
target_date = datetime.date(2024, 6, 12)


# model selection
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"


#Example 2 output test:
client = OpenAI()
try:
    response = client.chat.completions.create(
     model=llm_model,
     messages=[
        {"role": "user", "content": "Hello, who are you?"},
    ]
    )

    print(response.choices[0].message.content)

except RateLimitError as e:
    print("🚫 You have hit a quota or rate limit error.")
    print(e)

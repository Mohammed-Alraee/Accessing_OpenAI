This Python script demonstrates how to connect to the OpenAI API using environment variables and make a simple chat completion request with error handling.

Key Points:

- Environment variables:
  The script loads the OpenAI API key from a local .env file using python-dotenv.
  This keeps your key secure and out of the code.

- API key setup:
  OpenAI.api_key is set from the environment variable OPENAI_API_KEY.

- Dynamic model selection:
  The script compares the current date to a target date (2024-06-12) and chooses between two model versions accordingly:
    - After the target date: uses "gpt-3.5-turbo"
    - Before or on the target date: uses "gpt-3.5-turbo-0301"
      
- Making a chat request:
  It sends a message "Hello, who are you?" to the selected model and prints the response.

- Error handling:
  If you hit a rate limit or quota, it catches the RateLimitError and prints an informative message.

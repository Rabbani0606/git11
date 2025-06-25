import openai

# Set your OpenAI API key
openai.api_key = "your-api-key-here"

# Create a chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like today?"}
    ]
)

# Print the assistant's reply
print(response['choices'][0]['message']['content'])


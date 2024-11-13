# Install ollama 
# pip install ollama

from ollama import Client
# Model names:
# mathQA
# llama-3.1-8B-4bit
# llama3.2
# llama3.1

client = Client(host='http://localhost:11434')
print("Called API....\n Waiting for responce...")
response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print("Responce")
# print(response)
print(response['message']['content'])
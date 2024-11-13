# Connect Python with Ollama
## Access Ollama as a Microservice
``` 
# Install ollama 
# pip install ollama

from ollama import Client

# Model Names those are already their in the system
# 1. mathQA
# 2. llama-3.1-8B-4bit
# 3. llama3.2
# 4. llama3.1


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
```

## Access Ollama as a Microservice
```
import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  async for part in await AsyncClient().chat(model='llama3.2', messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())
```








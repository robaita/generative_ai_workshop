# OLLAMA Commands
> **1. Show existing Models**   
List all the existing models    
```ollama list```   

> **2. Pull Model**   
Import the finetuned model from Ollama Model Repository
``` ollama pull <model name> ```   
``` ollama create <model anme> -f <model file>```   
Example    
``` ollama pull llama3.2 ```   
``` ollama create <model anme> -f llama-3.1-8b-python-code-file```   

> **3. Run Model**   
Run a particular model    
```ollama run <model name> ```  
Example   
```ollama run llama3.2```    

> **4. Remove a Model**   
Remove a particular model    
```ollama rm <model name> ```  
Example   
```ollama rm llama3.2```  

> **5. Serve a Model**   
Serve a particular model to access it as micro service   
```ollama server ```  

> **6. Serve and Access Model via LAN**   
Serve a particular model to access it as micro service in LAN  
```set OLLAMA_HOST=0.0.0.0 ```  
```ollama serve```

> **6. Ollama Version**   
To check current Ollama version   
```ollama -- version``` 









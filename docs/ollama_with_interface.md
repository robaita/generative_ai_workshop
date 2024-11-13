# OLLAMA with OpenWebUI
## What is OpenWebUI
Open Web UI (OWUI) is an open-source framework for building cross-platform desktop applications using web technologies. It provides a customizable, modular design with pre-built components and state management capabilities. Ideal for rapid prototyping, collaboration, and scalability, OWUI simplifies development without sacrificing native-like experiences across various operating systems.   

## Installation of OpenWebUI
### Docker Installation
To install Docker on Ubuntu, follow these steps:   
> **Step 1: Update System**   
Make sure your system is up to date by running:   
```sudo apt update```   
```sudo apt upgrade```   

> **Step 2: Install Required Dependencies**   
Install dependencies required for Docker installation:   
```sudo apt install apt-transport-https ca-certificates curl software-properties-common```   

> **Step 3: Add Docker's Official GPG Key**   
Add Docker’s official GPG key to verify the authenticity of the package:   
```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg```   

> **Step 4: Add Docker Repository**   
Add the Docker repository to your system's software sources:   
```echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null```   

> **Step 5: Update Package List**   
Update your system's package list again to include the Docker packages:   
```sudo apt update```   

> **Step 6: Install Docker**   
Now install Docker:   
```sudo apt install docker-ce```   

> **Step 7: Verify Docker Installation**   
Check that Docker is installed and running:   
```sudo systemctl status docker```   
To verify the Docker version, run:   
```docker --version```   

> **Step 8: Allow Docker to Run Without sudo (Optional)**   
To run Docker commands without sudo, add your user to the docker group:   
```sudo usermod -aG docker $USER```   
Then log out and back in, or restart your system.   

### [OpenWebUI Installation](https://docs.openwebui.com/) and Run
If Ollama is on your computer, use this command:   
``` docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main ```

After the docker is running   
Open the below address in the browser    
``` http://localhost:3000 ```   
The browser then should show the below page.   
![Interface image](https://github.com/robaita/generative_ai_workshop/blob/main/images/openwebui.png)   

**Here the llama model is shown that is deployed in Ollama, that shows that Ollama and Open Web UI are communicating with each other.**
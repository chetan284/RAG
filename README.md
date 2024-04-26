# RAG
BMCC Demo on RAG

Prerequisites 
1.Python 
2.Python Libraries 
3.Ollama* 4.OpenAI API Key*

Downloading and Installing Ollama: 
To run Mistral locally, download Ollama from the official website. 
Once downloaded, move Ollama to your /Applications directory (for macOS). 
You can now run Ollama from the terminal.

Running Mistral with Ollama:
Open your terminal and execute the following commands: 
For the default Instruct model: 
ollama run mistral 
Check if 
installed ollama list

How to install Python libraries (Skip if pip is available on your system) 
Download miniforge https://conda-forge.org/miniforge/ 
Run downloaded shell script with ./<script file> 
conda create -n rag python=3.11 
conda activate rag

Libraries that we will need for the demo Run below command 
pip install --upgrade --quiet langchain-openai tiktoken langchain-chroma langchain

Proffering IDE for code writing ? 
For VSCode 
Install Python Development Extension 
Install Jupyter
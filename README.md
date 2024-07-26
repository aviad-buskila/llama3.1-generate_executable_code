This is a demonstration of how a code can be generated and then executed within the same scope. 
Generation of the code is being done locally, no use of api call, or external connections at all. 
I used Lllma3.1 (8B model), installed locally using ollama (see installation guide at https://github.com/ollama/ollama).
Once you install, pull the model and run it, you can run using this code. 

In the file app.py, you should define 4 variables:
function_name - what is the name of the designated function the LLM should generate. 
prompt - the function signature. Make sure you keep the output and structure instructions as is if you'd like to preserve the usage of the entire code I provide here.
function_input - the input the generated function would run with to demonstrate validity. 
path_for_generated_function - the name of the file to store the generated code in. 




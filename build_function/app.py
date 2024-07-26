import globals
from ModelMethods import AskLlama
from ProcessReponse import Response

function_name = 'sum_lst'
prompt = f"""
Generate a code of a python function named {function_name}.
The function  gets as an argument a list of integers and calculates their sum. 
The function returns a dictionary of two keys, status - which describes if the input was valid, and sum - which holds 
the sum of the list. 
Return an executable code, with no additional characters, do not include the word python at the beginning of the text.
Also, do not enclose it with ``` 
"""
function_input = [1, 5, 19]
#######################################################################################################################


path_for_generated_function = 'generated.py'

model = AskLlama(globals.MODEL_NAME, globals.ROLE)
response = Response(model.ask(prompt))
response.create_response_file(path_for_generated_function)

try:
    import generated
    func = getattr(generated, function_name)
    print(func(function_input))
except Exception as e:
    print(f"An exception occurred: {e}")










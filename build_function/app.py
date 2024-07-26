import globals
from ModelMethods import AskLlama
from ProcessReponse import Response

prompt = """
return a code of python function named sum_lst which gets as an argument a list of integers and calculates their sum. The 
function returns a dictionary of two keys, status - which describes if the input was valid and sum - which holds the sum 
of the list. Return only the code, with no comments or documentation, the response should include only code, do not 
have the python word at the beginning of the text
"""

path_for_generated_function = 'generated.py'

model = AskLlama(globals.MODEL_NAME, globals.ROLE)
response = Response(model.ask(prompt))
response.create_response_file(path_for_generated_function)

try:
    from generated import sum_lst
    print(sum_lst([1,5,9]))
except:
  print("An exception occurred")



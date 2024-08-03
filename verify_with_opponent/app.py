import build_function.globals as globals
from build_function.ModelMethods import AskLlama, AskOpponent
from build_function.ProcessReponse import Response

function_name = 'max_points_on_a_line'
prompt = f"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.
Your response MUST BE an executable code, with no additional characters, method name MUST BE {function_name}
YOU MUST NOT include the word python at the beginning. Also, YOU MUST NOT enclose the response with ```"""
function_input = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
path_for_generated_function = 'generated_by_subject.py'
path_for_opponent_function = 'generated_by_opponent.py'

model = AskLlama(globals.MODEL_NAME, globals.ROLE)
response = Response(model.ask(prompt, globals.MODEL_TEMP))
response.create_response_file(path_for_generated_function)
try:
    import generated_by_subject
    with open(path_for_generated_function, "r") as file:
        func = file.read()
        validation_prompt = f"""Given the task {prompt}, 
        There is a suggested implementation which is:
        {func} 
        You task is to determine if is this implementation correct? 
        if so, Return a one word output: True, no additional characters at all.  
        If the solution is wrong, provide a correct solution. 
        Your response MUST BE an executable code, with no additional characters,
        YOU MUST NOT include the word python at the beginning. Also, YOU MUST NOT enclose the response with ```"""
        opponent = AskOpponent(globals.OPPONENT_MODEL, globals.OPPONENT_ROLE)
        response = Response(opponent.ask(validation_prompt, globals.OPPONENT_MODEL_TEMP))
        response.create_response_file(path_for_opponent_function)
        try:
            import generated_by_opponent
            with open(path_for_opponent_function, "r") as opp_res:
                opponent_response = opp_res.read()
                if opponent_response.lower().strip() == "true":
                    print("Both models agreed")
                    func = getattr(generated_by_subject, function_name)
                    print(func(function_input))
                else:
                    print("Opponent did not agree with subject model")
                    func = getattr(generated_by_subject, function_name)
                    opp_func = getattr(generated_by_opponent, function_name)
                    print(f"Subject model implementation: {func(function_input)}")
                    print(f"Opponent model implementation: {opp_func(function_input)}")
        except Exception as e:
            print(f"An exception occurred: {e}")
except Exception as e:
    print(f"An exception occurred: {e}")

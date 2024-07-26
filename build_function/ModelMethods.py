import ollama


class AskLlama:
    def __init__(self, model, role):
        self.model = model
        self.role = role

    def ask(self, prompt):
        response = ollama.chat(model=self.model, messages=[
            {
                'role': self.role,
                'content': prompt
            }])
        return response

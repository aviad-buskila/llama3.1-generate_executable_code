class Response:
    def __init__(self, response):
        self.response = response
        self.content = response['message']['content']

    def print_response(self):
        print(self.content)

    def create_response_file(self, path):
        with open(path, "w") as file:
            file.writelines(self.content)
            file.close()
        return f"File were stored as {path}"




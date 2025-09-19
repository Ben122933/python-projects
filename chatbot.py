from difflib import SequenceMatcher
from datetime import datetime
import ast
import operator

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod
}

class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()

    def get_best_response(self, user_input: str) -> tuple[str, float] | None:
        highest_similarity: float = 0.0
        best_match: str = 'Sorry, I did\'t understand that.'

        for response in self.responses:
            similarity: float = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match: str = self.responses[response] # type: ignore

        if highest_similarity < 0.5:
            best_match =  "Sorry, I didn't understand that."

        return best_match, highest_similarity

    @staticmethod
    def safe_eval(expr: str) -> float:
        def _eval(node):
            if isinstance(node, ast.BinOp):
                left = _eval(node.left)
                right = _eval(node.right)
                return operators[type(node.op)](left, right)
            elif isinstance(node, ast.Constant):  # Python 3.8+
                return node.value
            else:
                raise TypeError(node)

        node = ast.parse(expr, mode='eval').body
        return _eval(node)

    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you today?')

        while True:
            user_input: str = input('You: ')

            # Calculator feature
            if user_input.lower().startswith("calculate"):
                try:
                    expression = user_input.replace("calculate", "").strip()
                    result = self.safe_eval(expression)
                    print(f"{self.name}: The answer is {result}")
                except Exception:
                    print(f"{self.name}: Sorry, I couldn't calculate that.")
                continue  # skip normal response handling

            response, similarity = self.get_best_response(user_input)

            if response == 'GET_TIME':
                response = f'The time is {datetime.now():%H:%M}'

            elif response == 'Goodbye!':
                break

            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')


def main() -> None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'bye': 'Goodbye! Have a great day!',
        'give me a fact': 'Did you know Python was named after Monty Python, not the snake?',
        'who are you': 'I am your friendly Python chatbot, Bob!',
        'what is your name': 'My name is Bob!',
        'i want to leave': 'Goodbye!',
        'thanks': 'You\'re welcome!'
    }

    chatbot: ChatBot = ChatBot(name='Bob', responses=responses)
    chatbot.run()

if __name__ == '__main__':
    main()

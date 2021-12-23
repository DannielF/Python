""" 
@param category: category of the game(1-5)
 """


class Category:
    category = int
    question = str
    options = list
    answer = str

    def __init__(self, category, question, options, answer) -> None:
        self.category = category
        self.question = question
        self.options = options
        self.answer = answer

from sbpcg import VectorEvaluator

class SanityTester:
    def __init__(self, opponent, cases):
        self.evaluator = VectorEvaluator(opponent, True)
        self.cases = cases
    
    def run_cases(self):
        for case in self.cases:
            self.evaluator.evaluate(case)
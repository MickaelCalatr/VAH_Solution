class Interpreter(object):
    def __init__(self, max_goals, precision=0.75):
        super(Interpreter, self).__init__()
        self.precision = precision
        self.max_goals = max_goals

    def analyse(self, results):
        goals = 0
        for x in results:
            if self.is_goal(x):
                goals += 1
        return goals >= self.max_goals

    def are_goals(self, results, max=10):
        goals = 0
        for x in results:
            if self.is_goal(x):
                goals += 1
            else:
                goals = 0
            if goals >= 4:
                return True
        return goals

    def first_goal(self, results):
        for i, x in enumerate(results):
            if self.is_goal(x):
                return i
        return -1

    def last_goal(self, results):
        position = -1
        for i, x in enumerate(results):
            if self.is_goal(x):
                position = i
        return position

    def is_goal(self, result):
        return result[0] >= self.precision

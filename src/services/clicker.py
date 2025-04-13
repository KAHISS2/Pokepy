class Clicker:

    def __init__(self):
        self.points = 0
        self.points_per_click = 1
        self.meta = 50
        self.level = 1

    def increment(self, label):
        self.points += self.points_per_click
        label.configure(text=str(self.points))
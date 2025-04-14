class Clicker:

    def __init__(self, points, points_per_click, points_per_auto_clicker, auto_click_cost, click_cost, auto_click_level, click_level):
        self.points = points
        self.points_per_click = points_per_click
        self.points_per_auto_clicker = points_per_auto_clicker
        self.auto_click_cost = auto_click_cost
        self.click_cost = click_cost
        self.auto_click_level = auto_click_level
        self.click_level = click_level

    def init(self, informations):
        informations[0].configure(text=str(self.points))
        informations[1].configure(text=f"por segundo: {self.auto_click_level}")
        informations[2].configure(text=f"por click: {self.click_level}")
        informations[3].configure(text=f"+1 por click (P${self.click_cost})")
        informations[4].configure(text=f"+1 por segundo (P${self.auto_click_cost})")
        

    def increment(self, label):
        self.points += self.points_per_click
        label.configure(text=str(self.points))

    def autoClick(self, root, label):
        self.points += self.points_per_auto_clicker
        label.configure(text=str(self.points))
        root.after(1000, self.autoClick, root, label)

    def buy_click(self, labels, button):
        if self.points >= self.click_cost:
            self.points -= self.click_cost
            self.points_per_click += 1
            self.click_level += 1
            self.click_cost = int(self.click_cost + self.click_level)
            labels[0].configure(text=str(self.points))
            labels[1].configure(text=f"por click: {self.click_level}")
            button.configure(text=f"+1 por click (P${self.click_cost})")
    
    def buy_auto_clicker(self, labels, button):
        if self.points >= self.auto_click_cost:
            self.points -= self.auto_click_cost
            self.points_per_auto_clicker += 1
            self.auto_click_level += 1
            self.auto_click_cost = int(self.auto_click_cost + self.auto_click_level)
            labels[0].configure(text=str(self.points))
            labels[1].configure(text=f"por segundo: {self.auto_click_level}")
            button.configure(text=f"+1 por segundo (P${self.auto_click_cost})")
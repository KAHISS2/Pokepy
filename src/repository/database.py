import tkinter as tk

class ButtonTycoon:
    def __init__(self, master):
        self.master = master
        master.title("Button Tycoon")

        # Estado do jogo
        self.money = 0
        self.money_per_click = 1
        self.auto_clicker_level = 0
        self.auto_clicker_cost = 100

        # Interface
        self.money_label = tk.Label(master, text=f"Dinheiro: R$ {self.money}")
        self.money_label.pack()

        self.click_button = tk.Button(master, text="Apertar Botão", command=self.click)
        self.click_button.pack(pady=10)

        self.upgrade_button = tk.Button(master, text="Upgrade: +1 por clique (R$ 50)", command=self.upgrade_click)
        self.upgrade_button.pack(pady=5)

        self.auto_clicker_button = tk.Button(master, text=f"AutoClicker Nível {self.auto_clicker_level} (R$ {self.auto_clicker_cost})", command=self.buy_auto_clicker)
        self.auto_clicker_button.pack(pady=5)

        # Começar loop do autoclicker
        self.update_auto_clicker()

    def click(self):
        self.money += self.money_per_click
        self.update_display()

    def upgrade_click(self):
        if self.money >= 50:
            self.money -= 50
            self.money_per_click += 1
            self.update_display()

    def buy_auto_clicker(self):
        if self.money >= self.auto_clicker_cost:
            self.money -= self.auto_clicker_cost
            self.auto_clicker_level += 1
            self.auto_clicker_cost = int(self.auto_clicker_cost * 1.5)
            self.auto_clicker_button.config(text=f"AutoClicker Nível {self.auto_clicker_level} (R$ {self.auto_clicker_cost})")
            self.update_display()

    def update_display(self):
        self.money_label.config(text=f"Dinheiro: R$ {self.money}")

    def update_auto_clicker(self):
        self.money += self.auto_clicker_level
        self.update_display()
        self.master.after(1000, self.update_auto_clicker)

# Executar
root = tk.Tk()
app = ButtonTycoon(root)
root.mainloop()
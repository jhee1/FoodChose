from random import choice
import tkinter as tk

class FoodChooserGUI:
    def __init__(self, master):
        self.master = master
        master.title("Food Chooser")

        self.food = []

        self.prompt_label = tk.Label(master, text="What would you like to eat? Insert as many ideas as possible and I will choose a meal for you :)")
        self.prompt_label.pack()

        self.prompt_entry = tk.Entry(master)
        self.prompt_entry.pack()

        self.add_button = tk.Button(master, text="Add", command=self.add_food)
        self.add_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        self.choice_button = tk.Button(master, text="Choose a meal", command=self.choose_food)
        self.choice_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def add_food(self):
        prompt = self.prompt_entry.get()
        self.prompt_entry.delete(0, 'end')
        if prompt != "":
            self.food.append(prompt)
            self.result_label.configure(text=f"Adding {prompt} to your list")

    def choose_food(self):
        if len(self.food) > 0:
            result = choice(self.food)
            self.result_label.configure(text=f"I have chosen {result} for you!")
        else:
            self.result_label.configure(text="Your list is empty. Please add some food ideas first.")

root = tk.Tk()
my_gui = FoodChooserGUI(root)
root.mainloop()
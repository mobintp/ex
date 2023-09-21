# Import tkinter for GUI
import tkinter as tk

# Define the model class
class CalculatorModel:
    # Initialize the model with an expression attribute
    def __init__(self):
        self.expression = ""

    # Define a method to evaluate the expression and return the result
    def evaluate(self):
        try:
            return eval(self.expression)
        except:
            return "Error"

    # Define a method to clear the expression
    def clear(self):
        self.expression = ""

    # Define a method to append a character to the expression
    def append(self, char):
        self.expression += char

# Define the view class
class CalculatorView:
    # Initialize the view with a root window and a model reference
    def __init__(self, root, model):
        self.root = root
        self.model = model

        # Create a label to display the expression
        self.label = tk.Label(root, text=self.model.expression, font=("Arial", 20), bg="white", anchor="e")
        self.label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Create a list of buttons with their labels and commands
        buttons = [
            ("7", lambda: self.controller.append("7")),
            ("8", lambda: self.controller.append("8")),
            ("9", lambda: self.controller.append("9")),
            ("/", lambda: self.controller.append("/")),
            ("4", lambda: self.controller.append("4")),
            ("5", lambda: self.controller.append("5")),
            ("6", lambda: self.controller.append("6")),
            ("*", lambda: self.controller.append("*")),
            ("1", lambda: self.controller.append("1")),
            ("2", lambda: self.controller.append("2")),
            ("3", lambda: self.controller.append("3")),
            ("-", lambda: self.controller.append("-")),
            ("0", lambda: self.controller.append("0")),
            (".", lambda: self.controller.append(".")),
            ("=", self.controller.evaluate),
            ("+", lambda: self.controller.append("+")),
            ("C", self.controller.clear)
        ]

        # Loop through the buttons and create them on the grid
        for i in range(len(buttons)):
            # Get the button label and command
            label, command = buttons[i]

            # Create a button with the label and command
            button = tk.Button(root, text=label, font=("Arial", 20), command=command)

            # Calculate the row and column of the button on the grid
            row = i // 4 + 1
            col = i % 4

            # Place the button on the grid
            button.grid(row=row, column=col, sticky="nsew")

        # Configure the rows and columns to have equal weight
        for i in range(5):
            root.rowconfigure(i, weight=1)
        for i in range(4):
            root.columnconfigure(i, weight=1)

    # Define a method to update the label with the expression
    def update(self):
        self.label.config(text=self.model.expression)

# Define the controller class
class CalculatorController:
    # Initialize the controller with a model and a view reference
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Set the view's controller attribute to this controller
        self.view.controller = self

    # Define a method to append a character to the model's expression and update the view
    def append(self, char):
        self.model.append(char)
        self.view.update()

    # Define a method to evaluate the model's expression and update the view
    def evaluate(self):
        result = self.model.evaluate()
        self.model.clear()
        self.model.append(str(result))
        self.view.update()

    # Define a method to clear the model's expression and update the view
    def clear(self):
        self.model.clear()
        self.view.update()

# Create a root window
root = tk.Tk()
root.title("Calculator")

# Create a model object
model = CalculatorModel()

# Create a view object with the root window and the model object
view = CalculatorView(root, model)

# Create a controller object with the model object and the view object
controller = CalculatorController(model, view)

# Start the main loop of the root 
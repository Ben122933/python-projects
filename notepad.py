# Import necessary tkinter modules
import tkinter as tk
from tkinter import filedialog  # For file dialogs (open/save)
from tkinter import Tk, Text, Frame, Button  # GUI widgets

# Define the main application class
class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Benjamin's notepad")  # Set window title

        # Track the current file path (used for Save)
        self.current_file: str = ''

        # Create the text area where the user writes notes
        self.text_area: Text = Text(self.root, wrap='word')  # Wrap text at word boundaries
        self.text_area.pack(expand=True, fill='both')  # Make the text area fill the window

        # Create a frame to hold the buttons at the bottom
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Save button - saves to the current file path
        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Save As button - lets the user pick a new file to save as
        self.save_as_button: Button = Button(self.button_frame, text='Save As', command=self.save_as_file)
        self.save_as_button.pack(side=tk.LEFT)

        # Load button - lets the user choose a file to open
        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)

    # Save to an existing file, or ask for one if none yet
    def save_file(self) -> None:
        if self.current_file:  # If we've opened or saved a file already
            with open(self.current_file, 'w') as file:
                # Write the current text to the file
                file.write(self.text_area.get(1.0, tk.END))
            print(f'File saved')
        else:
            # No file yet, use Save As instead
            self.save_as_file()

    # Ask the user where to save the file (Save As)
    def save_as_file(self) -> None:
        # Show the save dialog box and get the file path
        file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                      filetypes=[('Text Files', '*.txt')])
        if file_path:  # If user didn't cancel
            with open(file_path, 'w') as file:
                # Write the content of the text area to the file
                file.write(self.text_area.get(1.0, tk.END))
            # Remember this file path for future saves
            self.current_file = file_path
            print(f'File saved to: {file_path}')

    # Load a text file into the editor
    def load_file(self) -> None:
        # Show the open file dialog and get the file path
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                    filetypes=[('Text Files', '*.txt')])
        if file_path:  # If user didn't cancel
            with open(file_path, 'r') as file:
                # Read the file content
                content: str = file.read()
                # Clear the current text area
                self.text_area.delete(1.0, tk.END)
                # Insert the loaded content
                self.text_area.insert(tk.END, content)

            # Remember this file for future saves
            self.current_file = file_path
            print(f'File loaded from: {file_path}')

    # Run the application (starts the GUI loop)
    def run(self) -> None:
        self.root.mainloop()

# Entry point of the program
def main() -> None:
    root: Tk = tk.Tk()  # Create the main window
    app: SimpleNotepad = SimpleNotepad(root=root)  # Create the notepad app
    app.run()  # Run the app

# Only run the app if this script is run directly
if __name__ == '__main__':
    main()

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class MyWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")

        self.start_button = ttk.Button(root, text="Start", command=self.start_writing)
        self.start_button.pack(pady=10)

        self.end_button = ttk.Button(root, text="Spara & Avsluta", command=self.save_and_exit)
        self.end_button.pack(pady=10)
        self.end_button.config(state="disabled")

        # Textfält för att skriva
        self.text_box = tk.Text(root, height=20, width=60, state="disabled")
        self.text_box.pack(padx=10, pady=10)

        self.timer = None
        self.time_limit = 5

    def start_writing(self):
        """Aktiverar textfältet och startar timern."""
        self.text_box.config(state="normal")
        self.text_box.bind("<Key>", self.reset_timer)
        self.start_timer()

        self.start_button.pack_forget()
        self.end_button.config(state="normal")

    def start_timer(self):

        if self.timer is not None:
            self.root.after_cancel(self.timer)

        self.timer = self.root.after(self.time_limit * 1000, self.clear_text)

    def reset_timer(self, event):

        self.start_timer()

    def clear_text(self):
        self.text_box.delete(1.0, tk.END)
        messagebox.showwarning("Warning", "You stopped typing! All text has been deleted.")

    def save_and_exit(self):
        text_content = self.text_box.get(1.0, tk.END).strip()
        if text_content:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(text_content)
                messagebox.showinfo("Success", "Text saved successfully!")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MyWritingApp(root)
    root.mainloop()

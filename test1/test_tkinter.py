
import time, datetime
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("")
        self.window.rowconfigure(0, minsize=400, weight=1)
        self.window.columnconfigure(1, minsize=400, weight=1)
        self.window.mainloop()

class ValidEmailsGUI(GUI):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Emails validation")

        self.window.rowconfigure(0, minsize=300, weight=1)
        self.window.columnconfigure(1, minsize=200, weight=1)

        # self.text = tk.Entry(self.window)


        self.txt = tk.Text(self.window)
        self.fr_buttons = tk.Frame(self.window, relief=tk.RAISED, bd=2)

        self.btn_open = tk.Button(self.fr_buttons, text="Open", command=self.open_file)
        self.btn_run_check = tk.Button(self.fr_buttons, text="RUN check", command=self.run_check)
        # self.btn_validation = tk.Button(self.fr_buttons, text="Run validation")
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", command=self.save_file)

        # self.txt = tk.Text(self.window)
        start_txt = """1. Необходимо сохранить лист c email адресами в формат csv c разделителем \n
2. Выбрать этот файл на компьютере, нажав кнопку "Open" \n
3. Установить номер колонки с email адресами в поле Insert number column \"Email\"\n
4. Нажать кнопку "RUN check" для запуска проверки \n
5. Сохранить результат, нажав на кнопку \"Save as...\"
                    """
        self.txt.insert('0.0', start_txt)

        # self.label = ttk.Label()
        self.field_num_col = tk.Entry(self.fr_buttons)

        self.comment_column_number = ttk.Label(self.fr_buttons, text="Insert number column \"Email\"")
        self.run_time = ttk.Entry(self.fr_buttons)

        self.btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.comment_column_number.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.field_num_col.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.btn_run_check.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.run_time.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(row=3, column=0, sticky="ew", padx=5)

        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.txt.grid(row=0, column=1, sticky="nsew")

        self.window.mainloop()


    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[
                    ("Text Files", "*.csv"),
                    ("All Files", "*.*")
                    ]
        )
        if not filepath:
            return

        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.txt.delete('0.0', tk.END)
            self.txt.insert(tk.END, text)

        return filepath


    def run_check(self):
        time_ = datetime.datetime.now()
        self.run_time.insert(0, datetime.datetime.now() - time_)

    def save_file(self):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension=".csv",
            filetypes=[
                        ("Text Files", "*.csv"),
                        # ("All Files", "*.*")
                    ],
        )


if __name__ == "__main__":
    gui = ValidEmailsGUI()
    # gui.start()
    # window.mainloop()

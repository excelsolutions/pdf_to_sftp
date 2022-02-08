# Version 2022-01-27 Work
from PyPDF2 import PdfFileReader
from tkinter import messagebox as mbox
import tkinter as tk  # wg sposobu: https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
import tkinter.ttk as ttk
import json
import get_txt_from_pdf as pdf

# sposób na nowe okno / formę:
# https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    # TOP
        self.frame_Top_Main = tk.Frame(root)
        self.frame_Top_Main.pack(fill='x')
        self.lbl_Title = tk.Label(self.frame_Top_Main, text="PDF to SFTP", bg='yellow')
        self.lbl_Title.pack(side='top', anchor="w")

        self.lbl_Test = tk.Label(self.frame_Top_Main, text="PDF to SFTP", bg='white')
        self.lbl_Test.pack(side='top', anchor="w")

        self.button1 = tk.Button(root, text='New Window', width=25, command=self.new_window)
        self.button1.pack()

        btn_Close = tk.Button(parent, text='Close app')
        btn_Close.pack()
        # <create the rest of your GUI here>
        btn_Close.bind("<Button-1>", MainApplication.close)

        # Program
        path = 'pdf/united_states.PDF'
        pdf_text = ''
        char_start = 0
        char_to_find = 'Shipping number'
        pdf_text = pdf.text_extractor(path, 0)
        print(pdf_text)
        # char_start = pdf.find_text(self, pdf_text, char_to_find)

        pos_start = pdf.find_text_last_position(char_to_find, pdf_text) + 1
        pos_end = pos_start + 15
        self.lbl_Test.config(text="-" + pdf.take_text_from_to(pdf_text, pos_start, pos_end) + "-")


    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = form_Settings(self.newWindow)


    def close(self):
        print('Closing program')
        root.destroy()
        # self.parent.destroy()


class form_Settings:
    def __init__(self, master):
        self.master = master
        # Preparing
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill='x', pady=30)

        self.frame_path = tk.Frame(self.notebook, width=400, height=380)
        self.frame_basic = tk.Frame(self.notebook, width=400, height=380)
        self.frame_path.pack(fill='both', expand=True)
        self.frame_basic.pack(fill='both', expand=True)
        self.notebook.add(self.frame_path, text='Path')
        self.notebook.add(self.frame_basic, text='Basic operations')

        # Basic operations

        self.frame_preview = ttk.LabelFrame(self.frame_basic, text="Preview", width=200, height=200)
        self.frame_preview.pack(fill='x', anchor="nw")
        self.frame_basic_settings= ttk.LabelFrame(self.frame_basic, text="Setttings", width=200, height=200)
        self.frame_basic_settings.pack(fill=tk.BOTH)



        self.lbl_preview = tk.Label(self.frame_preview, text="Test", justify='left')
        self.lbl_preview.pack(fill='x', anchor="nw")
        self.lbl_char_start = tk.Label(self.frame_basic_settings, text="Start char")
        self.lbl_char_start.grid(row=0, column=0)
        self.txt_char_start = tk.Entry(self.frame_basic_settings, text="")
        self.txt_char_start.grid(row=0, column=1)

        path = 'pdf/united_states.PDF'
        pdf_content = pdf.load_content_pdf(self, path)
        self.lbl_preview.config(text=pdf_content)
        # TESTING CODE  --->
        file_txt = open('PDF_TEXT', 'w+', encoding='utf8')
        file_txt.writelines(pdf_content)
        file_txt.close()
        str_to_find = "Shipping number"
        find_char_pos = pdf_content.find(str_to_find)
        start_char = find_char_pos + len(str_to_find)
        end_char = start_char + 16
        print("Znaleziono: ", pdf_content[start_char:end_char])
        # TESTING CODE <----
    def save_settings(self):
        config = {"key1": "value1", "key2": "value2"}
        with open('.json', 'w') as f:
            json.dump(config, f)

    def close_windows(self):
        self.master.destroy()



if __name__ == '__main__':
    root = tk.Tk()
    root.title('PDF to SFTP 0.0.1')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

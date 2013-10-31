# Simple GUI
# Demonstrates creating a window

from tkinter import *

class Application(Frame):
    """ GUI application for Delte Line Programm. """ 
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create label for path      
        self.pathin_lbl = Label(self, text = "Input File: ")
        self.pathin_lbl.grid(row = 1, column = 0, sticky = W)

        # create entry widget for path
        self.pathin_ent = Entry(self, width = 100)
        self.pathin_ent.grid(row = 1, column = 1, sticky = W)

        # create label for path      
        self.pathout_lbl = Label(self, text = "Output File: ")
        self.pathout_lbl.grid(row = 2, column = 0, sticky = W)

         # create entry widget for path
        self.pathout_ent = Entry(self, width = 100)
        self.pathout_ent.grid(row = 2, column = 1, sticky = W)

        
        self.run_bttn = Button(self, text = "RUN", command = self.delete)
        self.run_bttn.grid(row = 3, column = 1, sticky = W)

        # create text widget to display message
        self.antwort_txt = Text(self, width = 24, height = 1, wrap = WORD)
        self.antwort_txt.grid(row = 4, column = 0, columnspan = 2, sticky = W)

    def delete(self):
        pathin = self.pathin_ent.get()
        pathout = self.pathout_ent.get()
        
        orig_file = open (pathin, "r")
        lines = orig_file.readlines()



        import fnmatch
        def find(seq, pattern):
            pattern = pattern.lower()
            for i, n in enumerate(seq):
                if fnmatch.fnmatch(n.lower(), pattern):
                    return i
                    return -1

        def index(seq, pattern):
            result = find(seq, pattern)
            if result == -1:
                raise ValueError
            return result
        def contains(seq, pattern):
            return find(seq, pattern) != -1


        try:
            for item in lines:
                begin_d_line = index(lines, "*PLD*")
                end_d_line = begin_d_line + 4
                begin_s_line = index(lines, "*SWD*")
                end_s_line = begin_s_line + 4
                del lines[begin_s_line:end_s_line]
                del lines[begin_d_line:end_d_line]

        except:
            new_text_file = open (pathout, "w")
            new_text_file.writelines(lines)
            new_text_file.close()

            message = "New file is created."
            self.antwort_txt.delete(0.0, END)
            self.antwort_txt.insert(0.0, message)
           


# main
root = Tk()
root.title("Delete Dead Trees")
root.geometry("700x90")

app = Application(root)

root.mainloop()

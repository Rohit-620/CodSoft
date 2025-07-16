import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

# 🎨––– PALETTE –––#
PRIMARY   = "#6C63FF"   # indigo
ACCENT    = "#F9A826"   # orange
BG        = "#ECEFF1"   # light-grey
TEXT      = "#212121"   # near-black
COMPLETE  = "#2E7D32"   # green
DATA_FILE = "tasks.json"

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("480x600")
        self.minsize(380, 450)
        self.configure(bg=BG)

        self.tasks: list[dict] = []           # [{text:str, done:bool}, …]
        self._build_ui()
        self._load()

    # UI––––––––––––––––––––––––––––––––––––
    def _build_ui(self):
        tk.Label(self, text="My Tasks", bg=PRIMARY, fg="white",
                 font=("Helvetica", 20, "bold"), pady=10
                 ).pack(fill=tk.X)

        list_frame = tk.Frame(self, bg=BG)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(15, 5))

        self.box = tk.Listbox(list_frame, font=("Helvetica", 12),
                              bg="white", fg=TEXT, highlightthickness=0,
                              activestyle="none")
        sb = tk.Scrollbar(list_frame, command=self.box.yview)
        self.box.config(yscrollcommand=sb.set)

        self.box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        # entry row
        entry_row = tk.Frame(self, bg=BG); entry_row.pack(fill=tk.X, padx=20)
        self.new = tk.StringVar()
        tk.Entry(entry_row, textvariable=self.new,
                 font=("Helvetica", 12)
                 ).pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(entry_row, text="Add", bg=ACCENT, fg="black",
                  font=("Helvetica", 11, "bold"), command=self.add
                  ).pack(side=tk.LEFT, padx=6)
        entry_row.bind_all("<Return>", lambda *_: self.add())

        # action buttons
        btn = lambda txt, cmd, c: tk.Button(btn_row, text=txt,
                                            command=cmd, bg=c, fg="white")
        btn_row = tk.Frame(self, bg=BG); btn_row.pack(fill=tk.X, padx=20, pady=10)
        btn("Edit",      self.edit,      "#FF7043").pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        btn("Complete",  self.done,      "#26A69A").pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        btn("Delete",    self.delete,    "#EF5350").pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        btn("Clear All", self.clear_all, "#B0BEC5").pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        # menu
        m = tk.Menu(self)
        file_m = tk.Menu(m, tearoff=0)
        file_m.add_command(label="Save",  command=self._save)
        file_m.add_command(label="Load",  command=self._load)
        file_m.add_separator()
        file_m.add_command(label="Export list…", command=self.export)
        file_m.add_separator()
        file_m.add_command(label="Exit",  command=self.quit)
        m.add_cascade(label="File", menu=file_m)
        self.config(menu=m)
        self.protocol("WM_DELETE_WINDOW", self.quit)

    # TASK OPS––––––––––––––––––––––––––––––
    def add(self):
        text = self.new.get().strip()
        if text:
            self.tasks.append({"text": text, "done": False})
            self.new.set("")
            self.refresh()

    def edit(self):
        i = self._sel()
        if i is not None:
            t = simpledialog.askstring("Edit Task", "Update task:", initialvalue=self.tasks[i]["text"])
            if t: self.tasks[i]["text"] = t.strip(); self.refresh()

    def done(self):
        i = self._sel()
        if i is not None:
            self.tasks[i]["done"] = not self.tasks[i]["done"]
            self.refresh()

    def delete(self):
        i = self._sel()
        if i is not None:
            self.tasks.pop(i); self.refresh()

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Delete ALL tasks?"):
            self.tasks.clear(); self.refresh()

    # DATA––––––––––––––––––––––––––––––––––
    def _load(self):
        if os.path.exists(DATA_FILE):
            try:    self.tasks = json.load(open(DATA_FILE))
            except: self.tasks = []
        self.refresh()

    def _save(self):
        try: json.dump(self.tasks, open(DATA_FILE, "w"), indent=2)
        except OSError: messagebox.showerror("Save Error", "Couldn’t save tasks.")

    def export(self):
        f = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text", "*.txt")],
                                         title="Export tasks to…")
        if f:
            with open(f, "w", encoding="utf-8") as out:
                for t in self.tasks:
                    mark = "[✓] " if t["done"] else "[ ] "
                    out.write(f"{mark}{t['text']}\n")
            messagebox.showinfo("Exported", "List saved!")

    # HELPERS–––––––––––––––––––––––––––––––
    def _sel(self):
        s = self.box.curselection()
        return s[0] if s else None

    def refresh(self):
        self.box.delete(0, tk.END)
        for t in self.tasks: self.box.insert(tk.END, t["text"])
        for i, t in enumerate(self.tasks):
            self.box.itemconfig(i, fg=COMPLETE if t["done"] else TEXT)

    def quit(self):
        self._save(); super().quit()

if __name__ == "__main__":
    TodoApp().mainloop()

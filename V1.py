import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def move_files_to_parent(parent_dir):
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            file_path = os.path.join(root, file)
            target_path = os.path.join(parent_dir, file)
            if os.path.exists(target_path):
                print(f"Warning: {target_path} already exists. Skipping.")
            else:
                shutil.move(file_path, target_path)
                print(f"Moved {file_path} to {target_path}")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        move_files_to_parent(folder_path)
        messagebox.showinfo("完成", "文件移动完成！")

def center_window(root, width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f'{width}x{height}+{x}+{y}')

# 创建主窗口
root = tk.Tk()
root.title("文件移动工具")

# 设置窗口居中
center_window(root, 300, 150)

# 创建一个按钮，用于选择文件夹
select_folder_button = tk.Button(root, text="选择文件夹", command=select_folder)
select_folder_button.pack(expand=True)

# 运行主循环
root.mainloop()
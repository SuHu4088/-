import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def move_files_to_parent(parent_dir):
    # 记录移动的文件数量和文件夹数量
    moved_files_count = 0
    subfolders_count = 0
    
    for root, dirs, files in os.walk(parent_dir):
        # 跳过父文件夹本身
        if root == parent_dir:
            continue
        
        subfolders_count += len(dirs)
        
        for file in files:
            file_path = os.path.join(root, file)
            target_path = os.path.join(parent_dir, file)
            
            print(f"正在移动文件：{file}")  # 在终端中打印正在移动的文件名称
            
            if os.path.exists(target_path):
                print(f"警告：{target_path} 已存在。跳过。")
            else:
                shutil.move(file_path, target_path)
                moved_files_count += 1
    
    print(f"移动完成，共移动了 {moved_files_count} 个文件。")  # 在终端中告知用户移动结束或完成
    
    # 扫描子文件夹并删除空白文件夹或打印非空白文件夹中的文件名
    for root, dirs, files in os.walk(parent_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # 如果文件夹为空
                print(f"删除空白文件夹：{dir_path}")
                os.rmdir(dir_path)
            else:
                print(f"非空白文件夹：{dir_path} 中的文件：")
                for file in os.listdir(dir_path):
                    print(file)

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
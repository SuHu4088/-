import os
import shutil
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def calculate_md5(file_path):
    """计算文件的MD5值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def move_files_to_parent(parent_dir):
    # 记录移动的文件数量和文件夹数量
    moved_files_count = 0
    skipped_files_count = 0
    
    for root, dirs, files in os.walk(parent_dir):
        # 跳过父文件夹本身
        if root == parent_dir:
            continue
        
        for file in files:
            file_path = os.path.join(root, file)
            target_path = os.path.join(parent_dir, file)
            
            print(f"正在移动文件：{file}")  # 在终端中打印正在移动的文件名称
            
            if os.path.exists(target_path):
                # 计算两个文件的MD5值
                file_md5 = calculate_md5(file_path)
                target_md5 = calculate_md5(target_path)
                
                print(f"文件 {file} 的MD5值：{file_md5}")
                print(f"目标文件 {target_path} 的MD5值：{target_md5}")
                
                if file_md5 == target_md5:
                    print(f"文件 {file} 与目标文件相同，跳过并删除。")
                    os.remove(file_path)
                    skipped_files_count += 1
                else:
                    print(f"文件 {file} 与目标文件不同，移动文件。")
                    shutil.move(file_path, target_path)
                    moved_files_count += 1
            else:
                shutil.move(file_path, target_path)
                moved_files_count += 1
    
    print(f"移动完成，共移动了 {moved_files_count} 个文件，跳过了 {skipped_files_count} 个文件。")
    
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
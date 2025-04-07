import tkinter as tk
from tkinter import messagebox

# 退出程序
def exit_program():
    root.destroy()

# 切换到下一个页面
def next_page():
    # 创建新窗口
    next_window = tk.Toplevel(root)
    next_window.title("下一个页面")
    next_window.geometry("400x300")

    # 添加标签显示文字
    label = tk.Label(next_window, text="这是下一个页面", font=("Arial", 16))
    label.pack(pady=20)

    # 关闭当前窗口
    root.withdraw()

# 创建主窗口
root = tk.Tk()

# 设置窗口标题
root.title("欢迎窗口")

# 设置窗口大小
root.geometry("400x300")

# 添加标签显示文字
label = tk.Label(root, text="欢迎使用 rustup-gui", font=("Arial", 16))
label.pack(pady=20)

# 添加“退出”按钮
exit_button = tk.Button(root, text="退出", command=exit_program, font=("Arial", 12))
exit_button.pack(side=tk.LEFT, padx=20, pady=10)

# 添加“继续”按钮
continue_button = tk.Button(root, text="继续", command=next_page, font=("Arial", 12))
continue_button.pack(side=tk.RIGHT, padx=20, pady=10)

# 运行主循环
root.mainloop()

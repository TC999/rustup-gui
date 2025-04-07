import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 设置窗口标题
root.title("Rustup 安装设置器")

# 设置窗口大小
root.geometry("400x300")

# 添加标签显示文字
label = tk.Label(root, text="欢迎使用 rustup-gui", font=("Arial", 16))
label.pack(pady=20)

label = tk.Label(root, text="这将辅助您安装 rust。", font=("Arial", 16))
label.pack(pady=20)

# 运行主循环
root.mainloop()

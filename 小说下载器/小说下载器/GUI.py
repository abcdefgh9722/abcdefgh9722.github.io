import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import novel


def search():
    name_list, href = novel.get_result(search_va.get())
    # 搜索结果
    tk.Label(text='搜索结果:', font=('黑体', 12)).grid(row=2, column=0)
    # 下拉框
    numberChosen = ttk.Combobox(root, textvariable=down_va)
    # 设置下拉列表的值
    numberChosen['values'] = tuple(zip(name_list, href))
    numberChosen.current(0)
    numberChosen.grid(row=2, column=1, padx=10, pady=10)


def save():
    novel_id = down_va.get().split()[-1]
    novel_name = down_va.get().split()[0]
    name, chapter_url_list = novel.get_novel_url(novel_id)
    for chapter_url in chapter_url_list:
        chapter_title, content = novel.get_novel_content(chapter_url)
        novel.save(name, chapter_title, content)
        text.insert(tk.END, '正在保存: ' + chapter_title + '\n')
        text.update()
    tk.messagebox.showinfo(title='温馨提示', message=f'{novel_name}下载完成')


root = tk.Tk()
root.title('小说下载器')
root.geometry("330x300+100+100")
# 可变变量
search_va = tk.Variable()
down_va = tk.Variable()
# 文本内容
tk.Label(root, text='小说下载器 V0.0.1', font=('黑体', 12)).grid(row=0, column=1)
tk.Label(root, text='搜索内容:', font=('黑体', 12)).grid(row=1, column=0)

# 搜索栏
search_bar = tk.Entry(root, textvariable=search_va)
search_bar.grid(row=1, column=1, padx=10, pady=10)

# 搜索按钮
tk.Button(root, text='搜索', font=('黑体', 12), command=search).grid(row=1, column=2)


# 下载按钮
tk.Button(root, text='下载', font=('黑体', 12), command=save).grid(row=2, column=2)

# 文本框
text = tk.Text(root, width=45, height=15)
text.grid(row=3, column=0, columnspan=20, padx=5, pady=5)

# 搜索结果
tk.Label(text='搜索结果:', font=('黑体', 12)).grid(row=2, column=0)
# # 下拉框
numberChosen = ttk.Combobox(root, textvariable=down_va)
# # 设置下拉列表的值
# name_list, href = novel.get_result(search_va.get())
numberChosen['values'] = (' ',)
numberChosen.current(0)
numberChosen.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
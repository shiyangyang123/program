# 导入必要的库
import tkinter as tk

# 定义棋盘大小和格子大小
BOARD_SIZE = 15
GRID_SIZE = 40

# 创建主窗口
root = tk.Tk()
root.title("五子棋")

# 创建画布
canvas = tk.Canvas(root, width=BOARD_SIZE * GRID_SIZE, height=BOARD_SIZE * GRID_SIZE)
canvas.pack()

# 绘制棋盘
for i in range(BOARD_SIZE):
    canvas.create_line(0, i * GRID_SIZE, BOARD_SIZE * GRID_SIZE, i * GRID_SIZE)
    canvas.create_line(i * GRID_SIZE, 0, i * GRID_SIZE, BOARD_SIZE * GRID_SIZE)

# 初始化棋盘状态
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# 当前玩家，1 表示黑子，2 表示白子
current_player = 1

# 落子函数
def place_piece(event):
    global current_player
    x = event.x // GRID_SIZE
    y = event.y // GRID_SIZE
    if board[y][x] == 0:
        board[y][x] = current_player
        color = "black" if current_player == 1 else "white"
        canvas.create_oval(x * GRID_SIZE + 5, y * GRID_SIZE + 5, (x + 1) * GRID_SIZE - 5, (y + 1) * GRID_SIZE - 5, fill=color)
        # 检查是否有玩家获胜
        if check_win(x, y, current_player):
            winner = "黑子" if current_player == 1 else "白子"
            tk.messagebox.showinfo("游戏结束", f"{winner}获胜！")
            root.quit()
        else:
            # 切换玩家
            current_player = 2 if current_player == 1 else 1

# 检查是否有玩家获胜
def check_win(x, y, player):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        # 正向检查
        for i in range(1, 5):
            new_x = x + i * dx
            new_y = y + i * dy
            if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE and board[new_y][new_x] == player:
                count += 1
            else:
                break
        # 反向检查
        for i in range(1, 5):
            new_x = x - i * dx
            new_y = y - i * dy
            if 0 <= new_x < BOARD_SIZE and 0 <= new_y < BOARD_SIZE and board[new_y][new_x] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

# 绑定鼠标点击事件
canvas.bind("<Button-1>", place_piece)

# 运行主循环
root.mainloop()
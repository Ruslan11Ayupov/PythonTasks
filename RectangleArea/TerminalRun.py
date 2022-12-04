from RectangleArea.Classes.RectangleArea import RectangleArea

ax1 = int(input())
ay1 = int(input())
ax2 = int(input())
ay2 = int(input())
bx1 = int(input())
by1 = int(input())
bx2 = int(input())
by2 = int(input())
area = RectangleArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2).run()
print("Ответ: ", area)
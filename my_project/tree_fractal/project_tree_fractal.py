from tkinter import *
import math

# Параметры
# angleBetween = 22  # Угол между ветками
lenFactor = 0.8  # Множитель длины вложенных веток
startLength = 100  # Начальная длина веток
minLength = 6  # Минимальная длина веток после которой рекурсия прекращается

# Подготовим окно вывода
root = Tk()
width, height = 1100, 500
c = Canvas(root, width=width, height=height)
c.pack()


def branch(point, angle, length):
    # Условие выхода из рекурсии
    if (length < minLength): return

    # Вычислим и нормализуем углы на которые направлены новые ветки
    # Нормализовать угол, значит преобразовать его к промежутку от 0 до 360 градусов
    lb_angle = normalize(angle + angleBetween)
    rb_angle = normalize(angle - angleBetween)

    x, y = point[0], point[1]
    # Получим точки в которые нужно провести линии
    lb_point = getBranchEnding(x, y, lb_angle, length)
    rb_point = getBranchEnding(x, y, rb_angle, length)

    # Узнаем насколько близко длина новых веток к минимальной
    # и в соответствии с этим зададим толщину линий
    branch_width = 10 * ((length - minLength) / (startLength - minLength))
    c.create_line(x, y, lb_point[0], lb_point[1], width=branch_width, fill='orange')
    c.create_line(x, y, rb_point[0], rb_point[1], width=branch_width, fill='orange')

    # Рекурсивно генерируем следующие ветки
    branch(lb_point, lb_angle, length * lenFactor)
    branch(rb_point, rb_angle, length * lenFactor)


# Функция, возвращающая кортеж с координатами точки конца очередной ветки
def getBranchEnding(x, y, angle, length):
    return (
        x - (math.sin(math.radians(angle)) * length),
        y - (math.cos(math.radians(angle)) * length))


def normalize(angle):
    while (angle < 0):
        angle += 360
    while (angle >= 360):
        angle -= 360
    return angle


def scaleevent(v):
    global angleBetween
    print(v)
    angleBetween = int(v)
    draw_tree()


def draw_tree():
    c.delete('all')
    return branch((x, y), 0, startLength * lenFactor)


if (__name__ == '__main__'):
    # Отрисуем ствол дерева
    root_x = width / 2
    root_y = height * 0.98
    x = root_x
    y = root_y - startLength
    c.create_line(root_x, root_y, x, y, fill='orange', width=10)

    # Запустим рекурсию, передав начальные значения
    # Для выполнения условия самоподобия первые
    # две ветки должны быть короче ствола
    # branch((x, y), 0, startLength * lenFactor)
    w = Scale(root, from_=1, to=90, resolution=1, orient=HORIZONTAL, command=scaleevent, length=500)
    w.pack()
    root.mainloop()
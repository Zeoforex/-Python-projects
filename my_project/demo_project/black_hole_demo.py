import tkinter as tk
from math import *
from random import randint
from tkinter.constants import CENTER

height = 700
width = 700
window = tk.Tk()
blackHoleRadius = 50

c = 30
G = 2  # ускорение свободного падения
dt = 0.1  # коэфициент ускорения
numberOfParticles = 30  # кол-во частиц
tracerColor = "green"  # цвет трассера
particlesPos = []  # все координаты точек
particles = []  # все оъекты точек
force = [c * numberOfParticles]
particleRadius = 2  # радиус частицы
blackHoleMass = 10000  # масса черной дыр
particalExits = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                 True, True, True, True, True, True, True, True, True, True, True, True,
                 True]  # попала ли частица в черную дыру


def createParticle(particleID):  # создание частицы
    # точки спауна частиц вертикально
    x = width - 50
    y = 5 + particleID * 10

    particlesPos.append([x - particleRadius, y - particleRadius, x + particleRadius,
                         y + particleRadius])  # укомплеткование массива позиций
    particles.append(canvas.create_oval(particlesPos[particleID],
                                        fill="gray"))  # укомплектование массива самих частиц, а так же их создание
    canvas.tag_lower(particles[particleID])  # двигаем частицу ближе к фону
    move(particleID, 1, 0)  # запуск рекурсии движения
    gap = canvas.create_oval(0, 0, 1, 1)  # тело для удаления в первой итерации рисования трассера
    drawTracer(particlesPos[particleID], [particlesPos[particleID][0], particlesPos[particleID][1]], particleID,
               gap)  # запуск рекусии трассера


def drawTracer(prevPoses, currentPos, particleID, currentTracer):  # отрисовка трассера
    if not particalExits[particleID]:  # если частица уже в черной дыре - трассер перестанет обновляться
        return
    if currentPos != prevPoses:  # недопущение ошибки при первом запуске
        prevPoses.append(currentPos)

    # print(prevPoses)
    canvas.delete(currentTracer)  # удаляем старый трассер
    currentTracer = canvas.create_polygon(prevPoses, outline=tracerColor)  # создаем новый трассер
    canvas.tag_lower(currentTracer)  # опускаем трассер
    canvas.tag_lower(inner)  # опускаем визуальный круг
    canvas.tag_lower(outer)  # опускаем визуальный круг
    window.after(10, drawTracer, prevPoses, [particlesPos[particleID][0], particlesPos[particleID][1]], particleID,
                 currentTracer)  # продолэение рекурсии


def move(particleID, speedX, speedY):  # рекурсия движения
    if (centerX + blackHoleRadius / 2 > particlesPos[particleID][0] > centerX - blackHoleRadius / 2) and (
            centerY + blackHoleRadius / 2 > particlesPos[particleID][1] > centerY - blackHoleRadius / 2):
        canvas.delete(particles[particleID])  # если частица попадает в черную дыру - она удалеяется
        particalExits[particleID] = False
    deltaV = c  # время замедляет скорость относительно себя
    deltaV *= dt  # коэфециент замедления времени
    # force[particleID] -= 0
    r = sqrt((particlesPos[particleID][0] - particleRadius + centerX) ** 2 + ((particlesPos[particleID][
                                                                                   1] - particleRadius + centerY) ** 2))  # дистация от частицы до центра черной дыры
    fg = (G * blackHoleMass) / (r * r)  # сила притяжения к черной дыре
    # printn(fg, G, blackHoleMass, r)
    speedX = 4 - (speedY + 3.5)  # скорость частицы по х
    speedY = ((-sin(speedX) / cos(speedX)) - 80) * fg  # скорость частицы по у
    # print(speedX, speedY)
    canvas.coords(particles[particleID], particlesPos[particleID][0] - speedX, particlesPos[particleID][1] - speedY,
                  particlesPos[particleID][2] - speedX, particlesPos[particleID][3] - speedY)  # двигаем объект частицы
    particlesPos[particleID] = [particlesPos[particleID][0] - speedX, particlesPos[particleID][1] - speedY,
                                particlesPos[particleID][2] - speedX,
                                particlesPos[particleID][3] - speedY]  # двигаем хранимые координаты частицы
    window.after(10, move, particleID, speedX, speedY)  # продолжение рекурсии


window.geometry("{}x{}".format(height, width))  # создание окна
canvas = tk.Canvas(window, height=height, width=width)  # создание холста
canvas.pack()  # упаковка холста
centerY = height // 2  # центр черной дыры
centerX = width // 2  # центр черной дыры
# сама черная дыра
canvas.create_oval(centerX - blackHoleRadius, centerY - blackHoleRadius, centerX + blackHoleRadius,
                   centerY + blackHoleRadius, fill="black")

# круги орбит, при пересечении которых частица, уже не может вернуться и/или достигает стабильной орбиты
inner = canvas.create_oval(centerX - 100, centerY - 100, centerX + 100, centerY + 100, outline="#fdeaa8", width=30)
outer = canvas.create_oval(centerX - 200, centerY - 200, centerX + 200, centerY + 200, outline="gray", width=60)

# запуск всех функций
for i in range(numberOfParticles):
    createParticle(i)

# основной цикл отрисовки программы
window.mainloop()
import math
import random

from prettytable import PrettyTable


def read() -> list[list[float]]:
    size_sle = int(input("Введите размерность СЛАУ: "))
    sle = []

    print("Введите матрицу ->")

    for row in range(size_sle):
        print(f"{row + 1}:", end=" ")
        sle.append([float(a) for a in input().split()])

    return sle


def read_from_file():
    filename = input("Введите имя файла: ")
    data = []
    try:
        file = open(filename, 'r')
        size = int(file.readline().strip())
        data = file.readlines()
    except FileNotFoundError:
        print("Ошибка! Нет такого файла")
        return

    matrix = []
    for i in range(size):
        matrix.append([float(a) for a in data[i].split()])
    print("Матрица успешно считана!")

    return matrix


def make_square(sle) -> list[list[float]]:
    tmp = []
    for i in range(len(sle)):
        tmp.append(sle[i][:len(sle)])
    return tmp


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def check_predominance(matrix: list[list[float]], isGenerated = False):
    size = len(matrix)
    all_indexes = set()
    sort_matrix = []
    for i in range(size):
        all_indexes.add(matrix[i].index(max(matrix[i][:len(matrix[i]) - 1])))
        sort_matrix.append([i, matrix[i].index(max(matrix[i][:len(matrix[i]) - 1]))])

    if size == len(all_indexes):
        sort_matrix = sorted(sort_matrix, key=lambda x: x[-1], reverse=False)
    elif isGenerated:
        return
    else:
        print("Не выполняется условие диагонального преобладания")
        return

    tmp = []
    for i in range(size):
        tmp.append(matrix[sort_matrix[i][0]])

    return tmp


def generate_matrix():
    n = int(input("Введите размер матрицы: "))
    th = []
    for i in range(n):
        th.append("x_" + str(i + 1))

    th.append("result")
    table = PrettyTable(th)
    matrix = []

    for i in range(n):
        row = []
        for j in range(n + 1):
            generate_number = round(random.random() * 10, 4)
            row.append(generate_number)
        matrix.append(row)

    sle = check_predominance(matrix, True)
    if sle is None:
        for i in range(n):
            matrix[i][i] = max(matrix[i]) + 1

    for i in range(n):
        td = []
        for j in range(n + 1):
            td.append(str(matrix[i][j]))
        table.add_row(td)
    print(table)
    return matrix

# variant 1: Root = 1; height = 5, left_leaf = root*2, right_leaf = root+3
from typing import Callable

def gen_bin_tree_nonrecursive(
    height: int = 5,
    root: int = 1,
    left_branch: Callable[[int], int] = lambda x: x * 2,
    right_branch: Callable[[int], int] = lambda y: y + 3
) -> dict[str, list]:
    """
    Генерирует бинарное дерево итеративным способом (без рекурсии).

    В каждом узле создаются два потомка — левый и правый —
    значения которых вычисляются при помощи переданных функций `left_branch` и `right_branch`.
    Алгоритм использует очередь для обхода дерева в ширину (BFS), добавляя новые узлы
    до достижения заданной высоты.

    Параметры:
        height (int): Высота дерева (количество уровней, включая корень).
                      Если height <= 0, возвращается дерево только с корневым узлом.
        root (int): Значение корневого узла.
        left_branch (Callable[[int], int]): Функция, вычисляющая значение левого потомка.
        right_branch (Callable[[int], int]): Функция, вычисляющая значение правого потомка.

    Возвращает:
        dict[str, list]: Словарь, представляющий бинарное дерево."""
    if height <= 0:
        return {str(root): []}

    tree = {str(root): []}
    queue = [(root, tree[str(root)], height)]

    while len(queue)>0:
        current_val, current_list, current_height = queue.pop(0)


        if current_height > 0:
            # Добавить слева
            left = left_branch(current_val)
            left_node = {str(left): []}
            current_list.append(left_node)
            queue.append((left, left_node[str(left)], current_height - 1))

            # Добавить справа
            right = right_branch(current_val)
            right_node = {str(right): []}
            current_list.append(right_node)
            queue.append((right, right_node[str(right)], current_height - 1))

    return tree
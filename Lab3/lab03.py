# вариант1: Root = 1; height = 5, left_leaf = root*2, right_leaf = root+3
def gen_bin_tree(height: int = 5,
                 root: int = 1,
                 left_branch=lambda x: x * 2,
                 right_branch=lambda y: y + 3) -> list[int]:
    """
        Генерирует бинарное дерево в виде вложенных списков.

        Аргументы:
        - height: высота дерева
        - root: значение корня
        - left_branch: функция для вычисления значения левого потомка
        - right_branch: функция для вычисления значения правого потомка

        Возвращает:
        - Вложенный список [root, left, right]
        """
    if height <= 0:
        return [root]
    left = gen_bin_tree(height - 1, left_branch(root), left_branch, right_branch)
    right = gen_bin_tree(height - 1, right_branch(root), left_branch, right_branch)
    return [root, left, right]


# print tree по варианту
tree = gen_bin_tree()
print(tree)

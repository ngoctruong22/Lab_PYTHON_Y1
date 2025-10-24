from typing import Callable


def gen_bin_tree_recursive(height: int = 5,
                           root: int = 1,
                           left_branch=lambda x: x * 2,
                           right_branch=lambda y: y + 3) -> dict[str, list]:
    """дерево строится путём рекурсивных вызовов для левого и правого поддерева
    """
    if height <= 0:
        return {str(root): []}
    left = gen_bin_tree_recursive(height - 1, left_branch(root), left_branch, right_branch)
    right = gen_bin_tree_recursive(height - 1, right_branch(root), left_branch, right_branch)
    return {str(root): [left, right]}


def gen_bin_tree_nonrecursive(
        height: int = 5,
        root: int = 1,
        left_branch: Callable[[int], int] = lambda x: x * 2,
        right_branch: Callable[[int], int] = lambda y: y + 3) -> dict[str, list]:
    """ дерево строится путём нерекурсивных
    """

    if height <= 0:
        return {str(root): []}

    tree = {str(root): []}
    queue = [(root, tree[str(root)], height)]

    while len(queue) > 0:
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

from src.app import bfs
def test_shortest_path():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (2, 2))
    assert path is not None


def test_start_equals_goal():
    grid = [
        [0, 0],
        [0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (0, 0))
    assert path == [(0, 0)]


def test_no_path():
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (2, 2))
    assert path is None


def test_avoids_obstacle():
    grid = [
        [0, 1],
        [0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (1, 1))
    assert path == [(0, 0), (1, 0), (1, 1)]


def test_path_starts_at_start():
    grid = [
        [0, 0],
        [0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (1, 1))
    assert path[0] == (0, 0)


def test_path_ends_at_goal():
    grid = [
        [0, 0],
        [0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (1, 1))
    assert path[-1] == (1, 1)


def test_path_avoids_obstacle():
    grid = [
        [0, 1],
        [0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (1, 1))
    assert all(grid[r][c] == 0 for r, c in path)


def test_nodes_expanded():
    grid = [
        [0, 0],
        [0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (1, 1))
    assert nodes > 0


def test_single_cell():
    grid = [[0]]
    path, nodes = bfs(grid, (0, 0), (0, 0))
    assert path == [(0, 0)]


def test_longer_path():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    path, nodes = bfs(grid, (0, 0), (2, 2))
    assert len(path) - 1 == 4
import numpy as np
from scipy.spatial import Delaunay
from PIL import Image, ImageFilter
import cv2
CONDITIONS = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]


def split_triangle(positions):
    assert positions.shape == (3, 2)
    positions = sorted(positions.tolist(), key=lambda x: x[::-1])
    flat = False
    for a, b, c in CONDITIONS:
        if positions[a][1] == positions[b][1]:
            base_x1, base_x2 = positions[a][0], positions[b][0]
            if base_x1 > base_x2:
                base_x1, base_x2 = base_x2, base_x1
            base_y = positions[a][1]
            tip = positions[c]
            flat = True
            break

    if flat:
        return {'triangle': [(base_x1, base_y), (base_x2, base_y), tip], 'flat': True}

    else:
        low, mid, high = positions
        mid_x, mid_y = mid
        low_x, low_y = low
        high_x, high_y = high
        dx, dy = high_x - low_x, high_y - low_y
        dy1 = mid_y - low_y
        fourth = (low_x + dx * dy1 / dy, mid_y)
        if mid_x > fourth[0]:
            mid, fourth = fourth, mid

        return {'triangles': [[mid, fourth, low], [mid, fourth, high]], 'flat': False}


def scan_triangle(positions):
    left_x, right_x = positions[0][0], positions[1][0]
    base_y = positions[0][1]
    tip_x, tip_y = positions[2]
    h = tip_y - base_y
    dx1 = tip_x - left_x
    dx2 = tip_x - right_x
    step = 1
    if tip_y < base_y:
        step = -1

    points = []

    for y in range(round(base_y), round(tip_y+step), step):
        ry = round(y)
        min_x = round(left_x + dx1 * (y - base_y) / h)
        max_x = round(right_x + dx2 * (y - base_y) / h)
        points.extend([(x, ry) for x in range(min_x, max_x+1)])

    return points


def rasterize_triangle(positions):
    data = split_triangle(positions)
    if data['flat']:
        return scan_triangle(data['triangle'])
    else:
        return scan_triangle(data['triangles'][0]) + scan_triangle(data['triangles'][1])


def sample(w, h, n=8192):
    points = np.zeros((n, 2))
    x = np.random.randint(0, w, n)
    y = np.random.randint(0, h, n)
    points[:, 0] = x
    points[:, 1] = y
    return points


def triangulate_image(path, detail, grey=False):
    assert 0 < detail <= 1
    image = np.array(Image.open(path))

    def triangle_color(x, y):
        return np.mean(image[y, x], axis=0)

    h, w = image.shape[:2]
    num_tiles = w * h / 64
    n = round(num_tiles * detail)
    samples = sample(w, h, n)
    corners = np.array([(0, 0), (0, h - 1), (w - 1, 0), (w - 1, h - 1)])
    points = np.concatenate((corners, samples))
    triangles = points[Delaunay(points).simplices]
    art = np.zeros((h, w, 3), dtype=np.uint8)
    for triangle in triangles:
        x, y = zip(*rasterize_triangle(triangle))
        art[y, x] = triangle_color(x, y)

    art = Image.fromarray(art)
    art = art.filter(ImageFilter.MedianFilter(
        3)).filter(ImageFilter.GaussianBlur(1))
    if grey:
        art = art.convert('L')
    art.show()
    return art


triangulate_image("1.png", 0.5, False)
from pathlib import Path
from problem_18 import load, find_max_path

if __name__ == '__main__':
    txt = Path('p067_triangle.txt').read_text()
    print(find_max_path(load(txt)))

from concurrent.futures import ProcessPoolExecutor
import json
from pathlib import Path
from concurrent.futures import as_completed


def main():
    root_dir = Path(__file__).parent.parent
    try:
        with open(f"{root_dir}/Data/inputs.json") as f:
            _inputs = json.load(f)
    except Exception as e:
        raise e

    with ProcessPoolExecutor(max_workers=len(_inputs)) as executor:
        futures = [executor.submit(run, ip) for ip in _inputs]
        for future in as_completed(futures):
            print(future.result())


def run(ip):
    # your code here
    pass


if __name__ == '__main__':
    main()



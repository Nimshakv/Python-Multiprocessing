from concurrent.futures import ProcessPoolExecutor
import json
from pathlib import Path
from concurrent.futures import as_completed


def main():
    root_dir = Path(__file__).parent
    print(f"{root_dir}/inputs.json")
    try:
        with open(f"{root_dir}/inputs.json") as f:
            _inputs = json.load(f)
    except Exception as e:
        raise e

    with ProcessPoolExecutor(max_workers=len(_inputs)) as executor:
        futures = [executor.submit(run, ip) for ip in _inputs]
        for future in as_completed(futures):
            pass


def run(ip):
    # your code here
    print(ip)
    pass


if __name__ == '__main__':
    main()



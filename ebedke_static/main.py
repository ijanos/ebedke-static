#!/usr/bin/env python3

import argparse
import json
from typing import List, Dict

from jinja2 import Environment, FileSystemLoader, StrictUndefined


def load_restaurants(json_path: str) -> List[Dict[str, object]]:
    with open(json_path) as f:
        ebedke_data = json.load(f)
    return ebedke_data


def generate_site(restaruants: List[Dict[str, object]], output_dir: str) -> None:
    with open('template/index.html.j2') as f:
        template_str = f.read()

    jinja_env = Environment(loader=FileSystemLoader("template/"), undefined=StrictUndefined)
    template = jinja_env.from_string(template_str)
    with open(f"{output_dir}/index.html", "w") as f:
        f.write(template.render(restaurants=restaruants)
)



def parse_args():
    parser = argparse.ArgumentParser(description='Ebedke static site generator')
    parser.add_argument('restaurants', help='a JSON file with restaurant data')
    parser.add_argument('--build_dir', default="build", help='output directory, default: build')

    return parser.parse_args()

def main() -> None:
    args = parse_args()
    restaurants = load_restaurants(args.restaurants)
    generate_site(restaurants, args.build_dir)

if __name__ == "__main__":
    main()

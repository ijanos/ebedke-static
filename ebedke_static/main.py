#!/usr/bin/env python3

import argparse
import json
from typing import List, Dict
import jinja2

def load_restaurants(json_path) -> List[Dict[str, object]]:
    with open(json_path) as f:
        ebedke_data = json.load(f)
    return ebedke_data


def generate_site(restaruants, output_dir) -> None:
    with open('template/index.html.j2') as f:
        template = jinja2.Template(f.read(), undefined=jinja2.StrictUndefined)
    with open(f"{output_dir}/index.html", "w") as f:
        f.write(template.render(restaurants=restaruants))


def main() -> None:
    parser = argparse.ArgumentParser(description='Ebedke static site generator')
    parser.add_argument('restaurants', help='a JSON file with restaurant data')
    parser.add_argument('--build_dir', default="build", help='output directory, default: build')

    args = parser.parse_args()

    restaurants = load_restaurants(args.restaurants)
    generate_site(restaurants, args.build_dir)

if __name__ == "__main__":
    main()

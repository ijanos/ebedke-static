#!/usr/bin/env python3

import argparse
import json
from typing import List, Dict, Any
from collections import defaultdict

from jinja2 import Environment, FileSystemLoader, StrictUndefined, Template


def load_restaurants(json_path: str) -> List[Dict[str, object]]:
    with open(json_path) as f:
        ebedke_data = json.load(f)
    return ebedke_data


def load_template(template_path: str) -> Template:
    with open(template_path) as f:
        template_str = f.read()

    jinja_env = Environment(loader=FileSystemLoader("template/"), undefined=StrictUndefined)
    return jinja_env.from_string(template_str)


def generate_page(target, template, keys={}):
    with open(target, "w") as f:
        f.write(template.render(keys))


def generate_site(restaruants: List[Dict[str, Any]], output_dir: str) -> None:
    generate_page(f"{output_dir}/404.html", load_template('template/404.html.j2'))

    groups: Dict[str, List[Any]] = defaultdict(list)
    for r in restaruants:
        groups["index"].append(r)
        for g in r["groups"]:
            groups[g].append(r)

    template_main = load_template('template/index.html.j2')
    for group, restaruants in groups.items():
        generate_page(f"{output_dir}/{group}.html", template_main, {"restaurants": restaruants})


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

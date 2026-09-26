import yaml

def load_dynamic_sitemaps(path="dynamic-sitemaps.yaml"):
    with open(path) as sitemaps_file:
        return yaml.load(sitemaps_file.read(), Loader=yaml.FullLoader)

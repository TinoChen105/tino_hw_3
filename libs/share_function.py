from requests_toolbelt.utils import dump


def print_raw_http(response):
    data = dump.dump_all(response)
    return "\n" * 2 + data.decode("utf-8")

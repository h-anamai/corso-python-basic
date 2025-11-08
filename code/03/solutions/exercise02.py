def join_url():
    url_parts = ["https:", "", "www.python.org", "doc"]
    final_url = "//".join(url_parts[:2]) + "/".join(url_parts[2:])

    print(final_url)

if __name__ == "__main__":
    join_url()
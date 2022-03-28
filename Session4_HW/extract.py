def extract_info(wt_list):
    result = {
        'title': [],
        'author': [],
        'rating': [],
        'length': 0
    }

    for wt in wt_list:
        result["title"].append(wt.find("dt").find("a").text)
        result["author"].append(wt.find("dd", {"class":"desc"}).find("a").text)
        result["rating"].append(wt.find("div", {"class":"rating_type"}).find("strong").text)
        result["length"] += 1

    return result
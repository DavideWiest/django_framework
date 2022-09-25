

std_title_clause = " - Davide Wiest"

def build_params(title, params):
    bparams = {
        "title": title + std_title_clause,
        "base_url": "http://127.0.0.1:8000/" # "https://davidewiest.com"
    }

    return {**bparams, **params}

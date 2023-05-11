import requests
import json
from colorama import Fore, Back, Style

def perform_dorking(query):
    # Set up the search engines
    search_engines = [
        {
            "name": "Google",
            "url": "https://www.google.com/search",
            "params": {"q": query}
        },
        {
            "name": "DuckDuckGo",
            "url": "https://duckduckgo.com/html/",
            "params": {"q": query}
        },
        {
            "name": "Bing",
            "url": "https://www.bing.com/search",
            "params": {"q": query}
        },
        {
            "name": "Dogpile",
            "url": "http://www.dogpile.com/search/web",
            "params": {"q": query}
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/scholar",
            "params": {"q": query}
        },
        {
            "name": "Webopedia",
            "url": "https://www.webopedia.com/search/",
            "params": {"query": query}
        },
        {
            "name": "Yahoo",
            "url": "https://search.yahoo.com/search",
            "params": {"p": query}
        },
        {
            "name": "Internet Archive",
            "url": "https://archive.org/search.php",
            "params": {"query": query}
        },
        {
            "name": "Baidu",
            "url": "https://www.baidu.com/s",
            "params": {"wd": query}
        },
        {
            "name": "Ask",
            "url": "https://www.ask.com/web",
            "params": {"q": query}
        },
        {
            "name": "AOL",
            "url": "https://search.aol.com/aol/search",
            "params": {"q": query}
        },
        {
            "name": "Yandex",
            "url": "https://www.yandex.com/search/",
            "params": {"text": query}
        },
        {
            "name": "Excite",
            "url": "https://www.excite.com/search",
            "params": {"q": query}
        },
    ]
    
    search_results = {}
    
    for engine in search_engines:
        name = engine["name"]
        url = engine["url"]
        params = engine["params"]
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            # Extract relevant information from the response
            # ... Your result extraction logic here ...
            search_results[name] = response.text
        
    # Save the results as JSON
    with open("results.json", "w") as f:
        json.dump(search_results, f, indent=4)

    print(f"{Fore.YELLOW}------------------------------------------------------------------------------------------------")
    print(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.GREEN}Dorking completed. Results saved in results.json")
    print (f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}]{Fore.WHITE}For visualize it you can use this page: {Fore.RED}https://jsonviewer.stack.hu/")


# Prompt the user to enter the query
query = input("Enter the query: ")

# Perform dorking
perform_dorking(query)
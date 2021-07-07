import requests
import json


headers = {
    "method": "GET",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
}


def parser(subreddit_name, pages, last_post=1):
    for i in range(pages):
        url = f"https://gateway.reddit.com/desktopapi/v1/subreddits/{subreddit_name}?rtj=only&redditWebClient=web2x&app=web2x-client-production&allow_over18=1&include=identity&after={last_post}"
        whole_json = requests.get(url, headers=headers).json()
        post_ids = [i for i in whole_json["posts"].keys() if len(i) < 15]
        last_post = post_ids[-1]
        data = [
            whole_json["posts"][i]["title"]
            for i in post_ids
            if whole_json["posts"][i]["title"].lower().startswith("[iwantout]")
        ]
        with open("reddit_data.txt", "a") as f:
            f.write(",\n".join(data) + "\n")
        print(f"Added {len(data)} new lines of data to reddit_data.txt")
    print("Done")


parser("IWantOut", 500)

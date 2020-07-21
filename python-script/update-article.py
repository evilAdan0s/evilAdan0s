#!/usr/bin/env python

import feedparser

def fetch_blog_entries():
    entries = feedparser.parse("https://eviladan0s.github.io/atom.xml")["entries"]
    result = [
        {
            "title": entry["title"],
            "url": entry["link"].split("#")[0],
            "published": entry["published"].split("T")[0],
        }
        for entry in entries
    ]
    return result[0:5]


def write_md(data):
	with open("../readme_old.md","r") as of:
		old_file_content = of.readlines() #list

	content = old_file_content + data #list

	with open("../README.md","w") as f:
		for i in content:
			f.write(i)

def generate_md(result):
	text = []
	for i in result:
		content = "- [{}]({}) - {}".format(i['title'],i['url'],i['published'])
		text.append(content + "\n")

	return text


if __name__ == '__main__':
	data = fetch_blog_entries()
	text = generate_md(data)
	write_md(text)






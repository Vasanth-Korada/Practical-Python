import wikipedia

print("Summary:"+wikipedia.summary("Kim Jong Un"))

print("Search Result:"+str(wikipedia.search("Kim Jong Un")))

obj = wikipedia.page("Kim Jong Un")

print("Title:"+obj.title)

print("URL:"+obj.url)

print("Content:"+obj.content)

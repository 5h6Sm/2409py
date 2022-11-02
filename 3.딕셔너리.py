d = {}
urls = {"google": "google.com", 18: "unesco.org"}

urls["x"] = 2560
print(urls)

urls["x"] = 1920
print(urls)

del urls["x"]
print(urls)
urls.pop(18)
print(urls)
urls.clear()
print(urls)

urls = {"google": "google.com", 18: "unesco.org"}
print(urls["google"])
print(urls.get("google"))
print("google" in urls)
print("google.com" in urls)
print("google.com" in urls.values())

print(len(urls))
print(urls.keys())
print(urls.values())
print(urls.items())

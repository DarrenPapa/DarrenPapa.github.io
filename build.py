import os

with open("lib_template.html") as input:
    with open("lib.html", "w") as output:
        res = []
        for i in os.listdir("libs"):
            lib, name = i.split(".", 1)
            name, _ = name.rsplit(".", 1)
            res.append(f'<a href="./libs/{i}">{lib}/{name}</a><br>')
        output.write(input.read().replace("<!--FILES-->", "\n"+"\n".join(res)+"\n"))
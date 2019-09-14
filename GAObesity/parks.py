import requests

r = requests.get("http://agr.georgia.gov/community-farmers-markets.aspx")
index = 0
while (r.text.find("<h3 align=", index) != -1):
    index = r.text.find("<h3 align=", index)
    print(r.text[(index + 19):(r.text.find("</h3>", index + 1))], end = "")
    index2 = r.text.find("<h3 align=", index + 1)
    count = 0
    while (r.text.find("<h4>", index, index2) != -1):
        count = count + 1
        index = r.text.find("<h4>", index, index2) + 1
    index = index2
    print("," + str(count))

import json
from scholarly import scholarly

# 你的 Google Scholar ID
scholar_id = "oqkhjW0AAAAJ"

# 获取 Google Scholar 用户信息
author = scholarly.search_author_id(scholar_id)
citations = author["citedby"]

# 构造 shields.io 格式 JSON
data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(citations),
    "color": "9cf"
}

# 保存到文件
with open("google-scholar-stats/gs_data_shieldsio.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"Updated citations: {citations}")
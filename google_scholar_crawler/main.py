# from scholarly import scholarly
# import jsonpickle
# import json
# from datetime import datetime
# import os

# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
# name = author['name']
# author['updated'] = str(datetime.now())
# author['publications'] = {v['author_pub_id']:v for v in author['publications']}
# print(json.dumps(author, indent=2))
# os.makedirs('results', exist_ok=True)
# with open(f'results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)

# shieldio_data = {
#   "schemaVersion": 1,
#   "label": "citations",
#   "message": f"{author['citedby']}",
# }
# with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)


# update 250802

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
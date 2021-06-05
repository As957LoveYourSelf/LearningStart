import numpy as np
import pandas as pd


# loading data
header = ["user_id", "item_id", "rating", "timestamp"]
data = pd.read_csv("u.data", sep='\t', names=header)
# 生成用户-电影评分矩阵
# 检查是否有重复的用户电影打分记录
data.duplicated(subset=["user_id", "item_id"]).sum()
item_id_user = data.groupby("item_id").count()["user_id"]
# 构建用户电影矩阵
users_num = data.user_id.max()
items_num = data.item_id.max()
users_item_rating = np.zeros((users_num, items_num))
for line in data.itertuples():        # 将DataFrame迭代成元组
    users_item_rating[line[1]-1, line[2]-1] = line[3]
np.savetxt("ratingmatrix.csv", users_item_rating, delimiter=",")

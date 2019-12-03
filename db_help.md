## 新建group表
### id int4 主键 非空 自增 设置索引 id_index B_Tree
#### 自增设置
1. 打开navcat查询列表，去创建一个序列
 ```CREATE SEQUENCE group_id_seq START 10;```
2. 在字段默认值里设 
```nextval('group_id_seq'::regclass)```

### groupname varchar

## 新建groupusers表

### id int4 自增
#### 自增设置
1. 打开navcat查询列表，去创建一个序列
 ```CREATE SEQUENCE group_user_id_seq START 10;```
2. 在字段默认值里设 
```nextval('group_user_id_seq'::regclass)```

### group_id int 外键group(id)  设置索引 group_id_index B_Tree

### user_id int 外键user(id)  设置索引 user_id_index B_Tree

### user_type bool t: 管理员 f: 普通用户
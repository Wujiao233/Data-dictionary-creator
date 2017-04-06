# Data-dictionary-creator
生成数据库（或单个表）的Markdown 格式数据字典

使用库：
- tqdm
- argparse
- pymysql

使用方法：

    python3 create_database_info.py [option]


## 效果示例

------------

### tb_actor
字段名 | 字段类型 | 默认值 | 可空 | 注解
---- | ---- | ---- | ---- | ----
ActorId | int(11) | None | NO | 主键
ActorName | varchar(45) | None | NO | 角色名称
ActorAuthority | int(11) | None | NO | 角色权限（1为客户，2为管理员）
StationId | int(11) | None | NO | 外键（标记关联的用户）
UserId | int(11) | None | NO | 外键（标记所属的取件点）

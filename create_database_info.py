import pymysql as mysql
import sys
import argparse
import tqdm

parser = argparse.ArgumentParser(description="由Mysql数据库生成数据字典")

parser.add_argument('host', help='The Host of Mysql Server')
parser.add_argument('user', help='Username of Mysql Server')
parser.add_argument('password', help='Password of Mysql Server')
parser.add_argument('database', help='The database name which you want to output')
parser.add_argument('-t', '--table', help='Tablename when only output one table', default=None)
parser.add_argument('-p', '--path', help='Output path', default='./')
parser.add_argument('-c', '--charset', help='Charset you want to use', default='utf8')

# print(parser.parse_args())

argv = parser.parse_args()

conn = mysql.connect(host=argv.host, user=argv.user, password=argv.password, database='information_schema',
                     charset=argv.charset)
cursor = conn.cursor()


def get_all_tablename(database):
    cursor.execute(
        "SELECT TABLE_NAME FROM information_schema.tables WHERE table_schema='{tablename}' AND table_type='base table'".format(
            tablename=database))
    return cursor.fetchall()


markdown_table_header = """### {table_name}
字段名 | 字段类型 | 默认值 | 可空 | 注解
---- | ---- | ---- | ---- | ----
"""
markdown_table_row = """%s | %s | %s | %s | %s
"""

if argv.table is None:
    tables = get_all_tablename(argv.database)
else:
    tables = [[argv.table]]

for table in tqdm.tqdm(tables):
    table = table[0]
    f = open(argv.path + '/' + table + '.md', 'w+', encoding='utf-8')
    # print(table)
    cursor.execute(
        "select COLUMN_NAME,COLUMN_TYPE,COLUMN_DEFAULT,IS_NULLABLE,COLUMN_COMMENT " +
        "from information_schema.COLUMNS where table_schema='{database}' and table_name='{table}'".format(
            database=argv.database, table=table))
    tmp_table = cursor.fetchall()
    # print(tmp_table)
    p = markdown_table_header.format(table_name=table)
    for col in tmp_table:
        tcol = list(col)
        tcol[4] = tcol[4].replace('\n','')
        tcol = tuple(tcol)
        p += markdown_table_row % tcol
    # print p
    f.writelines(p)
    f.close()

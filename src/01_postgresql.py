# PostgreSQLデータベースにODBCを使用して接続するサンプルコード
import pyodbc

conn_params = {
    "host": "10.146.11.69",
    "port": 5432,
    "dbname": "wine_db",
    "user": "postgres",
    "password": "postgres",
}

# ODBC接続文字列を作成
conn_str = (
    f"DRIVER={{PostgreSQL Unicode}};"
    f"SERVER={conn_params['host']};"
    f"PORT={conn_params['port']};"
    f"DATABASE={conn_params['dbname']};"
    f"UID={conn_params['user']};"
    f"PWD={conn_params['password']}"
)

try:
    # データベースに接続
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # 簡単なクエリを実行（例: テーブル一覧を取得）
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
    )
    tables = cursor.fetchall()

    print("Public schema tables:")
    for table in tables:
        print(table.table_name)

    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("Error connecting to database or executing query:", e)

import psycopg2


def reset_hourly_hit():
    conn = psycopg2.connect(
            host='ec2-44-194-113-156.compute-1amazonaws.com',
            database='d92a234ocho7h5',
            user='armqugxjzonbdg',
            password='5e47355403d4e003ccc8e89d99bbfa7dabeaad5281ca1772f89759a99c70623a',
            port='5432')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM "shortner_url";""")
    url_objs = cursor.fetchall()
    if url_objs:
        for url_obj in url_objs:
            stmt = """UPDATE "shortner_url" SET hourly_hit =%s WHERE "uuid" = %s;"""
            cursor.execute(stmt, (0, url_obj[2]))
            conn.commit()
            cursor.close()
            conn.close()


reset_hourly_hit()

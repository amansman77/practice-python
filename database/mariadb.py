import pymysql.cursors

def find_tag_name_all(cur):
    query = "SELECT DISTINCT TAG_NAME \
            FROM ejc_mold_setup_data \
            WHERE VALUE_TYPE = 'SETUP' \
            ORDER BY TAG_NAME"
    cur.execute(query, )

    tag_names = []
    
    row = cur.fetchone()
    while row is not None:
        tag_names.append(row['TAG_NAME'])
        row = cur.fetchone()
    
    return tag_names

def find_tag_value_all(cur, tag_name):
    query = "SELECT TAG_VALUE, COUNT(TAG_VALUE) AS CNT \
            FROM ejc_mold_setup_data \
            WHERE VALUE_TYPE = 'SETUP' AND TAG_NAME = '" + tag_name + "' \
            GROUP BY TAG_VALUE \
            ORDER BY CNT DESC"
    cur.execute(query, )

    tag_values = []
    
    row = cur.fetchone()
    while row is not None:
        tag_values.append(row['TAG_VALUE'])
        row = cur.fetchone()
    
    return tag_values

def add_ai_ejc_mold_setup_meta(cursor, tag_name, tag_value):
    sql = "INSERT INTO `omegaai`.`ai_ejc_mold_setup_meta` (`TAG_NAME`, `TAG_VALUE`) VALUES (%s, %s);"
    cursor.execute(sql, (tag_name, tag_value))

if __name__ == '__main__':
    connection = pymysql.connect(host="localhost",
                             port=3600,
                             user='admin',
                             password='admin',
                             database='testdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

    # Get Cursor
    with connection:
        with connection.cursor() as cursor:
            tag_names = find_tag_name_all(cursor)
        
        for tag_name in tag_names:
            if tag_name == 'TEMPERATURE':
                print('TEMPERATURE is not setup attribute. skip...')
                
            with connection.cursor() as cursor:
                tag_values = find_tag_value_all(cursor, tag_name)
                add_ai_ejc_mold_setup_meta(cursor, tag_name, ','.join(map(str, tag_values)))
            connection.commit()

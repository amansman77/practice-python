import psycopg2

def save(conn):
    # insert into z_ho_bit(id, bit_data) values(nextval('z_ho_bit_id_seq'), B'0000000001')
    sql = "INSERT INTO z_ho_bit (id, bit_data) " \
            + "values  (nextval('z_ho_bit_id_seq'), %s)"
    val = []
    for i in range(1):
        val.append(
            (b'0000000001')
        )

    cur = conn.cursor()
    cur.executemany(sql, val)
    conn.commit()
    rowcount = cur.rowcount
    cur.close()

    return rowcount

def saveOne(conn):
        cur = conn.cursor()
        query = "INSERT INTO z_ho_bit (id, bit_data) values (nextval('z_ho_bit_id_seq'), B'11111011111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')"
        # data = (psycopg2.Binary('0000000001'))
        cur.execute(query, ())
        conn.commit()
        cur.close()

        # print('Save data')

if __name__ == '__main__':
    conn = psycopg2.connect(host='192.168.7.130', dbname='platform_rms',
                            user='aiplatform', password='platformadmin', port='30432')

    # rowcount = save(conn)
    # print('Save:', rowcount)
    for i in range(1000):
        saveOne(conn)
        print("Insert count:", i)

    conn.close()
    
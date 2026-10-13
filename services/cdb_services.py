from db import get_connection


def save_chunk(document_id, text, page, filename):
    conn = get_connection()
    cursor = conn.cursor()

    sql = (
        "INSERT INTO chunks "
        "(document_id, chunk_text, page_number, filename) "
        "VALUES (%s, %s, %s, %s)"
    )

    cursor.execute(sql, (document_id, text, page, filename))

    conn.commit()

    chunk_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return chunk_id


if __name__ == "__main__":
    chunk_id = save_chunk(2, "hello", 5, "supp.pdf")
    print("Inserted chunk ID:", chunk_id)
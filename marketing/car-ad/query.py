'''
get whole table query generator
'''
def get_table(table):
    qry = (
    """
    SELECT * FROM my_db.{};
    """).format(table)
    print(qry)
    return qry
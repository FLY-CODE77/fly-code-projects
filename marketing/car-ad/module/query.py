'''
get whole table query generator
'''
def get_table(table):
    qry = (
    """
    SELECT * FROM my_db.{};
    """).format(table)
    print("your query is", qry)
    return qry
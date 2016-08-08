
def test():
  # Connect to the database.
  import pymysql
  conn = pymysql.connect(
      db='',
      user='',
      passwd='',
      host='',
      autocommit=True)

  c = conn.cursor()

  # Insert some example data.
  c.execute("INSERT INTO numbers VALUES (1, 'One!')")
  c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
  c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
  #conn.commit()

  # Print the contents of the database.
  c.execute("SHOW TABLES")
  print([(r[0]) for r in c.fetchall()])

  


class Place:

  def __init__(self, id, country, address, postcode, town, stars, opened):
    self.id = id
    self.country = country
    self.address = address
    self.postcode = postcode
    self.town = town
    self.stars = stars
    self.opened = opened

  def get_places(conn):
    
    cur = conn.cursor()
    '''cur.execute("""SELECT name,address,postcode,town,stars,hotel.id FROM hotel 
  INNER JOIN country ON hotel.country = country.id
  where open = 1;""")'''
    cur.execute("""SELECT * FROM trip_advisor ;""")

    # votre code 
    Places = [{"country":elem[0], "address":elem[1], "postcode":elem[2], "town":elem[3], "stars":elem[4],"id":elem[5]} for elem in cur.fetchall()]
    
    cur.close()

    return Places

  def get_cuisine(conn):
    cursor = conn.cursor()
    '''cur.execute("""SELECT name,address,postcode,town,stars,hotel.id FROM hotel 
  INNER JOIN country ON hotel.country = country.id
  where open = 1;""")'''
    cursor.execute("SELECT distinct Cuisine FROM trip_advisor ")
    a = []
    for elem in cursor.fetchall():
      for el in ''.join(elem).split(','):
        a.append(el.strip())
    cursor.close()
    c_n = set(a)

    cuisine=c_n
    return cuisine


class Recherche:

  def __init__(self, email, hotel_id, room_num, check_in,  check_out, num_persons):
    self.email = email
    self.hotel_id = hotel_id
    self.room_num = room_num
    self.check_in = check_in
    self.check_out = check_out
    self.num_persons = num_persons

  def find_place(conn,cu,ty,cp=75):
    
    cur = conn.cursor()
    # votre code ici
    cur.execute("SELECT Nom, Type,Téléphone,Mail,lat,lon FROM trip_advisor WHERE (instr(Code_Postal ,'{}')) AND (instr(Cuisine ,'{}')) AND (instr(Type ,'{}'))".format(cp,cu,ty))
    

    while True:
    #je recup la premiere ligne du select
      tple = cur.fetchone()
      #tout les lignes du select ont été recupéré
      if tple is None : 
        break
      # on verifie si la chmbre est disponible a la date check in demandé
      room_number = tple[0]
      if Recherche.is_room_available(conn, cp):
        return room_number
    #on a trouvé aucun chambre disponible
    return None
    


  def is_room_available (conn, cp):
    cur = conn.cursor()

    request = "SELECT * FROM trip_advisor WHERE instr(Code_Postal ,'{}') "
    cur.execute(request.format(cp))

    if cur.fetchone() is None : return False

    request = "SELECT * FROM trip_advisor WHERE instr(Code_Postal ,'{}') "
    cur.execute(request.format(cp))
    
    return cur.fetchone() 
    '''is None'''



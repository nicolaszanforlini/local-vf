class Carte:

  def __init__(self, cp,cu,ty):
    self.cp = cp
    self.cu = cu
    self.ty = ty

  def sauve(self,conn):
    cursor = conn.cursor()

    import folium
    from folium.plugins import MarkerCluster

    cursor.execute("SELECT AVG(lat) FROM trip_advisor ")
    lat_m=cursor.fetchone()[0]
    cursor.execute("SELECT AVG(lon) FROM trip_advisor ")
    lon_m=cursor.fetchone()[0]

    rest_map = folium.Map(location=[lat_m,lon_m],zoom_start=13, tiles='OpenStreetMap')
    marker_cluster = folium.plugins.MarkerCluster().add_to(rest_map)

    cursor.execute("SELECT Nom, Type,Téléphone,Mail,lat,lon FROM trip_advisor WHERE (instr(Code_Postal ,'{}')) AND (instr(Cuisine ,'{}')) AND (instr(Type ,'{}'))".format(self.cp,self.cu,self.ty))
    #cursor.execute("SELECT Nom, Type,Téléphone,Mail,lat,lon FROM trip_advisor WHERE (Code_Postal = {})".format(self.cp))
    for elem in cursor.fetchall():
        if elem[4] is not None:
            marker = folium.Marker(location=(round(elem[4],6),round(elem[5],6)), popup=elem[0].strip().replace("'","")+' '+str(elem[2])[:15]).add_to(marker_cluster)
    rest_map.save('templates/map.html')
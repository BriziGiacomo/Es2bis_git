if __name__== "__main__":
    SOGLIA_ORE=1067
    planes=list()
    pln1={"codice":"C-137", "modello":"stuka-B2", "ore_volo": 1300, "controlli_ok":True}
    pln2={"codice":"PRIME", "modello":"F-117", "ore_volo": 232, "controlli_ok":False}
    pln3={"codice":"A-AAA", "modello":"stuka-B2", "ore_volo": 2300, "controlli_ok":True}
    pln4={"codice":"ESTEBAN", "modello":"stuka-B1", "ore_volo": 239, "controlli_ok":True}
    pln5={"codice":"ROGER", "modello":"F-11", "ore_volo": 1233, "controlli_ok":False}
    pln6={"codice":"NI--A", "modello":"L-115", "ore_volo": 766, "controlli_ok":True}
    planes.append(pln1)
    planes.append(pln2)
    planes.append(pln3)
    planes.append(pln4)
    planes.append(pln5)
    planes.append(pln6)
    print("Riepilogo dati aerei:")
    for pl in planes:
        print("codice: "+pl["codice"]+", modello: "+ pl["modello"] +", ore volo: "+str(pl["ore_volo"])+", controlli validi: "+str(pl["controlli_ok"]))
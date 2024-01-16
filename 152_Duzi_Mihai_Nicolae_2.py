f = open("cinema.in", "r")
d = {}
cinemauri = []
line = f.readline().split(" % ")
while line != ['']:
    cinema = line[0]
    film = line[1]
    ore = line[2].split()
    if cinema not in d.keys():
        d[cinema] = {}
    d[cinema][film] = ore
    line = f.readline().split(" % ")
def sterge_ore(d, cinema, film, ore):
    for o in ore:
        d[cinema][film].remove(o)
    if d[cinema][film] == []:
        d[cinema].pop(film)
    list = [f for f in d[cinema].keys()]
    return list
def cinema_film(d, cinemas, ora_minima, ora_maxima):
    intre = []
    for cine in d.keys():
        if cine in cinemas:
            for filme in d[cine].keys():
                listaore = []
                for ora in d[cine][filme]:
                    if ora_minima < ora < ora_maxima:
                        listaore.append(ora)
                if listaore != []:
                    intre.append((filme, cine, listaore))
    intre = sorted(intre, key = lambda x: (x[0], -len(x[2])))
    return intre

f = input("f = ")
c = input("c = ")
o = input("o = ")
o = [o]
intr = cinema_film(d, ["Cinema 1", "Cinema 2"], "14:00", "22:00")
ramas = sterge_ore(d,c,f,o)
print(ramas)
print(d)
print(intr)
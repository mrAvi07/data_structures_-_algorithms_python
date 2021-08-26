class DVD:
    def __init__(self, name, director, year):
        self.name = name
        self.director = director
        self.year = year



if __name__=="__main__":

    dvd1 = DVD("love song", "anupam khair", 2002)
    dvd2 = DVD("SAD song", "Ashish chanchlani", 2008)
    dvd3 = DVD("masups song", "gabbar singh", 1995)
    dvd4 = DVD("Panjabi", "dj ani", 1025)

    dvd_list = []

    dvd_list.append(dvd1)
    dvd_list.append(dvd2)
    dvd_list.append(dvd3)
    dvd_list.append(dvd4)

    for dvd in dvd_list:
        print(f"The {dvd.name}, directed by {dvd.director}, released in {dvd.year}.")

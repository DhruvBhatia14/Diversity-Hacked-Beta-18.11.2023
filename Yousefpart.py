class Location:
    def __init__(self, majors_list):
        self.majors = majors_list 
        self.locpref = ["Edmonton", "Red Deer", "Calgary", "Alberta", "Canada"]
        self.universities = [
        # Alberta
        "University of Alberta", "University of Calgary", "University of Lethbridge",
        "Athabasca University", "Grant MacEwan University", "Mount Royal University", 
        "Alberta University of the Arts",

        # British Columbia
        "University of British Columbia", "Simon Fraser University", "University of Victoria",
        "University of Northern British Columbia", "Thompson Rivers University", "Royal Roads University",
        "Capilano University", "Emily Carr University of Art and Design", "Kwantlen Polytechnic University",
        "Justice Institute of British Columbia", "Vancouver Island University", "University of the Fraser Valley",

        # Manitoba
        "University of Manitoba", "University of Winnipeg", "Brandon University", "Université de Saint-Boniface",

        # New Brunswick
        "University of New Brunswick", "Mount Allison University", "St. Thomas University",
        "Université de Moncton",

        # Newfoundland and Labrador
        "Memorial University of Newfoundland",

        # Nova Scotia
        "Dalhousie University", "Saint Mary's University", "Acadia University",
        "University of King's College", "Cape Breton University", "Mount Saint Vincent University",
        "St. Francis Xavier University", "NSCAD University",

        # Ontario
        "University of Toronto", "University of Ottawa", "York University",
        "McMaster University", "University of Waterloo", "Western University",
        "Queen's University", "Carleton University", "Toronto Metropolitan University",
        "University of Guelph", "Brock University", "Wilfrid Laurier University",
        "Lakehead University", "Trent University", "Ontario Tech University",
        "University of Windsor", "Algoma University", "Nipissing University", "Laurentian University",

        # Prince Edward Island
        "University of Prince Edward Island",

        # Quebec
        "McGill University", "Université de Montréal", "Université Laval",
        "Concordia University", "Bishop's University",
        "École Polytechnique",

        # Saskatchewan
        "University of Saskatchewan", "University of Regina",

        # Territories
        "Yukon College"
        ]
        print(len(self.universities))
    def extract_distances(self):
        self.distance_dict = {}
        for c in range(len(self.locpref)-2):
            city = self.locpref[c]
            distance_allowed = input("What distance range in km do you want to allow arround %s? " %city)
            self.distance_dict[city] = distance_allowed
        self.distance_dict[self.locpref[-2]] = True
        self.distance_dict[self.locpref[-1]] = True
        return self.distance_dict
    

    def University_check(self):
        self.distnace_cleared_university = []
        curr_major = self.majors[0]
        current_locpref = self.locpref[0]
        dist_allow = self.distance_dict[current_locpref]
        for university in self.universities:
            #Ask chatgpt if the university is within distance and it has the major and return True or false
            within_distnace = True
            if within_distnace:
                self.distnace_cleared_university.append(university)
            else:
                continue
        
        return self.distnace_cleared_university

x = Location(["eng", "ed", "nurs"])
x.extract_distances()
y = x.University_check()
print(len(y))




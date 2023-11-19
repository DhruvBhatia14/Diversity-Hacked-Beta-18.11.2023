class Location:
    def __init__(self, majors_list):
        self.majors = majors_list 
        self.locpref = []
        self.province = ["Alberta","British Columbia","Manitoba","New Brunswick","Newfoundland and Labrador","Northwest Territories","Nova Scotia",
        "Nunavut","Ontario","Prince Edward Island","Quebec","Saskatchewan","Yukon"]
        self.provcitiesdic = {
        "Alberta": ["Calgary", "Edmonton", "Red Deer","Lethbridge"],
        "British Columbia": ["Vancouver", "Victoria", "Surrey"],
        "Manitoba": ["Winnipeg", "Brandon", "Thompson"],
        "New Brunswick": ["Fredericton", "Saint John", "Moncton"],
        "Newfoundland and Labrador": ["St. John's", "Mount Pearl", "Corner Brook"],
        "Northwest Territories": ["Yellowknife", "Inuvik", "Hay River"],
        "Nova Scotia": ["Halifax", "Dartmouth", "Sydney"],
        "Nunavut": ["Iqaluit", "Rankin Inlet", "Arviat"],
        "Ontario": ["Toronto", "Ottawa", "Mississauga", "Hamilton", "Waterloo"],
        "Prince Edward Island": ["Charlottetown", "Summerside", "Stratford"],
        "Quebec": ["Montreal", "Quebec City", "Laval"],
        "Saskatchewan": ["Saskatoon", "Regina", "Prince Albert"],
        "Yukon": ["Whitehorse", "Dawson City", "Watson Lake"]
        }
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
    
    def userloc(self):
        self.loc = str(input("Where do you currently stay? "))
        return self.loc
    
    def locquestions(self):
        self.provlocs = "The provinces you can choose from are:\n"
        for i in range(len(self.province)-1):
            self.provlocs += self.province[i]+", "
        self.provlocs = self.provlocs + self.province[len(self.province)-1]+"."
        print(self.provlocs)
        tag = True
        while tag:
            try:
                x=(input("Which province would you prefer for University? ")).title()
                assert (x in self.province)
                tag=False
            except AssertionError:
                print("We do not have that in our database right now, please consider a new province.")
        self.locpref.append(x)
        for items in self.provcitiesdic:
            if x == items:
                y = self.provcitiesdic[items]
                break
        q = "The cities you can choose from are:\n"
        for j in range(len(y)-1):
            q += y[j] + ", "
        q = q + y[len(y)-1] + "."
        print(q)
        s = "Which city would you prefer in "+items+"? "
        flag = True
        while flag:
            try:
                t = (input(s)).title()
                assert (t in y)
                flag = False
            except AssertionError:
                    print("We do not have that in our database right now, please consider a new city.")
        self.locpref.insert(0,t)
        flag = True
        while flag:
            s = "Would you consider any other cities in this province other than "+t+"? (Yes/No) "
            z = (input(s)).title()
            if z == "Yes":
                tag = True
                while tag:
                    try:
                        w = (input("Which other city in this province? ")).title()
                        assert (w in y)
                        self.locpref.insert(1,w)
                        tag = False
                    except AssertionError:
                        print("We do not have that in our database right now, please consider a new city.")
            if z == "No":
                flag = False
        self.locpref.append("Canada")
        print(self.locpref)    

    def University_check(self):
        self.distance_cleared_university = []
        curr_major = self.majors[0]
        current_locpref = self.locpref[0]
        for university in self.universities:
            #Ask chatgpt if the university is in the city it has the major and return True or false
            within_distnace = True
            if within_distnace:
                self.distance_cleared_university.append(university)
            else:
                continue
        
        return self.distance_cleared_university

x = Location(["eng", "ed", "nurs"])
x.locquestions()
y = x.University_check()
print(len(y))




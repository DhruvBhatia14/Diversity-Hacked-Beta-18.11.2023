from FatDict import *
class Location:
    def __init__(self, majors_list):
        self.majors = majors_list 
        self.locpref = []
        self.universities_major = returndict()
        self.province = ["Alberta","British Columbia","Manitoba","New Brunswick","Newfoundland and Labrador","Nova Scotia",
        "Nunavut","Ontario","Prince Edward Island","Quebec","Saskatchewan","Yukon"]
        self.provcitiesdic = {
        "Alberta": ["Calgary", "Edmonton", "Athabasca","Lethbridge"],
        "British Columbia": ["Vancouver","Burnaby","Prince George","Kamloops","New Westminister","Nanaimo","Abbotsford", "Victoria", "Surrey"],
        "Manitoba": ["Winnipeg", "Brandon"],
        "New Brunswick": ["Fredericton", "Sackville", "Moncton"],
        "Newfoundland and Labrador": ["St. John's"],
        "Nova Scotia": ["Halifax", "Wolfville","Antigonish", "Sydney"],
        "Nunavut": ["Iqaluit", "Rankin Inlet", "Arviat"],
        "Ontario": ["Toronto", "Ottawa", "Hamilton", "Waterloo","London","Kingston","Guelph","St. Catharines","Thunder Bay", "Peterborough",
        "Oshawa","Windsor","Sault Ste. Marie","North Bay","Sudbury"],
        "Prince Edward Island": ["Charlottetown"],
        "Quebec": ["Montreal", "Quebec City", "Sherbrooke"],
        "Saskatchewan": ["Saskatoon", "Regina"],
        "Yukon": ["Whitehorse"]
        }
        self.universities_locations = {
        "University of Alberta": ['Edmonton', 'Alberta', 'Canada'],
        "Alberta University of the Arts": ['Edmonton', 'Alberta', 'Canada'],
        "Grant MacEwan University": ['Edmonton', 'Alberta', 'Canada'],
        "Athabasca University": ['Athabasca', 'Alberta', 'Canada'],
        "University of Calgary": ['Calgary', 'Alberta', 'Canada'],
        "Mount Royal University": ['Calgary', 'Alberta', 'Canada'],
        "University of Lethbridge": ['Lethbridge', 'Alberta', 'Canada'],
        "University of British Columbia": ['Vancouver', 'British Columbia', 'Canada'],
        "Capilano University": ['Vancouver', 'British Columbia', 'Canada'],
        "Emily Carr University of Art and Design": ['Vancouver', 'British Columbia', 'Canada'],
        "Simon Fraser University": ['Burnaby', 'British Columbia', 'Canada'],
        "Kwantlen Polytechnic University": ['Surrey', 'British Columbia', 'Canada'],
        "University of Victoria": ['Victoria', 'British Columbia', 'Canada'],
        "Royal Roads University": ['Victoria', 'British Columbia', 'Canada'],
        "University of Northern British Columbia": ['Prince George', 'British Columbia', 'Canada'],
        "Thompson Rivers University": ['Kamloops', 'British Columbia', 'Canada'],
        "Justice Institute of British Columbia": ['New Westminister', 'British Columbia', 'Canada'],
        "Vancouver Island University": ['Nanaimo', 'British Columbia', 'Canada'],
        "University of the Fraser Valley": ['Abbotsford', 'British Columbia', 'Canada'],
        "University of Manitoba": ['Winnipeg', 'Manitoba', 'Canada'],
        "University of Winnipeg": ['Winnipeg', 'Manitoba', 'Canada'],
        "Université de Saint-Boniface": ['Winnipeg', 'Manitoba',' Canada'],
        "Brandon University": ['Brandon', 'Manitoba', 'Canada'],
        "University of New Brunswick": ['Fredericton','New Brunswick', 'Canada'],
        "St. Thomas University": ['Fredericton', 'New Brunswick', 'Canada'],
        "Mount Allison University": ['Sackville', 'New Brunswick', 'Canada'],
        "Université de Moncton": ['Moncton', 'New Brunswick', 'Canada'],
        "Memorial University of Newfoundland": ["St. John's", "Newfoundland and Labrador", "Canada"],
        "Dalhousie University": ['Halifax', 'Nova Scotia', 'Canada'],
        "Saint Mary's University": ['Halifax', 'Nova Scotia', 'Canada'],
        "University of King's College": ['Halifax', 'Nova Scotia', 'Canada'],
        "Mount Saint Vincent University": ['Halifax', 'Nova Scotia', 'Canada'],
        "NSCAD University": ['Halifax', 'Nova Scotia', 'Canada'],
        "Acadia University": ['Wolfville', 'Nova Scotia', 'Canada'],
        "Cape Breton University": ['Sydney', 'Nova Scotia', 'Canada'],
        "St. Francis Xavier University": ['Antigonish', 'Nova Scotia', 'Canada'],
        "University of Toronto": ['Toronto', 'Ontario', 'Canada'],
        "York University": ['Toronto', 'Ontario', 'Canada'],
        "Toronto Metropolitan University": ['Toronto', 'Ontario', 'Canada'],
        "University of Ottawa-Université d'Ottawa": ['Ottawa', 'Ontario', 'Canada'],
        "Carleton University": ['Ottawa', 'Ontario', 'Canada'],
        "McMaster University": ['Hamilton', 'Ontario', 'Canada'],
        "University of Waterloo": ['Waterloo', 'Ontario', 'Canada'],
        "Wilfrid Laurier University": ['Waterloo', 'Ontario', 'Canada'],
        "Western University": ['London', 'Ontario', 'Canada'],
        "Queen's University": ['Kingston', 'Ontario', 'Canada'],
        "University of Guelph": ['Guelph', 'Ontario', 'Canada'],
        "Brock University": ['St. Catharines', 'Ontario', 'Canada'],
        "Lakehead University": ['Thunder Bay', 'Ontario', 'Canada'],
        "Trent University": ['Peterborough', 'Ontario', 'Canada'],
        "Ontario Tech University": ['Oshawa', 'Ontario', 'Canada'],
        "University of Windsor": ['Windsor', 'Ontario', 'Canada'],
        "Algoma University": ['Sault Ste. Marie', 'Ontario', 'Canada'],
        "Nipissing University": ['North Bay', 'Ontario', 'Canada'],
        "Laurentian University": ['Sudbury', 'Ontario', 'Canada'],
        "University of Prince Edward Island": ['Charlottetown', 'Prince Edward Island', 'Canada'],
        "McGill University": ['Montreal', 'Quebec', 'Canada'],
        "Université de Montréal": ['Montreal', 'Quebec', 'Canada'],
        "Concordia University": ['Montreal', 'Quebec', 'Canada'],
        "Université Laval": ['Quebec City', 'Quebec', 'Canada'],
        "Bishop's University": ['Sherbrooke', 'Quebec', 'Canada'],
        "University of Saskatchewan": ['Saskatoon', 'Saskatchewan', 'Canada'],
        "University of Regina": ['Regina', 'Saskatchewan', 'Canada'],
        "Yukon College": ['Whitehorse', 'Yukon', 'Canada']
        }
        #Make a dictionary that has keys of all the possible majors and values of true or false for weather the university has the major

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
        "University of Toronto", "University of Ottawa-Université d'Ottawa", "York University",
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

        # Saskatchewan
        "University of Saskatchewan", "University of Regina",

        # Territories
        "Yukon College"
        ]
    
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
        #self.locpref.append(x)
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
                i=1
                while tag:
                    try:
                        w = (input("Which other city in this province? ")).title()
                        assert (w in y)
                        if w not in self.locpref:
                            self.locpref.append(w)
                        elif w in self.locpref:
                            print("This city has alreayd been considered, try another or type No if you have included each city already.")
                            if len(self.locpref)==(len(y)+1):
                                break
                            else:
                                continue
                        tag = False
                    except AssertionError:
                        print("We do not have that in our database right now, please consider a new city.")
            if z == "No":
                flag = False
        self.locpref.append(x)
        print(self.locpref)    

    def University_check(self):
        self.distance_cleared_university = []
        curr_major = self.majors[0]
        current_locpref = self.locpref[0]
        for university in self.universities:
            within_distance = self.val3_uni(university,current_locpref,curr_major)
            if within_distance:
                self.distance_cleared_university.append(university)
            else:
                continue
        
        return self.distance_cleared_university

    def val3_uni(self,university,current_locpref,curr_major):
        TFloc = False
        TFmaj = False
        if current_locpref in self.universities_locations[university]:
            TFloc = True
        if curr_major in self.universities_major[university]:
            TFmaj = True
        if TFloc and TFmaj:
            return True
        else:
            return False
    
    def bunloc(self):
        self.locpref.pop(0)
    
    def bunmajor(self):
        self.majors.pop(0)

if __name__ == "__main__":
    x = Location(["Journalism and Mass Communication","Social Sciences","Sustainability Studies","Education","Tourism and Hospitality","Languages"])
    x.locquestions()
    y = x.University_check()
    print(y)
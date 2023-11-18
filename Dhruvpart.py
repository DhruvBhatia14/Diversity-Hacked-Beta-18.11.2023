province=["Alberta","British Columbia","Manitoba","New Brunswick","Newfoundland and Labrador","Northwest Territories","Nova Scotia",
    "Nunavut","Ontario","Prince Edward Island","Quebec","Saskatchewan","Yukon"]

provcitiesdic = {
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

def userloc():
    loc=str(input("Where do you currently stay? "))
    return loc

def locquestions():
    provlocs="The provinces you can choose from are:\n"
    for i in range(len(province)-1):
        provlocs+=province[i]+", "
    provlocs=provlocs+province[len(province)-1]+"."
    print(provlocs)
    tag=True
    while tag:
        try:
            x=(input("Which province would you prefer for University? ")).title()
            assert (x in province)
            tag=False
        except AssertionError:
            print("We do not have that in our database right now, please consider a new province.")
    locpref=[]
    locpref.append(x)
    for items in provcitiesdic:
        if x==items:
            y=provcitiesdic[items]
            break
    q="The cities you can choose from are:\n"
    for j in range(len(y)-1):
        q+=y[j]+", "
    q=q+y[len(y)-1]+"."
    print(q)
    s="Which city would you prefer in "+items+"? "
    flag=True
    while flag:
        try:
            t=(input(s)).title()
            assert (t in y)
            flag=False
        except AssertionError:
                print("We do not have that in our database right now, please consider a new city.")
    locpref.insert(0,t)
    flag=True
    while flag:
        s="Would you consider any other cities in this province other than "+t+"? (Yes/No) "
        z=(input(s)).title()
        if z=="Yes":
            tag=True
            while tag:
                try:
                    w=(input("Which other city in this province? ")).title()
                    assert (w in y)
                    locpref.insert(1,w)
                    tag=False
                except AssertionError:
                    print("We do not have that in our database right now, please consider a new city.")
        if z=="No":
            flag=False
    locpref.append("Canada")
    print(locpref)
locquestions()
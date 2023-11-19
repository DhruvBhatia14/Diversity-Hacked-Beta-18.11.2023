from majorselection import *
from Unilocation import *

#Geting majors list
student = MajorSelector()
majors = student.major_select()
print(majors)

#Getting Safe Universities list
locate = Location()
locate.locquestions()
safe_Universities = locate.University_check()
Consider_cost = True
while safe_Universities == []:
    if len(locate.locpref) == 1 and len(locate.majors) == 1:
        print("No Univerities Mach what you want, and there are no further options to consider")
        Consider_cost = False
        break
    if len(locate.locpref) != 1 and len(locate.majors) != 1:
        print("No Univerities Mach what you want, would you like to consider location option2:%s or major option2:%s" % locate.locpref[1],locate.majors[1])
        bun = input("Input \"location\" or \"major\" or \"dont reconsider\": ").lower()
        if bun == "location":
            locate.bunloc()
            safe_Universities = locate.University_check()
        elif bun == "major":
            locate.bunmajor()
            safe_Universities = locate.University_check()
        else:
            print("No Univerities Mach what you want")
            Consider_cost = False
            break
    elif len(locate.locpref) != 1:
        print("No Univerities Mach what you want, would you like to consider location option2:%s" % locate.locpref[1])
        bun = input("Input \"yes\" or \"no\": ").lower()
        if bun == "yes":
            locate.bunloc()
            safe_Universities = locate.University_check()
        else:
            print("No Univerities Mach what you want")
            Consider_cost = False
            break
    else:
        print("No Univerities Mach what you want, would you like to consider major option2:%s" % locate.majors[1])
        bun = input("Input \"yes\" or \"no\": ").lower()
        if bun == "yes":
            locate.bunmajor()
            safe_Universities = locate.University_check()
        else:
            print("No Univerities Mach what you want")
            Consider_cost = False
            break
assert safe_Universities != []

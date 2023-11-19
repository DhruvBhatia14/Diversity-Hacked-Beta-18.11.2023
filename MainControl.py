from majorselection import *
from Unilocation import *
from CostFunction import *

def recursion():
    global Consider_cost
    global safe_Universities
    while safe_Universities == []:
        if len(locate.locpref) == 1 and len(locate.majors) == 1:
            print("No Univerities Match what you want, and there are no further options to consider")
            Consider_cost = False
            exit()
        if len(locate.locpref) != 1 and len(locate.majors) != 1:
            print("No Universities Match what you want, would you like to reconsider location option2:%s or major option2:%s" % (locate.locpref[1], locate.majors[1]))
            bun = input("Input \"location\" or \"major\" or \"dont reconsider\": ").lower()
            if bun == "location":
                locate.bunloc()
                safe_Universities = locate.University_check()
            elif bun == "major":
                locate.bunmajor()
                safe_Universities = locate.University_check()
            else:
                print("No Univerities Match what you want")
                Consider_cost = False
                exit()
        elif len(locate.locpref) != 1:
            print("No Univerities Match what you want, would you like to consider location option2:%s" % locate.locpref[1])
            bun = input("Input \"yes\" or \"no\": ").lower()
            if bun == "yes":
                locate.bunloc()
                safe_Universities = locate.University_check()
            else:
                print("No Univerities Match what you want")
                Consider_cost = False
                exit()
        else:
            print("No Univerities Match what you want, would you like to consider major option2:%s" % locate.majors[1])
            bun = input("Input \"yes\" or \"no\": ").lower()
            if bun == "yes":
                locate.bunmajor()
                safe_Universities = locate.University_check()
            else:
                print("No Univerities Match what you want")
                Consider_cost = False
                exit()
    print(safe_Universities)
    if Consider_cost:
        assert safe_Universities != []
        cost_dict = CostCalc(locate.majors,safe_Universities)
        cost_dict1= cost_dict.copy()
        cost_dict2=cost_dict.copy()
        
        budget = float(input("How much are you willing to spend going to this University in total? ").strip("$").strip(",").strip("."))
        for key in cost_dict1:
            if float(((cost_dict1[key].strip("$")).replace(",",""))) > budget:
                del cost_dict[key]
        if cost_dict != {}:
            print("For your top Major %s and your top Location %s:" %(locate.majors[0],locate.locpref[0]))
            for key in cost_dict:
                print(key,":",cost_dict[key])
            exit()
        while cost_dict == {}:
            print("No Universities fall within all your requirements")
            cost_reconsider = input("Budget insufficient, whould you like to reconsider your budget?(Yes/No): ").lower()
            if cost_reconsider == "yes":
                budget = float(input("How much are you willing to spend going to this University in total? ").strip("$").strip(",").strip("."))
                cost_dict = cost_dict1.copy()
                for key in cost_dict2:
                    if float(((cost_dict2[key].strip("$")).replace(",",""))) > budget:
                        del cost_dict[key]
                if cost_dict != {}:
                    print("For your top Major %s and your top Location %s:" %(locate.majors[0],locate.locpref[0]))
                    for key in cost_dict:
                        print(key,":",cost_dict[key])
                    exit()
                    
            else:
                check_again = input("Do you want to try to reconsider major or location, saying no will exit program?(yes/no): ").lower()
                if check_again == 'yes':
                    # go to line 15 and enter the while loop
                    safe_Universities = []
                    recursion()
                else:
                    print("No Univerities Match what you want")
                    exit()

#Geting majors list
#Getting Safe Universities list
student = MajorSelector()
majors = student.major_select()
print(majors)
locate = Location(majors)
locate.locquestions()
safe_Universities = locate.University_check()
print(safe_Universities)
Consider_cost = True
recursion()
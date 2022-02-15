

from tabulate import tabulate


def read():
    empleados={}
    employes_list=[]
    with  open("./files/employees.txt","r",encoding="utf-8") as f:
        for employee_line in f:
            
            name=employee_line.rstrip().split('=')[0]
            days=employee_line.rstrip().split('=')[1]
            days=days.split(",")
            empleados[name]=set(days)
            
    return empleados 



def match_employ(dic_employ):
    dic_match={}
    for name1, set1 in dic_employ.items():
        for name2,set2 in dic_employ.items():
            
            if name1!=name2:
                set_join=set1.intersection(set2)
                count=len(set_join)
                names=name1+ '-' +name2
                names2=name2+ '-' +name1

                if not(names in dic_match) and not(names2 in dic_match):
                    dic_match[names]=count
       
    return dic_match

def show_result(dic_match):

    result=dic_match.items()

    print(tabulate(result, headers=["Names", "Matches"]))
    
  

                

def run():
    empleados=read() 
    print('---------------')
    print(match_employ(empleados))
    show_result(match_employ(empleados))



if __name__ == '__main__':
    run()
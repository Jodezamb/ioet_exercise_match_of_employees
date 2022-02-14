
def read():
    empleados={}
    employes_list=[]
    with  open("./files/employees.txt","r",encoding="utf-8") as f:
        for employee_line in f:
            
            name=employee_line.rstrip().split('=')[0]
            days=employee_line.rstrip().split('=')[1]
            days=days.split(",")
            empleados[name]=days
            
    return empleados 


def match_Employees(dic_employees):
    count=1
    diccion={}
    
    for name, days in dic_employees.items():
        
        for day in days:
            

            if not(day in diccion):
                
                diccion[day]=[name]
            else:
                diccion[day].append(name)
    return diccion


            
        


def run():
    empleados=read()
    print(match_Employees(empleados))


if __name__ == '__main__':
    run()
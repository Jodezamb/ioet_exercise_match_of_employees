
from typing import Dict 
from tabulate import tabulate

'''Funcion que lee el arhivo employees.txt ubicado en la carpeta files
   y devuleve un diccionario employees con los empleados y los dias en los que trabajo
'''
def read() -> dict:

    employees:Dict[str,set]={} # estructura del diccionario que contendra la data
    
    with  open("./files/employees.txt","r",encoding="utf-8") as f:

        for employee_line in f:
            
            name=employee_line.rstrip().split('=')[0] # se realiza un split por el operador '=' y se asigna el primer valor a name [0]
            days=employee_line.rstrip().split('=')[1] # se realiza un split '='  y se asigna los valores de los dias a day 
            days=days.split(",")                      # se realiza un split ','  para separar cada dia de days.
            employees[name]=set(days)  
            
    return employees  # estructura employees -> {'RENE': {'TH01:00-03:00', 'TU10:00-12:00', 'MO10:00-12:00', 'SU20:00-21:00', 'SA14:00-18:00'}}

'''Funcion que recibe como parametro un diccionario con los empleados y sus dias  trabajo 
   y devuleve un diccionario dic_match que contiene las veces que los empleandos coindicen
   en el trabajo
'''

def match_employees(dic_employees: dict) ->dict:

    dic_match:Dict[str,int]={} # estructura del diccionario que contendra la data

    # se realiza una dobla iteraccion para comparar los dias que trabaja un empleado con otro
    for name1, set_days1 in dic_employees.items():
        for name2,set_days2 in dic_employees.items():
            
            # se valida que no se compare  el mismo empleado
            if name1!=name2:
                set_join_days=set_days1.intersection(set_days2) # interseccion de los conjuntos de dias entre los empleados,
                count=len(set_join_days)
                names=name1+ '-' +name2
                names2=name2+ '-' +name1                        # nombre  intercambiado para validacion es lo mismo (Jose-Adrian y Adrian-Jose)        

                if not(names in dic_match) and not(names2 in dic_match): # validacion del doble for nombres repetidos (Jose-Adrian => Adrian-Jose)
                    dic_match[names]=count
       
    return dic_match # estructura dic_match ->  {'RENE-ASTRID': 2, 'RENE-ANDRES': 2,.......,'ANDRES-KEVIN': 3}


'''Funcion que recibe como parametro un diccionario que contiene las veces que los empleandos coindicen
   en el trabajo y devuleve un string en formato de tabla para la muestra de los resultados
'''
def show_result(dic_match: dict)->str:

    result=dic_match.items()
    table=tabulate(result, headers=["Names", "Matches"])

    return table  
    
  
'''Funcion principal donde se ejecuten las funciones para el desarrollo del ejericio
'''
                
def run():

    empleados=read() #contiene el diccionario de employees
    match_empleados=match_employees(empleados) #contiene el diccionario dic_match
    print('------------------------')
    
    print(show_result(match_empleados))  # muestra  el resultado esperado

    #Para mostrar los siguientes diccionarios borrar # de las siguientes lineas. 
    #print(empleados)
    #print(match_empleados)



if __name__ == '__main__':
    run()
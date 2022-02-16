# IOET exercise match employees

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our example below:

**EXAMPLE**

**INPUT**

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

**OUTPUT:**

ASTRID-RENE: 2

ASTRID-ANDRES: 3

RENE-ANDRES: 2


# Resource

To make use of the repository you must execute the command **"git clone (url)"** from your computer, you must also have **python 3** installed and the following libraries.

 - Typing
 - Tabulate

 and you should continue with the following steps.....


# RUN
- Open visual studio Code in the folder where the repository was cloned

![ ](https://github.com/Jodezamb/ioet_exercise_match_of_employees/blob/main/files/start.png?raw=true)

- Open a terminal in VSC in the same folder of the repository, then proceed with the installation of the virtual enviroment 
## Virtual enviroment
### Windows 
1. py -m venv venv 
2. .\venv\Scripts\activate  

### Linux
1. sudo apt-get install python3-pip
2. apt-get install python3-venv
3. python3 -m venv venv
4. source venv/bin/activate
 
and   the libraries and execute line by line.
libraries
1. pip install tabulate
2. pip install mypy
3. py -m pip install types-tabulate ![image](https://user-images.githubusercontent.com/67130967/154313679-ee4601d0-923c-4102-ba49-68cf96edce74.png)
![image](https://user-images.githubusercontent.com/67130967/154313684-923edafa-c176-4371-9f8c-3363d3b18547.png)

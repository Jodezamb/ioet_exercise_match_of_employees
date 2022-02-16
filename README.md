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

# Description
For the resolution of the exercise, libraries such as mypy were used to perform the validation of static typing and not incur in typing errors, in addition, the Tabulate library was used to format the data shown to the user as a table and finally it was used the typing module to offer a better structure in the typing of the types of objects that will be used for the development of the exercise.


# Resource

To make use of the repository you must execute the command **"git clone (url)"** from your computer, you must also have **python 3** installed and the following libraries.

 - Typing
 - Tabulate
 - mypy

 and you should continue with the following steps.....


# RUN
- Open visual studio Code in the folder where the repository was cloned

![ ](https://github.com/Jodezamb/ioet_exercise_match_of_employees/blob/main/files/start.png?raw=true)

- Open a terminal in VSC in the same folder of the repository, then proceed with the installation of the virtual enviroment 
## Virtual enviroment
After installing and activating the virtual environment, the environment should appear in the terminal

### Windows 
1. py -m venv venv 
2. .\venv\Scripts\activate  

*example*

![ ](https://github.com/Jodezamb/ioet_exercise_match_of_employees/blob/main/files/venvi.png?raw=true)

### Linux
1. sudo apt-get install python3-pip
2. sudo apt-get install python3-venv
3. python3 -m venv venv
4. source venv/bin/activate

*example*

![ ](https://github.com/Jodezamb/ioet_exercise_match_of_employees/blob/main/files/linux.png?raw=true)

 


 **Execute line by line the following commands in the terminal to download the necessary modules **

1. pip install tabulate   
2. pip install mypy

### As a last step, verify that VSC recognizes the virtual environment like this and WE ARE READY TO RUN
![ ](https://github.com/Jodezamb/ioet_exercise_match_of_employees/blob/main/files/check.png?raw=true)


## Result
Pairs employees with times they are at work per week.

![ ](https://github.com/Jodezamb/ioet_exercise_match_of_employees/blob/main/files/result.png?raw=true)

## Test static typing
It can be seen that the result of the validation of the static typing through mypy was successful since it does not show typing errors

![ ](https://github.com/Jodezamb/ioet_exercise_match_of_employees/blob/main/files/mypy.png?raw=true)





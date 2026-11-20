
class employee:
    def __init__(self, name, ID, job_title, salary, department, joining_date):
        self.name = name
        self.ID = ID
        self.department = department
        self.job_title = job_title
        self.salary = salary
        self.joining_date = joining_date

employees = []

while True:
    ask = input("Do u wanna create a new employee?: ")
    if ask == "exit":
        break
    elif ask == "yes":
        name = input("enter the name of the employee: ")
        ID = input("enter the ID: ")
        Department = input("enter the name of the department: ")
        job_title = input("enter the job title: ")
        salary = input("enter the salary: ")
        joining_date = input("enter the joining date: ")

        employees.append(employee(
            name, ID, job_title, salary, Department, joining_date
        ))

        print("Employee created successfully!")

    elif ask == "no":
        search_id = input("Enter the employee ID you want to find: ")
        if employee.ID == employee.ID:
         print("the ids are same")
         for person in employees:
            if person.ID == search_id:
                print("Employee found!")
                print("Name:", person.name)
                print("ID:", person.ID)
                print("Job Title:", person.job_title)
                print("Salary:", person.salary)
                print("Department:", person.department)
                print("Joining Date:", person.joining_date)
                break
        else:
            print("Employee not found!")

    else:
        print("Invalid input! Please enter yes or no.")

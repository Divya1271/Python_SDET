class Company:
    company_name="Infosys"
    def __init__(self,employee_name,designation):
        self.employee_name=employee_name
        self.designation=designation
    def show(self):
        print(f"The name of the employee,company name and his designation is:{self.employee_name},{self.designation},{self.company_name}")
c1=Company("Ram","ASE")
c2=Company("Rohan","SD")
c1.show()
c2.show()


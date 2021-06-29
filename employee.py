import csv
def write_as_file(info_list):
    with open("employee_info.csv",'a+',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell==0:
            writer.writerows(["Name","Age","Degree","email-id","phone-no"])
        writer.writerow(info_list)
if __name__=="__main__":
    condition=True
    serial_no = 1
    while(condition):
        emp_details=input("\nenter the number #{} and details of the emploee as Name,Age,Degree,emailid,phone-no".format(serial_no))
        employee_list=emp_details.split(" ")
        print("\nthe entered information is:\nName: {}\nAge: {}\nDegree: {}\nemailid: {}\nphone-no: {}"
                .format(employee_list[0],employee_list[1],employee_list[2],employee_list[3],employee_list[4]))
        check_condition=input("check whether the entered information is corect or not (yes/no):")
        if check_condition=="yes":
            write_as_file(employee_list)
            condition_check=input("you would like to enter the next employee details (yes/no)")
            if condition_check=="yes":
                condition=True
                serial_no=serial_no+1
            elif condition_check=="no":
                condition=False
        elif check_condition == "no":
            print("please reenter the details from the first")



import csv

def write_into_csv(information_list):
    with open('student_info.csv','a',newline='') as csv_line:
        writer=csv.writer(csv_line)

        if csv_line.tell() == 0:
            writer.writerow(["Name","Age","Contact_number","Email_ID"])
        writer.writerow(information_list)

if __name__ == '__main__':
    condition=True
    student_count=1

    while(condition):
        student_info=input(f"Enter information for student #{student_count} in the followin pattern(Name Age Contact_number Email_ID):")
        #splitting the data
        student_info_list=student_info.split(" ")
        print(f"\nThe entered information is: \nName:{student_info_list[0]}\nAge:{student_info_list[1]}\nContact_Number:{student_info_list[2]}\nEmailID:{student_info_list[3]}")
        check= input("Is the information entered is correct?(yes/no)")
        if check=="yes":
             write_into_csv(student_info_list)
             condition_check=input("Enter (yes or no) to proceed to enter details:")
             if condition_check=="yes":
                student_count+=1
                condition=True

             elif condition_check=="no":
                condition=False
        
        elif check=="no":
            print("\nPlease re enter the details")

        
       
        



import os
def load__frist():
    students={}
    file=open("frist.txt","r")
    lines=file.readlines()
    file.close()
    for line in lines:
        p=line.strip().split(",")
        if len(p)!=4:
            continue
        name=p[0]
        students[name]={"clade":p[1],"year":p[2],"born":p[3]}
    return students
def save__frist(students):
    file=open("frist.txt","w")
    for name ,data in students.items():
        line=f"{name},{data["clade"]},{data["year"]},{data["born"]}\n"
        file.write(line)
    file.close()
def print_frist(students):
    os.system("cls")
    print("="*86)
    print(f"|{"name":<25}|{"clade":<25}|{"year":<15} |{"born":<15}|")
    print("="*86)
    for name,student in students.items():
        print(f"|{name:<25}|{student["clade"]:<25}|{student["year"]:<15} |{student["born"]:<15}|")
        print("_"*86)
def add_frist(students):
    os.system("cls")
    name=input("Entre name :")
    if name in students:
        print("student found")
    else:
        clade=input("Entre clade :")
        year=input("Entre year :")
        born=input("Entre born :")
        students[name]={"clade":clade,"year":year,"born":born}
        print("add student ")
def edit_frist(students):
    os.system("cls")
    name=input("Entre name :")
    if name in students:
        clade=input("Entre clade :")
        year=input("Entre year :")
        born=input("Entre born :")
        students[name]={"clade":clade,"year":year,"born":born}
        print("student update ")
    else:
        print("student not fount")
def delete_frist(students):
    os.system("cls")
    name=input("Entre name :")
    if name in students:
        del students[name]
        print("student delete ")
    else:
        print("student not fount")
def search_frist(students):
    os.system("cls")
    name=input("Entre name :")
    if name in students:
        data=students[name]
        print("="*86)
        print(f"|{"name":<25} |{"clade":<25}| {"year":<15} |{"born":<15}|")
        print("="*86)
        print(f"|{name:<25}|{data["clade"]:<25}|{data["year"]:<15}|{data["born"]:<15}|")
        print("="*86)
    else:
        print("student not found")
student_data=load__frist()
def manage_frist ():
    os.system("cls")
    while True:
        print("1=all students ")
        print("2=add students ")
        print("3=modify students ")
        print("4=delete students ")
        print("5=search students ")
        print("6=save and Exit  ")
        choice=int(input("Entre choice :"))
        if choice==1:
            print_frist(student_data)
        elif choice==2:
            add_frist(student_data)
        elif choice==3:
            edit_frist(student_data)
        elif choice==4:
            delete_frist(student_data)
        elif choice==5:
            search_frist(student_data)
        elif choice==6:
            save__frist(student_data)
            break
        else:
            os.system("cls")
            print("error")
def load_sconde_scondary():
    student2={}
    file=open("sconde.txt","r")
    lines=file.readlines()
    file.close()
    for line in lines:
        p=line.strip().split(",")
        if len(p)!=4:
            continue
        name=p[0]
        student2[name]={"clade":p[1],"year":p[2],"born":p[3]}
    return student2
def save__sconde_scondary(student2):
    file=open("sconde.txt","w")
    for name ,data in student2.items():
        line=f"{name},{data["clade"]},{data["year"]},{data["born"]}\n"
        file.write(line)
    file.close()
def print_sconde_scondary(student2):
    os.system("cls")
    print("="*86)
    print(f"|{"name":<25}|{"clade":<25}|{"year":<15} |{"born":<15}|")
    print("="*86)
    for name,student in student2.items():
        print(f"|{name:<25}|{student["clade"]:<25}|{student["year"]:<15} |{student["born"]:<15}|")
        print("_"*86)
def add_sconde_scondary(student2):
    os.system("cls")
    name=input("Entre name :")
    if name in student2:
        print("student found")
    else:
        clade=input("Entre clade :")
        year=input("Entre year :")
        born=input("Entre born :")
        student2[name]={"clade":clade,"year":year,"born":born}
        print("add student ")
def edit_sconde_scondary(student2):
    os.system("cls")
    name=input("Entre name :")
    if name in student2:
        clade=input("Entre clade :")
        year=input("Entre year :")
        born=input("Entre born :")
        student2[name]={"clade":clade,"year":year,"born":born}
        print("student update ")
    else:
        print("student not fount")
def delete_sconde_scondary(student2):
    os.system("cls")
    name=input("Entre name :")
    if name in student2:
        del student2[name]
        print("student delete ")
    else:
        print("student not fount")
def search_sconde_scondary(student2):
    os.system("cls")
    name=input("Entre name :")
    if name in student2:
        data=student2[name]
        print("="*86)
        print(f"|{"name":<25} |{"clade":<25}| {"year":<15} |{"born":<15}|")
        print("="*86)
        print(f"|{name:<25}|{data["clade"]:<25}|{data["year"]:<15}|{data["born"]:<15}|")
        print("="*86)
    else:
        print("student2 not found")
sconde_data=load_sconde_scondary()
def manage_scond():
    os.system("cls")
    while True:
        print("1=all students ")
        print("2=add students ")
        print("3=edit students ")
        print("4=delete students ")
        print("5=search students ")
        print("6=save and Exit  ")
        choice=int(input("Entre choice :"))
        if choice==1:
            print_sconde_scondary(sconde_data)
        elif choice==2:
            add_sconde_scondary(sconde_data)
        elif choice==3:
            edit_sconde_scondary(sconde_data)
        elif choice==4:
            delete_sconde_scondary(sconde_data)
        elif choice==5:
            search_sconde_scondary(sconde_data)
        elif choice==6:
            save__sconde_scondary(sconde_data)
            break
        else:
         print("error")
def load_thirty_scondary():
    student3={}
    file=open("thirty.txt","r")
    lines=file.readlines()
    file.close()
    for line in lines:
        p=line.strip().split(",")
        if len(p)!=4:
            continue
        name=p[0]
        student3[name]={"clade":p[1],"year":p[2],"born":p[3]}
    return student3
def save_thirty_scondary(student3):
    file=open("thirty.txt","w")
    for name ,data in student3.items():
        line=f"{name},{data["clade"]},{data["year"]},{data["born"]}\n"
        file.write(line)
    file.close()
def print_thirty_scondary(student3):
    os.system("cls")
    print("="*86)
    print(f"|{"name":<25}|{"clade":<25}|{"year":<15} |{"born":<15}|")
    print("="*86)
    for name,student in student3.items():
        print(f"|{name:<25}|{student["clade"]:<25}|{student["year"]:<15} |{student["born"]:<15}|")
        print("_"*86)
def add_thirty_scondary(student3):
    os.system("cls")
    name=input("Entre name :")
    if name in student3:
        print("student found")
    else:
        clade=input("Entre clade :")
        year=input("Entre year :")
        born=input("Entre born :")
        student3[name]={"clade":clade,"year":year,"born":born}
        print("add student ")
def edit_thirty_scondary(student3):
    os.system("cls")
    name=input("Entre name :")
    if name in student3:
        clade=input("Entre clade :")
        year=input("Entre year :")
        born=input("Entre born :")
        student3[name]={"clade":clade,"year":year,"born":born}
        print("student update ")
    else:
        print("student not fount")
def delete_sconde_scondary(student3):
    os.system("cls")
    name=input("Entre name :")
    if name in student3:
        del student3[name]
        print("student delete ")
    else:
        print("student not fount")
def search_thirty_scondary(student3):
    os.system("cls")
    name=input("Entre name :")
    if name in student3:
        data=student3[name]
        print("="*86)
        print(f"|{"name":<25} |{"clade":<25}| {"year":<15} |{"born":<15}|")
        print("="*86)
        print(f"|{name:<25}|{data["clade"]:<25}|{data["year"]:<15}|{data["born"]:<15}|")
        print("="*86)
    else:
        print("student not found")
thirty_data=load_thirty_scondary()
def manage_thirty():
    os.system("cls")
    while True:
        print("1=all students ")
        print("2=add students ")
        print("3=edit students ")
        print("4=delete students ")
        print("5=search students ")
        print("6=save and Exit  ")
        choice=int(input("Entre choice :"))
        if choice==1:
                print_thirty_scondary(thirty_data)
        elif choice==2:
            add_thirty_scondary(thirty_data)
        elif choice==3:
            edit_thirty_scondary(thirty_data)
        elif choice==4:
            delete_sconde_scondary(thirty_data)
        elif choice==5:
            search_thirty_scondary(thirty_data)
        elif choice==6:
            save_thirty_scondary(thirty_data)
            break
        else:
            print("error")
def manage_student():
        os.system("cls")
        while True:
            print("1=frist_scondary ")
            print("2=scond_scondary ")
            print("3=thirty_scondary ")
            print("4= Exit  ")
            choice=int(input("Entre choice :"))
            if choice==1:
                manage_frist()
            elif choice==2:
                manage_scond()
            elif choice==3:
                manage_thirty()
            elif choice==4:
                break
            else:
                os.system("cls")
                print("error")
def load_teacher():
    teacher1={}
    file=open("teacher.txt","r")
    lines=file.readlines()
    file.close()
    for line in lines:
        p=line.strip().split(",")
        if len(p)!=3:
            continue
        name=p[0]
        teacher1[name]={"qualification":p[1],"cource":p[2]}
    return teacher1
def save_teacher(teacher1):
    file=open("teacher.txt","w")
    for name ,data in teacher1.items():
        line=f"{name},{data['qualification']},{data['cource']}\n"
        file.write(line)
    file.close()
def print_teacher(teacher1):
    os.system("cls")
    print("="*86)
    print(f"|{'name':<25}|{'qualification':<25}|{'cource':<15}|")
    print("="*86)
    for name,data in teacher1.items():
        print(f"|{name:<25}|{data['qualification']:<25}|{data['cource']:<15}|")
        print("_"*86)
def add_teacher(teacher1):
    os.system("cls")
    name=input("Entre name :")
    if name in teacher1:
        print("teacher found")
    else:
        qualification=input("Entre  qualification :")
        cource=input("Entre   cource :")
        teacher1[name]={"qualification":qualification,"cource":cource}
        print("add student ")
def edit_teacher(teacher1):
    os.system("cls")
    name=input("Entre name :")
    if name in teacher1:
        qualification=input("Entre  qualification :")
        cource=input("Entre   cource :")
        teacher1[name]={"qualification":qualification,"cource":cource}
        print("teacher update ")
    else:
        print("teacher not fount")
def delete_teacher(teacher1):
    os.system("cls")
    name=input("Entre name :")
    if name in teacher1:
        del teacher1[name]
        print("teacher delete ")
    else:
        print("teacher not fount")
def search_teacher(teacher1):
    os.system("cls")
    name=input("Entre name :")
    if name in teacher1:
        data=teacher1[name]
        print("="*86)
        print(f"|{'name':<25} |{'qualification':<25}| {'cource':<15}|")
        print("="*86)
        print(f"|{name:<25}|{data['qualification']:<25}|{data['cource']:<15}|")
        print("="*86)
    else:
        print("teacher not found")
t_data=load_teacher()
def manage_teacher ():
    os.system("cls")
    while True:
        print("1=all teacher ")
        print("2=add teacher")
        print("3=edit teacher ")
        print("4=delete teacher ")
        print("5=search teacher ")
        print("6=save and Exit  ")
        choice=int(input("Entre choice :"))
        if choice==1:
            print_teacher(t_data)
        elif choice==2:
            add_teacher(t_data)
        elif choice==3:
            edit_teacher(t_data)
        elif choice==4:
            delete_teacher(t_data)
        elif choice==5:
            search_teacher(t_data)
        elif choice==6:
            save_teacher(t_data)
            break
        else:
            print("error")
def load_grade1():
    grade1={}
    file=open("grade_frist.txt","r")
    lines=file.readlines()
    file.close
    for line in lines:
        p=line.strip().split(",")
        if len(p)!=3:
            continue
        name=p[0]
        grade1[name]={"total":p[1],"average":p[2]}
    return grade1
def save_grade1(grade1):
    file=open("grade_frist.txt","w")
    for name ,data in grade1.items():
        line=f"{name},{data["total"]},{data["average"]}\n"
        file.write(line)
    file.close()
def print_grade1(grade1):
    os.system("cls")
    print("="*86)
    print(f"|{"name":<25}|{"total":<25}|{"average":<15} |")
    print("="*86)
    for name,g in grade1.items():
        print(f"|{name:<25}|{g["total"]:<25}|{g["average"]:<15}|")
        print("_"*86)
def add_grade1(grade1):
    os.system("cls")
    name=input("Entre name :")
    if name in grade1:
        print("grade1 found")
    else:
        total=input("Entre total :")
        average=input("Entre average:")
        
        grade1[name]={"total":total,"average":average}
        print("add grade1 ")
def edit_grade1(grade1):
    os.system("cls")
    name=input("Entre name :")
    if name in grade1:
        total=input("Entre total :")
        average=input("Entre average :")
        
        grade1[name]={"total":total,"average":average}
        print("grade1 update ")
    else:
        print("grade1 not fount")
def delete_grade1(grade1):
    os.system("cls")
    name=input("Entre name :")
    if name in grade1:
        del grade1[name]
        print("grade1 delete ")
    else:
        print("grade1 not fount")
def search_grade1(grade1):
    os.system("cls")
    name=input("Entre name :")
    if name in grade1:
        data=grade1[name]
        print("="*86)
        print(f"|{"name":<25} |{"total":<25}| {"average":<15}|")
        print("="*86)
        print(f"|{name:<25}|{data["total"]:<25}|{data["average"]:<15}|")
        print("="*86)
    else:
        print("grade1 not found")
grade1_data=load_grade1()
def manage_grade_frist():
    os.system("cls")
    while True:
        print("1=all  grade1")
        print("2=add grade1 ")
        print("3=edit grade1 ")
        print("4=delete grade1 ")
        print("5=search grade1 ")
        print("6=save and Exit  ")
        choice=int(input("Entre choice :"))
        if choice==1:
            print_grade1(grade1_data)
        elif choice==2:
            add_grade1(grade1_data)
        elif choice==3:
            edit_grade1(grade1_data)
        elif choice==4:
            delete_grade1(grade1_data)
        elif choice==5:
            search_grade1(grade1_data)
        elif choice==6:
            save_grade1(grade1_data)
            break
        else:
            print("error")
def load_grade2():
    grade2={}
    file=open("grade_scond.txt","r")
    lines=file.readlines()
    file.close
    for line in lines:
        p=line.strip().split(",")
        if len(p)!=3:
            continue
        name=p[0]
        grade2[name]={"total":p[1],"average":p[2]}
    return grade2
def save_grade2(grade2):
    file=open("grade_scond.txt","w")
    for name ,data in grade2.items():
        line=f"{name},{data["total"]},{data["average"]}\n"
        file.write(line)
    file.close()
def print_grade2(grade2):
    os.system("cls")
    print("="*86)
    print(f"|{"name":<25}|{"total":<25}|{"average":<15} |")
    print("="*86)
    for name,g in grade2.items():
        print(f"|{name:<25}|{g["total"]:<25}|{g["average"]:<15}|")
        print("_"*86)
def add_grade2(grade2):
    os.system("cls")
    name=input("Entre name :")
    if name in grade2:
        print("grade2 found")
    else:
        total=input("Entre total :")
        average=input("Entre average:")
        
        grade2[name]={"total":total,"average":average}
        print("add grade2 ")
def edit_grade2(grade2):
    os.system("cls")
    name=input("Entre name :")
    if name in grade2:
        total=input("Entre total :")
        average=input("Entre average :")
        
        grade2[name]={"total":total,"average":average}
        print("grade2 update ")
    else:
        print("grade2 not fount")
def delete_grade2(grade2):
    os.system("cls")
    name=input("Entre name :")
    if name in grade2:
        del grade2[name]
        print("grade2 delete ")
    else:
        print("grade2 not fount")
def search_grade2(grade2):
    os.system("cls")
    name=input("Entre name :")
    if name in grade2:
        data=grade2[name]
        print("="*86)
        print(f"|{"name":<25} |{"total":<25}| {"average":<15}|")
        print("="*86)
        print(f"|{name:<25}|{data["total"]:<25}|{data["average"]:<15}|")
        print("="*86)
    else:
        print("grade2 not found")
grade2_data=load_grade2()
def manage_grade_scond():
    os.system("cls")
    while True:
        print("1=all  grade2")
        print("2=add grade2 ")
        print("3=edit grade2 ")
        print("4=delete grade2 ")
        print("5=search grade2")
        print("6=save and Exit  ")
        choice=int(input("Entre choice :"))
        if choice==1:
            print_grade2(grade2_data)
        elif choice==2:
            add_grade2(grade2_data)
        elif choice==3:
            edit_grade2(grade2_data)
        elif choice==4:
            delete_grade2(grade2_data)
        elif choice==5:
            search_grade2(grade2_data)
        elif choice==6:
            save_grade2(grade2_data)
            break
        else:
            print("error")
def load_grade3():
    grade3={}
    file=open("grade_thirty.txt","r")
    lines=file.readlines()
    file.close
    for line in lines:
        p=line.strip().split(",")
        if len(p)!=3:
            continue
        name=p[0]
        grade3[name]={"total":p[1],"average":p[2]}
    return grade3
def save_grade3(grade3):
    file=open("grade_thirty.txt","w")
    for name ,data in grade3.items():
        line=f"{name},{data["total"]},{data["average"]}\n"
        file.write(line)
    file.close()
def print_grade3(grade3):
    os.system("cls")
    print("="*86)
    print(f"|{"name":<25}|{"total":<25}|{"average":<15} |")
    print("="*86)
    for name,g in grade3.items():
        print(f"|{name:<25}|{g["total"]:<25}|{g["average"]:<15}|")
        print("_"*86)
def add_grade3(grade3):
    os.system("cls")
    name=input("Entre name :")
    if name in grade3:
        print("grade2 found")
    else:
        total=input("Entre total :")
        average=input("Entre average:")
        
        grade3[name]={"total":total,"average":average}
        print("add grade2 ")
def edit_grade3(grade3):
    os.system("cls")
    name=input("Entre name :")
    if name in grade3:
        total=input("Entre total :")
        average=input("Entre average :")
        
        grade3[name]={"total":total,"average":average}
        print("grade3 update ")
    else:
        print("grade3 not fount")
def delete_grade3(grade3):
    os.system("cls")
    name=input("Entre name :")
    if name in grade3:
        del grade3[name]
        print("grade3 delete ")
    else:
        print("grade3 not fount")
def search_grade3(grade3):
    os.system("cls")
    name=input("Entre name :")
    if name in grade3:
        data=grade3[name]
        print("="*86)
        print(f"|{"name":<25} |{"total":<25}| {"average":<15}|")
        print("="*86)
        print(f"|{name:<25}|{data["total"]:<25}|{data["average"]:<15}|")
        print("="*86)
    else:
        print("grade3 not found")
grade3_data=load_grade3()
def manage_grade_thirty():
    os.system("cls")
    while True:
        print
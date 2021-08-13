import tax_calculator as tc
import Person as pc

workers = []
counter = 0


def all_people():
    if len(workers) > 0:
        print("|No.| Name | Age | Gross Pay | Net Pay |")
        print("|---|------|-----|-----------|---------|")
        for worker in workers:
            print("|", workers.index(worker) + 1, "|", worker.name, "|", worker.age, "|", worker.salary, "|",
                  worker.net_pay, "|")
    else:
        print("No Workers")


while counter < 2:
    try:
        name = str(input("Enter your name: \n"))
        try:
            age = int(input("Enter your age: \n"))
            gross_pay = int(input("Enter your pay: \n"))
            net_pay = tc.total_calc_tax(gross_pay, age)
            person = pc.Person(
                name,
                age,
                gross_pay,
                net_pay
            )
            workers.append(person)
            counter += 1
        except ValueError:
            print("Invalid Data")
    except KeyboardInterrupt:
        print('The program was stopped by the user')
        all_people()
        exit()
all_people()

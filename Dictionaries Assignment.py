
# Create a list with all employee information

employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]


# Separate the information and make sure there are no duplicates.

employee_numbers = []
employee_names = []
hourly_wages = []

for item in employee_data:

    if type(item) == int:
        if item not in employee_numbers:
            employee_numbers.append(item)

    elif type(item) == str:
        if item not in employee_names:
            employee_names.append(item)

    elif type(item) == float:
        if item not in hourly_wages:
            hourly_wages.append(item)


# Display the three lists

print("Employee Numbers:")
print(employee_numbers)

print("Employee Names:")
print(employee_names)

print("Hourly Wages:")
print(hourly_wages)


# Calculate hourly rates with benefits

total_hourly_rate = []

for wage in hourly_wages:
    rate = wage * 1.3
    total_hourly_rate.append(rate)

print("Total Hourly Rates:")
print(total_hourly_rate)


# Find the highest hourly rate

highest_rate = max(total_hourly_rate)

print("Highest Hourly Rate:", highest_rate)

if highest_rate > 37.30:
    print("Warning: Someone's salary may be a budget concern.")
else:
    print("There are no salary budget concerns.")


# Find salaries between 28.15 and 30.65

underpaid_salaries = []

for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("Underpaid Salaries:")
print(underpaid_salaries)


# Calculate employee raises

company_raises = []

for wage in hourly_wages:

    if wage >= 22 and wage < 24:
        new_wage = wage * 1.05

    elif wage >= 24 and wage < 26:
        new_wage = wage * 1.04

    elif wage >= 26 and wage < 28:
        new_wage = wage * 1.03

    else:
        new_wage = wage * 1.02

    company_raises.append(new_wage)

print("Company Raises:")
print(company_raises)


# Create a complex condition with four truth tests.

if len(employee_numbers) > 0 and len(employee_names) > 0 and len(hourly_wages) > 0 and highest_rate > 22:
    print("All employee information is available.")
else:
    print("Some employee information is missing.")


# Combine all employee information into a list of dictionaries

employee_database = []

for index in range(len(employee_numbers)):

    employee_record = {
        "employee_number": employee_numbers[index],
        "employee_name": employee_names[index],
        "employee_salary": hourly_wages[index],
        "total_hourly_rate": total_hourly_rate[index],
        "company_raise": company_raises[index]
    }

    employee_database.append(employee_record)


# Display the final employee database

print("Final Employee Database:")
print(employee_database)

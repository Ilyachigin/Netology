from accounting.application.salary import *
from accounting.application.db.people import *
from datetime import *


if __name__ == '__main__':
    print(date.today())
    get_employees()
    calculate_salary()


from modelos.usuarios.user import User
from modelos.company.company import Company
from modelos.infor import Work

User.create_user()
Work.infor_works()
Company.create_company()

def main():
    Company.company_list()
    User.user_list()
    Work.work_list()

if __name__ == '__main__':
    main()
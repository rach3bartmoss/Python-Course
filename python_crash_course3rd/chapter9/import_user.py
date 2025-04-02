from module_user import User
from module_admin import Admin, Privileges

user1 = User('Rache', 'Bartmoss')

admin1 = Admin(user1.first_name, user1.last_name)

admin1.describe_user()

admin1.privileges.show_privileges()


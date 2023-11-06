class Permission:
    """Represents a permission that can be granted to a role."""

    def __init__(self, name):
        self.name = name


class Role:
    """Represents a role with a set of permissions."""

    def __init__(self, name):
        self.name = name
        self.permissions = []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class User:
    """Represents a user with roles in various courses."""

    def __init__(self, username):
        self.username = username
        self.roles = {}  # Dictionary mapping course to role

    def assign_role(self, course, role):
        self.roles[course] = role

    def can_perform_action(self, course, action):
        role = self.roles.get(course)
        if role and role.has_permission(action):
            return True
        return False


class Course:
    """Represents a course with enrolled students and professors."""

    def __init__(self, name):
        self.name = name
        self.users = []

    def enroll_user(self, user, role):
        user.assign_role(self, role)
        self.users.append(user)


class Forum:
    """Represents the forum system managing courses and user roles."""

    def __init__(self):
        self.courses = {}
        self.users = {}

    def add_course(self, course):
        self.courses[course.name] = course

    def add_user(self, user):
        self.users[user.username] = user

    def assign_user_to_course(self, username, course_name, role):
        user = self.users.get(username)
        course = self.courses.get(course_name)
        if user and course:
            course.enroll_user(user, role)


# Example usage
# Create permissions
send_breakout = Permission('send_to_breakout')
tech_support = Permission('tech_support')

# Create roles
professor_role = Role('professor')
professor_role.add_permission(send_breakout)
student_role = Role('student')
tech_support_role = Role('tech_support')
tech_support_role.add_permission(tech_support)

# Create users
Mera = User('Mera')
bob = User('Bob')

# Create courses
math_course = Course('Mathematics')
cs_course = Course('Computer Science')

# Create forum system
forum = Forum()
forum.add_course(math_course)
forum.add_course(cs_course)
forum.add_user(Mera)
forum.add_user(bob)

# Assign roles to users in courses
forum.assign_user_to_course('Mera', 'Mathematics', professor_role)
forum.assign_user_to_course('Bob', 'Computer Science', student_role)

# Check if Mera can send the class to breakout in Mathematics course
# Should return true
print(Mera.can_perform_action(math_course, send_breakout))

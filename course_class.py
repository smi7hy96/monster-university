class Course:

    def __init__(self, module_name, list_of_students, start_date):
        self.__module_name = module_name
        self.list_of_students = list_of_students
        self.start_date = start_date

    def set_module_name(self, module_name):
        self.__module_name = module_name

    def get_module_name(self):
        return self.__module_name

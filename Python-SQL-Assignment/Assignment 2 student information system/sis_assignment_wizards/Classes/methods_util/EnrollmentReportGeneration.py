from MagicalDBUtil import MagicalDBUtil  # Assuming you have a Harry Potter-themed DBUtil

class EnchantmentReportGeneration:
    def __init__(self, magical_db_util):
        self.magical_db_util = magical_db_util

    def generate_enchantment_report(self):
        course_code = input("Enter the course code: ")
        query = "SELECT * FROM magical_courses mc JOIN magical_enrollments me ON mc.course_code = me.course_code WHERE mc.course_code = %s"
        value = (course_code,)
        return self.magical_db_util.fetchall(query, value)

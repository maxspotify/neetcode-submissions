class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        for s in sandwiches:
            student_count = len(students)
            found = False
            while student_count and not found:
                student = students.popleft()
                if s == student:
                    found = True
                else:
                    students.append(student)
                    student_count -= 1
            if not found:
                return len(students)
        return 0
            
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle = students.count(0)
        square = len(students) - circle

        for sandwich in sandwiches:
            if sandwich and square:
                square -= 1
            elif (not sandwich) and circle:
                circle -= 1
            else:
                break
        return circle + square
from dataclasses import dataclass
from datetime import time
from timefold.solver.domain import planning_entity, PlanningId, PlanningVariable

@dataclass
class Timeslot:
    id: int
    day_of_week: str
    start_time: time
    end_time: time

@planning_entity
@dataclass
class Lesson:
    id: int
    subject: str
    teacher: str
    student_group: str
    timeslot: Timeslot = None
    room: str = None

@dataclass
class TimeTable:
    timeslots: list[Timeslot]
    rooms: list[str]
    lessons: list[Lesson]

def generate_problem():
    timeslots = [
        Timeslot(1, "Monday", time(9, 0), time(10, 0)),
        Timeslot(2, "Tuesday", time(9, 0), time(10, 0))
    ]
    rooms = ["Room 1", "Room 2"]
    lessons = [
        Lesson(1, "Math", "Mr. Smith", "Group A"),
        Lesson(2, "English", "Mrs. Johnson", "Group B")
    ]
    return TimeTable(timeslots, rooms, lessons)

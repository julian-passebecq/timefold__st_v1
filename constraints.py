from domain import Lesson
from timefold.solver.score import (Joiners, HardSoftScore, ConstraintFactory, Constraint, constraint_provider)

@constraint_provider
def define_constraints(constraint_factory: ConstraintFactory) -> list[Constraint]:
    return [
        room_conflict(constraint_factory)
    ]

def room_conflict(constraint_factory: ConstraintFactory) -> Constraint:
    return (
        constraint_factory.for_each_unique_pair(Lesson,
                Joiners.equal(lambda lesson: lesson.timeslot),
                Joiners.equal(lambda lesson: lesson.room))
            .penalize(HardSoftScore.ONE_HARD)
            .as_constraint("Room conflict")
    )

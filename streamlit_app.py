import streamlit as st
from timefold.solver import SolverFactory
from timefold.solver.config import SolverConfig, TerminationConfig, ScoreDirectorFactoryConfig, Duration
from domain import TimeTable, Lesson, generate_problem
from constraints import define_constraints

st.title("Timefold Solver Test")

if st.button("Run Solver"):
    try:
        solver_config = SolverConfig(
            solution_class=TimeTable,
            entity_class_list=[Lesson],
            score_director_factory_config=ScoreDirectorFactoryConfig(
                constraint_provider_function=define_constraints
            ),
            termination_config=TerminationConfig(
                spent_limit=Duration(seconds=30)
            )
        )

        solver = SolverFactory.create(solver_config).build_solver()
        solution = solver.solve(generate_problem())
        st.write("Solution found:")
        st.write(solution)
    except Exception as e:
        st.error(f"Error during solving: {str(e)}")
        st.write("Detailed error information:")
        st.write(e)

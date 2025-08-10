from student_table import StudentTable
import pytest


db = StudentTable("postgresql://postgres:s9141525990@localhost:5432/postgres")


@pytest.fixture(scope='session')
def area():
    use_db = {}
    use_db.clear()
    yield db
    use_db.clear()


def test_add_entity():
    user_id = "15051981"
    level = "Elementary"
    education_form = "group"
    subject_id = "1"
    db.add_student(user_id, level, education_form, subject_id)
    students = db.check_by_id(user_id)

    for student in students:
        assert student['user_id'] == int(user_id)


def test_edit_entity():
    user_id = "15051981"
    level = "Beginner"
    education_form = "group"
    subject_id = "1"
    where_id = "15051981"
    db.edit_student(user_id, level, education_form, subject_id, where_id)
    students = db.check_by_id(user_id)

    for student in students:
        assert student['level'] == level


def test_delete_entity():
    user_id = "15051981"
    db.delete_student(user_id)
    students = db.check_by_id(user_id)

    assert students == []

from sqlalchemy import create_engine, text


class StudentTable:
    def __init__(self, connection_string):
        self.__conn = create_engine(connection_string)

# Добавление
    def add_student(self, user_id, level, education_form, subject_id):
        with self.__conn.connect() as connection:
            result = connection.execute(
                text(f"INSERT INTO student \
                    (user_id,\"level\", education_form, subject_id)\
                 VALUES \
                    ({user_id}, '{level}', '{education_form}', {subject_id})")
                )
            connection.commit()
        return result

# Изменение
    def edit_student(self, user_id, level, education_form, subject_id, id):
        with self.__conn.connect() as connection:
            result = connection.execute(
                text(f"UPDATE student SET user_id = {user_id},\
                \"level\" = '{level}', education_form = '{education_form}',\
                subject_id = {subject_id} WHERE user_id = '{id}'")
                )
            connection.commit()
        return result

# Удаление
    def delete_student(self, id):
        with self.__conn.connect() as connection:
            result = connection.execute(
                text(f"DELETE FROM student WHERE user_id = '{id}'")
                )
            connection.commit()
            return result

# Получение спсика
    def check_by_id(self, id):
        with self.__conn.connect() as connection:
            result = connection.execute(
                text(f"SELECT * FROM student WHERE user_id = '{id}'")
            )
        return result.mappings().all()

import pyodbc


class GlobalStatic(object):
    d_id = None

    @staticmethod
    def set_doctor_id(d_id):
        GlobalStatic.d_id = d_id

        print(f"Set id to: {GlobalStatic.d_id}")


class DbConnector(object):
    connection = None

    @staticmethod
    def get_connection():
        if not DbConnector.connection:
            DbConnector.connection = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server=DESKTOP-EAC2CGC\KAUSHIK;"
                "Database=forensic;"
                "Trusted_Connection=yes;"
            )

        return DbConnector.connection









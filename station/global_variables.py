import pyodbc


class GlobalStatic(object):
    pst_id = None
    hospital_id = None
    p_id = None

    case_info_tuple = None
    evi_upd_info_tuple = None
    doc_info_tuple = None

    case_evidence_tuple = None
    evidence_tuple = None

    test_static = False

    @staticmethod
    def set_static_test():
        GlobalStatic.test_static = True

    @staticmethod
    def set_case_evidence_tuple(evidence_tuple):
        GlobalStatic.case_evidence_tuple = evidence_tuple
        print(f"Setting case evidence: {GlobalStatic.case_evidence_tuple}")

    @staticmethod
    def set_evidence_tuple(doc_evidence_tuple):
        print(f"Setting case evidence: {doc_evidence_tuple}")
        GlobalStatic.evidence_tuple = doc_evidence_tuple

    @staticmethod
    def set_evi_upd_info(evi_upd_info_tuple):
        print(f"Setting case info tuple: {evi_upd_info_tuple}")
        GlobalStatic.evi_upd_info_tuple = evi_upd_info_tuple

    @staticmethod
    def set_doc_info(doc_info_tuple):
        print(f"Setting case into tuple: {doc_info_tuple}")
        GlobalStatic.doc_info_tuple = doc_info_tuple

    @staticmethod
    def set_case_info(case_info_tuple):
        print(f"Setting case into tuple: {case_info_tuple}")
        GlobalStatic.case_info_tuple = case_info_tuple

    @staticmethod
    def set_police_station_id(pst_id):
        GlobalStatic.pst_id = pst_id

        print(f"Set id to: {GlobalStatic.pst_id}")

    @staticmethod
    def set_hospital_id(h_id):
        GlobalStatic.hospital_id = h_id

        print(f"Set hospital id to: {GlobalStatic.hospital_id}")

    @staticmethod
    def set_police_id(p_id):
        GlobalStatic.p_id = p_id

        print(f"Set id to: {GlobalStatic.p_id}")

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

import pyodbc


class GlobalStatic(object):
    police_station_id = None
    hospital_id = None
    police_id = None
    # d_id = None

    assign_pid_tuple = None
    assign_did_tuple = None
    hospital_assign_did = None

    case_info_tuple = None
    evi_upd_info_tuple = None

    case_evidence_tuple = None
    evidence_tuple = None
    evi_evidence_doc_tuple =None
    set_delete_doc = None


    @staticmethod
    def set_delete_doc(set_delete_doc):
        GlobalStatic.set_delete_doc = set_delete_doc
        print(f"Setting evidence to : {set_delete_doc}")


    @staticmethod
    def set_evidence_doc(evidence_doc):
        GlobalStatic.evi_evidence_doc_tuple = evidence_doc
        print(f"Setting evidence to : {evidence_doc}")


    @staticmethod
    def set_evidence(evidence):
        GlobalStatic.evi_upd_info_tuple = evidence
        print(f"Setting evidence to : {evidence}")

    # @staticmethod
    # def set_policeCase_pid_tuple(policeCase_pid_tuple):
    #     GlobalStatic.police_case_pid_tuple = policeCase_pid_tuple
    #     print(f"Setting case evidence: {GlobalStatic.police_case_pid_tuple}")

    @staticmethod
    def set_assign_pid_tuple(assign_pid_tuple):
        GlobalStatic.assign_pid_tuple = assign_pid_tuple
        print(f"Setting case evidence: {GlobalStatic.assign_pid_tuple}")

    @staticmethod
    def set_hospital_assign_did_tuple(hospital_assign_did):
        GlobalStatic.hospital_assign_did = hospital_assign_did
        print(f"Setting case evidence: {GlobalStatic.hospital_assign_did}")

    @staticmethod
    def set_assign_did_tuple(assign_did_tuple):
        GlobalStatic.assign_did_tuple = assign_did_tuple
        print(f"Setting case evidence: {GlobalStatic.assign_did_tuple}")

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

    # @staticmethod
    # def set_doc_info(doc_info_tuple):
    #     print(f"Setting case into tuple: {doc_info_tuple}")
    #     GlobalStatic.doc_info_tuple = doc_info_tuple

    @staticmethod
    def set_case_info(case_info_tuple):
        print(f"Setting case into tuple: {case_info_tuple}")
        GlobalStatic.case_info_tuple = case_info_tuple

    @staticmethod
    def set_police_station_id(pst_id):
        GlobalStatic.police_station_id = pst_id

        print(f"Set id to: {GlobalStatic.police_station_id}")

    @staticmethod
    def set_hospital_id(h_id):
        GlobalStatic.hospital_id = h_id

        print(f"Set id to: {GlobalStatic.hospital_id}")

    @staticmethod
    def set_police_id(p_id):
        GlobalStatic.police_id = p_id

        print(f"Set id to: {GlobalStatic.police_id}")

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

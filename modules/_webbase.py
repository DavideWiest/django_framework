# from modules.stockdatamanager import StockDataManager
# from .db_structs import UserCol, StockCol, StocklistCol
from .mongomanager import MongoManager

from modules.ssecrets import PassManager, SecretOperator, DeploymentHelper
# from modules.mailoperator import MailOperator
# from modules.mailchimp import MailChimp


class Webbase():
    def __init__(self):
        self.dh = DeploymentHelper()
        self.run_settings, self.device_settings = self.dh.get_json_settings()
        self.so = SecretOperator()
        self.pm = PassManager()
        self.secrets = self.so.get_json_secrets()
        
        # self.mm = MongoManager(self.secrets["db"]["con_str"], self.secrets["db"]["db_name"])
        
        # self.usercol = UserCol(self.mm)
        # self.stockcol = StockCol(self.mm)
        # self.stocklistcol = StocklistCol(self.mm)

        # self.mo = MailOperator(self.secrets["mail"]["from_email"], self.secrets["mail"]["from_email_pass"], self.secrets["mail"]["smtp_server"], self.secrets["mail"]["smpt_port"], self.secrets["backup_mail"]["from_email"], self.secrets["backup_mail"]["from_email_pass"], self.secrets["backup_mail"]["smtp_server"], self.secrets["backup_mail"]["smpt_port"])
        
        # self.mc = MailChimp(self.secrets["mailchimp"]["api_key"], self.secrets["mailchimp"]["server"], self.secrets["mailchimp"]["primary_list_id"])

        # self.sm = StockDataManager(self.secrets["polygon"]["api_key"])

wb = Webbase()


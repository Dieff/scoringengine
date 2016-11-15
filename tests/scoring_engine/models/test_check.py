import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../scoring_engine'))

from models.check import Check
from models.round import Round
from db import DB

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
from helpers import generate_sample_model_tree


class TestCheck(object):
    def setup(self):
        self.db = DB()
        self.db.connect()
        self.db.setup()

    def teardown(self):
        self.db.destroy()

    def test_init_check(self):
        check = Check()
        assert check.id is None
        assert check.round is None
        assert check.round_id is None

    def test_basic_check(self):
        service = generate_sample_model_tree('Service', self.db)
        round_obj = Round(number=1)
        self.db.save(round_obj)
        check = Check(round=round_obj, service=service)
        self.db.save(check)
        assert check.id is not None
        assert check.round == round_obj
        assert check.round_id == round_obj.id
        assert check.service == service
        assert check.service_id == service.id
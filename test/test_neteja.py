# -*- coding: UTF-8 -*-

import netejahtml
import unittest
from test.testhelper import llegir_mail


class TestNeteja(unittest.TestCase):

    def test_treure_style(self):
        msg = llegir_mail("reply-mutipart-alternative.txt")
        html = msg.get_body()
        net = netejahtml.neteja_reply(html)
        self.assertFalse("text-decoration" in net)

    def test_treure_script(self):
        msg = llegir_mail("reply-mutipart-alternative.txt")
        html = msg.get_body()
        net = netejahtml.neteja_reply(html)
        self.assertFalse("alert" in net)

    def test_treure_comentaris(self):
        msg = llegir_mail("comentaris.txt")
        html = msg.get_body()
        net = netejahtml.neteja_nou(html)
        self.assertFalse("supportList" in net)
        
    def test_mail_accents(self):
        msg = llegir_mail("accents.txt")
        html = msg.get_body()
        net = netejahtml.neteja_nou(html)
        print(html)
        print(net)
        self.assertTrue("áccents vàris" in net)
        

if __name__ == '__main__':
    unittest.main()

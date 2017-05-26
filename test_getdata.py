import unittest

import os
import json

from getdata import *

class TestGetData(unittest.TestCase):
    def test_renvoi_un_JSON_valide(self):
        self.assertEqual(createJSON([100, 70, 20]), { "offreTotal": 100, "offreDev": 70, "offreDevJunior": 20 })
        self.assertEqual(createJSON([99, 69, 19]), { "offreTotal": 99, "offreDev": 69, "offreDevJunior": 19 })
    def test_un_fichier_est_cree(self):
        testFileName = 'truc.txt'
        if os.path.exists(testFileName):
            os.remove(testFileName)
        writeToJsonFile(testFileName, { "offreTotal": 99, "offreDev": 69, "offreDevJunior": 19 })
        self.assertEqual(True, os.path.exists(testFileName))

    def test_les_donnees_dans_le_fichier(self):
        testFileName = 'truc.json'
        if os.path.exists(testFileName):
            os.remove(testFileName)
        writeToJsonFile(testFileName, { "truc": 12 })
        with open(testFileName, "r") as f:
            self.assertEqual(json.load(f), {"truc": 12})



unittest.main()

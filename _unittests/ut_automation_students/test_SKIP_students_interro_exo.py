"""
@brief      test log(time=2s)
"""
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version, ExtTestCase, skipif_circleci


class TestInterroExo(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    @skipif_circleci("produces a segmentation fault")
    def test_interro_motif(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from ensae_teaching_cs.automation_students.interro_motif import execute_python_scripts, _get_code
        code = _get_code(b"aa.bb@ensae-paristech.fr")
        self.assertEqual(code, 51)

        temp = get_temp_folder(__file__, "temp_interro_motif")
        data = os.path.join(temp, "..", "projects", "exo_1A_2016.xlsx")
        root = os.path.join(temp, "..", "projects")
        input = pandas.read_excel(data, engine='openpyxl')
        url = "http://www.xavierdupre.fr/enseignement/examens/1A_2016/enonce_{0}.txt"
        col_names = dict(folder="nom_prenom", mail="nom_prenom")
        df = execute_python_scripts(
            root, input, col_names=col_names, url=url, fLOG=fLOG, eol="/")
        out = os.path.join(temp, "results.xlsx")
        df.to_excel(out)
        self.assertExists(out)


if __name__ == "__main__":
    unittest.main()

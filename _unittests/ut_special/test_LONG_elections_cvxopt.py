# -*- coding: utf-8 -*-
"""
@brief      test log(time=180s)
"""
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG, unzip
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from ensae_teaching_cs.special.elections import ElectionResults


class TestElections(unittest.TestCase):

    def test_loading_elections_2012(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.split(__file__)[0])
        file = os.path.join(path, "data", "election_2012.xls")
        if not os.path.exists(file):
            temp = get_temp_folder(__file__, "temp_loading_elections_2012")
            zip_ = os.path.join(path, "data", "elections.zip")
            unzip(zip_, temp)
            file = os.path.join(temp, "election_2012.xlsx")
        assert os.path.exists(file)

        if is_travis_or_appveyor() == "travis":
            warnings.warn(
                "The test cannot read an excel file using xlrd. Disabling it.")
            return

        el = ElectionResults(year=2012, file=file)
        fLOG(el.get_candidates_votes(0))
        el.correct("cand")
        fLOG(el.get_candidates_votes(0))
        fLOG(sum(el.get_people(0)), sum(el.get_people(1)))

        more_debug = False
        if more_debug:
            fLOG("----")
            tbl = el.T0.head().copy()
            tbl["total"] = tbl.apply(lambda row: sum(
                [row[_] for _ in el.T0.columns if _ not in el.LevelCol]), axis=1)
            fLOG(tbl.to_html(float_format=lambda x: "%d" %
                             x, force_unicode=True, index=False))
            fLOG("----")
            tbl = el.T1.head().copy()
            tbl["total"] = tbl.apply(lambda row: sum(
                [row[_] for _ in el.T1.columns if _ not in el.LevelCol]), axis=1)
            fLOG(tbl.to_html(float_format=lambda x: "%d" %
                             x, force_unicode=True, index=False))
            fLOG("----")
        res = el.vote_transfer()
        fLOG(res)

        def pour(x):
            if x < 0.01:
                return ""
            else:
                return f"{x * 100:3.0f}" + "%"

        def pour2(x):
            if x < 0.01:
                return "0%"
            else:
                return f"{x * 100:3.0f}" + "%"

        def agg(x):
            if x[0] == x[1]:
                if x[0] == "0%":
                    return ""
                else:
                    return x[0]
            else:
                return "%s-%s" % tuple(x)

        boot = el.bootstrap(iter=10, fLOG=fLOG)
        comb = el.combine_into_string([boot[2], boot[3]], pour2, agg)
        fLOG(comb)
        assert len(comb) > 0

        fLOG(res.to_html(float_format=pour, index=True))
        fLOG(comb.to_html(index=True))

    def test_loading_elections_2007(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.split(__file__)[0])

        if is_travis_or_appveyor() == "travis":
            warnings.warn(
                "The test cannot read an excel file using xlrd. Disabling it.")
            return

        file = os.path.join(path, "data", "election_2007.xls")
        if not os.path.exists(file):
            temp = get_temp_folder(__file__, "temp_loading_elections_2007")
            zip_ = os.path.join(path, "data", "elections.zip")
            unzip(zip_, temp)
            file = os.path.join(temp, "election_2007.xlsx")
        assert os.path.exists(file)

        el = ElectionResults(year=2007, file=file)
        res = el.vote_transfer()
        fLOG(res)
        assert len(res) > 0

    def test_read_all_elections(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(path, "temp_read_all_elections")
        if not os.path.exists(temp):
            os.mkdir(temp)
        if is_travis_or_appveyor() == "travis":
            warnings.warn(
                "The test cannot read an excel file using xlrd. Disabling it.")
            return
        for year in [2012, 2002, 2007]:
            for level in ["Départements", "Cantons", ]:
                fLOG("******reading ", year, level)
                file = os.path.join(path, "data", "election_%d.xlsx" % year)
                if not os.path.exists(file):
                    file = os.path.join(temp, "election_%d.xlsx" % year)
                if not os.path.exists(file):
                    zip_ = os.path.join(path, "data", "elections.zip")
                    unzip(zip_, temp)
                    file = os.path.join(temp, "election_%d.xlsx" % year)
                assert os.path.exists(file)

                el = ElectionResults(year=year, file=file, level=level)
                fLOG("saving")
                xls = os.path.join(temp, "out_%d_%s_0.xlsx" % (year, level))
                el.T0.to_excel(xls)
                xls = os.path.join(temp, "out_%d_%s_1.xlsx" % (year, level))
                el.T1.to_excel(xls)
                res = el.vote_transfer()
                fLOG(res)


if __name__ == "__main__":
    unittest.main()

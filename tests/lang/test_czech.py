# -*- coding: utf-8 -*-
import pytest

GOLDEN_CS_RULES_TEST_CASES = [
    ("Jde o majite firmy ABTrade s. r. o., kteří stojí i za dalšími společnostmi, např. XYZCorp a.s.",
     ["Jde o majite firmy ABTrade s. r. o., kteří stojí i za dalšími společnostmi, např. XYZCorp a.s."]),
    ("„Průzkumy beru na lehkou váhu. V podstatě mě to nezajímá,“ reagoval Zeman na průzkum agentury Focus.",
     ["„Průzkumy beru na lehkou váhu. V podstatě mě to nezajímá,“ reagoval Zeman na průzkum agentury Focus."]),
    ("Toto se mi podařilo až na 10. pokus, ale stálo to za to.",
     ["Toto se mi podařilo až na 10. pokus, ale stálo to za to."]),
    ("Jde o príslušníky XII. Pluku speciálního nasazení.",
     ["Jde o príslušníky XII. Pluku speciálního nasazení."]),
    ("Společnost byla založena 7. dubna 2020, na smlouvě však figuruje datum 20. březen 2020.",
     ["Společnost byla založena 7. dubna 2020, na smlouvě však figuruje datum 20. březen 2020."]),
]


@pytest.mark.parametrize('text,expected_sents', GOLDEN_CS_RULES_TEST_CASES)
def test_cs_sbd(cs_default_fixture, text, expected_sents):
    """Czech language SBD tests"""
    segments = cs_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents

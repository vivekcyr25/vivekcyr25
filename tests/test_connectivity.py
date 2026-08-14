"""
Unit tests for scripts/build_connectivity.py SVG banner and card generators.
"""

import xml.etree.ElementTree as ET
from scripts.build_connectivity import (
    CARDS,
    LINK_MAP,
    LOGOS,
    build_combined_banner_svg,
    build_single_card_svg,
    img_tag,
)


class TestConnectivitySVG:

    def test_img_tag_formatting(self):
        tag = img_tag("dGVzdA==", 10.5, 20.0, 34.0)
        assert 'x="10.5"' in tag
        assert 'y="20.0"' in tag
        assert 'width="34.0"' in tag
        assert 'href="data:image/svg+xml;base64,dGVzdA=="' in tag

    def test_cards_and_links_defined(self):
        assert len(CARDS) == 6
        assert len(LINK_MAP) >= 6
        for card in CARDS:
            key = card[5]
            assert key in LOGOS
            assert key in LINK_MAP

    def test_build_combined_banner_svg_validity(self):
        banner_svg = build_combined_banner_svg()
        assert "<svg" in banner_svg
        assert 'viewBox="0 0 900 100"' in banner_svg
        assert "LinkedIn" in banner_svg
        assert "GitHub" in banner_svg
        assert "ORCID" in banner_svg
        # Verify XML parsability
        root = ET.fromstring(banner_svg)
        assert root.tag.endswith("svg")

    def test_build_single_card_svg_validity(self):
        card_tuple = CARDS[0]
        card_svg = build_single_card_svg(card_tuple)
        assert "<svg" in card_svg
        assert 'viewBox="0 0 142 92"' in card_svg
        assert "LinkedIn" in card_svg
        root = ET.fromstring(card_svg)
        assert root.tag.endswith("svg")

"""Test my garden functions."""


__author__ = "730669462"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date
"""Importing functions."""


def test_add_by_kind_edge_case():
    """Test add_by_kind with an empty dictionary and new plant kind."""
    plants_by_kind = {}
    plant_kind = "flower"
    plant_type = "tupil"
    add_by_kind(plants_by_kind, plant_kind, plant_type)
    assert plants_by_kind == {"flowers": ["tulip"]}


def test_add_by_kind_use_case():
    """Test add_by_kind with an empty dictionary and new plant kind."""
    plants_by_kind = {}
    plant_kind = "flower"
    plant_type = "sunflower"
    add_by_kind(plants_by_kind, plant_kind, plant_type)
    assert plants_by_kind == {"flowers": ["rose", "sunflower"]}


def test_add_by_date_edge_case():
    """Test add_by_date with an empty dictionary and new month."""
    plants_by_date = {}
    plant_date = "March"
    plant_time = "carrot"
    add_by_date(plants_by_date, plant_date, plant_time)
    assert plants_by_date == {"March": ["carrot"]}


def test_add_by_date_use_case():
    """Test add_by_date with existing month."""
    plants_by_date = {"March": ["carrot"]}
    plant_date = "March"
    plant_time = "celery"    
    add_by_date(plants_by_date, plant_date, plant_time)
    assert plants_by_date == {"March": ["carrot", "celery"]}


def test_lookup_by_kind_and_date_edge_case():
    """Test lookup_by_kind_and_date with empty dictionaries."""
    plants_by_kind = {"Vegetable": ["celery"]}
    plants_by_date = {"March": ["tulip", "corn"]}
    plant_kind = "Flower"
    plant_date = "April"
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, plant_date)
    expected = f"No {plant_kind}s to plant in {plant_date}."
    assert result == expected


def test_lookup_by_kind_and_date_use_case():
    """Test lookup_by_kind_and_date with existing data."""
    plants_by_kind = {"Vegetable": ["celery"], "flowers": ["rose", "sunflower"]}
    plants_by_date = {"March": ["tulip", "corn"], "June": ["carrot", "sunflower"]}
    plant_kind = "Flower"
    plant_date = "April"
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, plant_date)
    expected = f"No {plant_kind}s to plant in {plant_date}."
    assert result == expected

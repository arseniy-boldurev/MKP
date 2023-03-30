import pytest
import tempfile
import os
from main import population_change

@pytest.fixture
def population_file():
    data = 'Ukraine, 2020, 45415596\nUkraine, 2010, 42343326\nUnited States, 2020, 309348193\nUnited States, 2010, 331002651\n'
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(data)
        f.close()
        yield f.name
        os.unlink(f.name)
def test_population_change(population_file):
    expected = {
        'Ukraine': [(2010, 2020, 3072270)],
        'United States': [(2010, 2020, -21654458)]
    }
    assert population_change(population_file) == expected

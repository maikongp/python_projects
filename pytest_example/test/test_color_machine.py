import pytest
import source.color_machine as cm

@pytest.fixture(autouse=True)
def color_machine():
    return cm.ColorMachine()

class TestColorMachine():      

    def test_create_secondary_color_not_from_primary_color(self, color_machine):

        assert color_machine.create_secondary_color(["white", "blue"]) == "white is not a primary color"

    def test_create_secondary_with_only_one_primary_color(self, color_machine):

        assert color_machine.create_secondary_color(["blue"]) == "A secondary color is made by two primary colors"

    @pytest.mark.parametrize("primary_colors, secondary_color", 
                             [(["red", "yellow"], "orange"),
                              (["yellow", "blue"], "green"),
                              (["red", "blue"], "purple")])
    def test_create_secondary_color_successfully(self, color_machine, primary_colors, secondary_color):
        assert color_machine.create_secondary_color(primary_colors) == secondary_color


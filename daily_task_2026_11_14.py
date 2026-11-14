"""Daily OOP Task - 14 November 2026: Community Garden Manager.

Manage garden plots, register plants, track harvests and calculate totals.
Concepts: encapsulation, composition, properties, validation and date handling.
"""

from datetime import date
import math


class Plant:
    """Represent one plant and protect its harvest status."""

    def __init__(self, plant_id, name, planted_on):
        if not isinstance(plant_id, str) or not plant_id.strip():
            raise ValueError("Plant ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Plant name cannot be empty.")

        try:
            parsed_date = date.fromisoformat(planted_on)
        except (TypeError, ValueError):
            raise ValueError("Planting date must use YYYY-MM-DD format.") from None
        if parsed_date > date.today():
            raise ValueError("Planting date cannot be in the future.")

        self.plant_id = plant_id.strip().upper()
        self.name = name.strip().title()
        self.planted_on = parsed_date
        self.__harvested = False

    @property
    def harvested(self):
        """Read-only harvest status."""
        return self.__harvested

    @property
    def growing_days(self):
        """Return the number of days since planting."""
        end_date = date.today()
        return (end_date - self.planted_on).days

    def mark_harvested(self):
        if self.__harvested:
            raise ValueError("This plant has already been harvested.")
        self.__harvested = True

    def display(self):
        status = "Harvested" if self.harvested else "Growing"
        print(
            f"{self.plant_id} | {self.name} | {status} | "
            f"{self.growing_days} days in the garden"
        )


class GardenPlot:
    """A plot owns and manages its Plant objects (composition)."""

    def __init__(self, plot_id, area_sq_m):
        if not isinstance(plot_id, str) or not plot_id.strip():
            raise ValueError("Plot ID cannot be empty.")
        if isinstance(area_sq_m, bool) or not isinstance(area_sq_m, (int, float)):
            raise TypeError("Plot area must be a number.")
        if not math.isfinite(area_sq_m) or area_sq_m <= 0:
            raise ValueError("Plot area must be finite and greater than zero.")

        self.plot_id = plot_id.strip().upper()
        self.area_sq_m = float(area_sq_m)
        self.__plants = {}

    def add_plant(self, plant):
        if not isinstance(plant, Plant):
            raise TypeError("Only Plant objects can be added.")
        if plant.plant_id in self.__plants:
            raise ValueError("A plant with this ID already exists in the plot.")
        self.__plants[plant.plant_id] = plant

    def find_plant(self, plant_id):
        if not isinstance(plant_id, str) or not plant_id.strip():
            raise ValueError("Plant ID cannot be empty.")
        return self.__plants.get(plant_id.strip().upper())

    def harvest_plant(self, plant_id):
        plant = self.find_plant(plant_id)
        if plant is None:
            raise LookupError("Plant was not found in this plot.")
        plant.mark_harvested()

    @property
    def total_plants(self):
        return len(self.__plants)

    @property
    def harvested_count(self):
        return sum(plant.harvested for plant in self.__plants.values())

    @property
    def growing_count(self):
        return self.total_plants - self.harvested_count

    def show_report(self):
        print(f"\n--- Garden Plot {self.plot_id} ({self.area_sq_m:.1f} sq. m.) ---")
        if not self.__plants:
            print("No plants registered.")
            return
        for plant in self.__plants.values():
            plant.display()
        print(
            f"Total: {self.total_plants} | Growing: {self.growing_count} | "
            f"Harvested: {self.harvested_count}"
        )


class GardenManager:
    """Manage multiple plots and produce a garden-wide summary."""

    def __init__(self, garden_name):
        if not isinstance(garden_name, str) or not garden_name.strip():
            raise ValueError("Garden name cannot be empty.")
        self.garden_name = garden_name.strip()
        self.__plots = {}

    def add_plot(self, plot):
        if not isinstance(plot, GardenPlot):
            raise TypeError("Only GardenPlot objects can be registered.")
        if plot.plot_id in self.__plots:
            raise ValueError("A plot with this ID already exists.")
        self.__plots[plot.plot_id] = plot

    def find_plot(self, plot_id):
        if not isinstance(plot_id, str) or not plot_id.strip():
            raise ValueError("Plot ID cannot be empty.")
        return self.__plots.get(plot_id.strip().upper())

    def show_garden_report(self):
        print(f"\n===== {self.garden_name} =====")
        for plot in self.__plots.values():
            plot.show_report()
        total = sum(plot.total_plants for plot in self.__plots.values())
        harvested = sum(plot.harvested_count for plot in self.__plots.values())
        print(f"\nGarden total: {total} plants | {harvested} harvested")


def main():
    garden = GardenManager("Green Corner Community Garden")

    vegetable_plot = GardenPlot("P01", 12)
    herb_plot = GardenPlot("P02", 6)

    vegetable_plot.add_plant(Plant("V101", "Tomato", "2026-10-01"))
    vegetable_plot.add_plant(Plant("V102", "Chilli", "2026-10-05"))
    herb_plot.add_plant(Plant("H201", "Mint", "2026-10-10"))

    garden.add_plot(vegetable_plot)
    garden.add_plot(herb_plot)

    vegetable_plot.harvest_plant("V101")
    garden.show_garden_report()

    found = garden.find_plot("p01").find_plant("v102")
    print(f"\nSearch result: {found.name if found else 'Not found'}")

    # Check duplicate IDs and invalid data.
    try:
        vegetable_plot.add_plant(Plant("V102", "Extra Chilli", "2026-10-12"))
    except ValueError as error:
        print("Duplicate check passed:", error)

    try:
        GardenPlot("P03", 0)
    except ValueError as error:
        print("Area validation passed:", error)

    try:
        vegetable_plot.harvest_plant("V101")
    except ValueError as error:
        print("Harvest validation passed:", error)

    assert garden.find_plot("P02").total_plants == 1
    assert vegetable_plot.harvested_count == 1
    assert vegetable_plot.growing_count == 1
    assert garden.find_plot("missing") is None
    print("\nAll community garden checks passed successfully.")


if __name__ == "__main__":
    main()

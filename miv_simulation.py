import math
import random

# Constants for the simulation
EARTH_TO_MARS_DISTANCE = 225e6  # Distance in kilometers
MARS_GRAVITY = 3.71  # Gravity in m/s^2


class MagneticGenerator:
    """Generates energy using Faraday's Law."""

    def __init__(self, coil_turns: int, magnetic_field_strength: float, velocity: float) -> None:
        self.coil_turns = coil_turns  # Number of turns in the coil
        self.magnetic_field_strength = magnetic_field_strength  # Strength of the magnetic field in Tesla
        self.velocity = velocity  # Speed of the MiV through the magnetic field

    def generate_energy(self) -> float:
        """Generate energy based on a simplified Faraday's law."""
        flux_change = self.magnetic_field_strength * self.velocity  # Simplified for demonstration
        energy_generated = self.coil_turns * flux_change
        return max(0.0, energy_generated)  # Energy cannot be negative


class HydrogenReactor:
    """Water-lithium hydrogen reactor for energy production."""

    def __init__(self, water_supply: float, lithium_supply: float) -> None:
        self.water_supply = water_supply
        self.lithium_supply = lithium_supply

    def produce_hydrogen(self) -> float:
        """Simulates hydrogen production using water and lithium for plasma propulsion."""
        if self.water_supply > 0 and self.lithium_supply > 0:
            hydrogen_produced = min(self.water_supply, self.lithium_supply) * random.uniform(0.5, 1.0)
            self.water_supply -= hydrogen_produced
            self.lithium_supply -= hydrogen_produced
            return hydrogen_produced
        print("Reactor supplies depleted.")
        return 0.0


class PlasmaPropulsion:
    """Plasma propulsion system that consumes hydrogen fuel."""

    def __init__(self, hydrogen_fuel: float) -> None:
        self.hydrogen_fuel = hydrogen_fuel

    def use_plasma(self, mode: str = "hot") -> float:
        """Uses hydrogen fuel to create thrust with hot or cold plasma."""
        if self.hydrogen_fuel <= 0:
            print("No hydrogen fuel left for plasma propulsion.")
            return 0.0

        fuel_multiplier = 1.0 if mode == "hot" else 0.5
        plasma_usage = self.hydrogen_fuel * fuel_multiplier
        self.hydrogen_fuel -= plasma_usage
        thrust = plasma_usage * 1000  # Arbitrary thrust value
        print(f"Generated {thrust:.0f} N of thrust using {mode} plasma.")
        return thrust


class PlasmaVortex:
    """Plasma vortex for neutralizing gravitational effects."""

    def __init__(self, strength: float) -> None:
        self.strength = strength

    def generate_free_fall(self, local_gravity: float) -> float:
        """Generate a free-fall zone by neutralizing gravitational effects."""
        return max(0.0, local_gravity - self.strength)


class NavigationSystem:
    """Navigation system that leverages plasma vortices to reach fixed points."""

    def __init__(self, position: tuple[float, float, float] | None = None) -> None:
        if position is None:
            position = (0.0, 0.0, 0.0)
        self.position = position

    def navigate_to_fixed_position(
        self,
        target_position: tuple[float, float, float],
        plasma_vortex: PlasmaVortex,
        available_energy: float | None = None,
    ) -> float | None:
        """Use plasma vortex to neutralize gravitational fields and navigate.

        Returns the energy required when the maneuver is feasible. If available energy
        is supplied and insufficient, returns ``None`` and leaves position unchanged.
        """
        local_gravity = random.uniform(0.5, 2.0)  # Simulated local gravity (m/s^2)
        adjusted_gravity = plasma_vortex.generate_free_fall(local_gravity)
        print(f"Adjusted gravity after plasma vortex: {adjusted_gravity:.2f} m/s^2.")

        distance = math.sqrt(sum((self.position[i] - target_position[i]) ** 2 for i in range(3)))
        print(f"Distance to target position: {distance:.2f} km.")

        energy_required = distance * random.uniform(0.5, 1.5)  # Arbitrary energy requirement
        print(f"Energy required for fixed position navigation: {energy_required:.2f} units.")

        if available_energy is not None and energy_required > available_energy:
            print("Insufficient energy for fixed position navigation. Jump aborted.")
            return None

        self.position = target_position
        return energy_required


class MiV:
    """Simulation of the MiV integrating all subsystems."""

    def __init__(self) -> None:
        self.mass = 1000  # Mass of the MiV in arbitrary units
        self.energy_level = 10000  # Initial energy level

        # System components
        self.generator = MagneticGenerator(coil_turns=37, magnetic_field_strength=0.5, velocity=20)
        self.reactor = HydrogenReactor(water_supply=100, lithium_supply=50)
        self.propulsion = PlasmaPropulsion(hydrogen_fuel=0)
        self.navigation = NavigationSystem()
        self.plasma_vortex = PlasmaVortex(strength=10)

    def simulate_jump_to_mars(self, target_position: tuple[float, float, float]) -> bool:
        """Simulate the MiV making a space-time jump using the subsystems."""
        print("Starting space-time jump to Mars...")

        # Step 1: Generate additional energy using magnetic vortex and Faraday induction
        energy_generated = self.generator.generate_energy()
        self.energy_level += energy_generated
        print(f"Generated {energy_generated:.2f} units of energy. Current energy level: {self.energy_level:.2f}.")

        # Step 2: Use reactor to produce hydrogen for plasma propulsion
        hydrogen_produced = self.reactor.produce_hydrogen()
        self.propulsion.hydrogen_fuel += hydrogen_produced
        print(f"Produced {hydrogen_produced:.2f} units of hydrogen fuel.")

        # Step 3: Navigate to the target position (Mars) using plasma vortex and magnetic navigation
        energy_used = self.navigation.navigate_to_fixed_position(
            target_position,
            self.plasma_vortex,
            available_energy=self.energy_level,
        )
        if energy_used is None:
            print(f"Energy level remains at: {self.energy_level:.2f}.")
            return False

        self.energy_level -= energy_used
        print(f"Energy level after navigation: {self.energy_level:.2f}.")

        # Step 4: Use plasma propulsion to finalize the jump
        self.propulsion.use_plasma("hot")
        print("Space-time jump to Mars completed.")
        return True


def run_simulation() -> None:
    """Run a single MiV jump simulation to a random Mars coordinate."""
    target_position = (
        random.uniform(100_000, 500_000),
        random.uniform(100_000, 500_000),
        random.uniform(100_000, 500_000),
    )
    miv = MiV()
    miv.simulate_jump_to_mars(target_position)


if __name__ == "__main__":
    run_simulation()

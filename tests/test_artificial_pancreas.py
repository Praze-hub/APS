import pytest
from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixture
def system():
    return ArtificialPancreasSystem(glucose_level=100, insulin_sensitivity=1.0)

def test_glucose_increases_after_meal(system):
    before = system.glucose_level
    system.meal(30)
    after = system.glucose_level
    assert after > before, "Glucose should increase after eating carbs"
    expected_increase = 30 * system.GLUCOSE_PER_CARB
    assert pytest.approx(before + expected_increase, rel=1e-6) == after

def test_glucose_decreases_after_exercise(system):
    system.glucose_level = 140
    before = system.glucose_level
    system.exercise(20)
    after = system.glucose_level
    assert after < before, "Glucose should decrease after exercise"
    expected_decrease = 20 * system.GLUCOSE_BURN_PER_MIN
    if before - expected_decrease >= 50:
        assert pytest.approx(before - expected_decrease, rel=1e-6) == after
        
    else:
        assert after == 50
    

@pytest.mark.parametrize(
    "start_glucose, expected_action",
    [
        (160, "deliver insulin"),
        (30, "warn_low_glucose"),
        (100, "maintain"),
    ],
)

def test_predict_action_various(start_glucose, expected_action):
    aps = ArtificialPancreasSystem(glucose_level=start_glucose, insulin_sensitivity=1.0, target_glucose=100, tolerance=10)
    action, new_level = aps.predict_action()
    assert action == expected_action

def test_glucose_never_below_minimum(system):
    system.glucose_level = 60
    system.exercise(1000)
    assert system.glucose_level >= 50, "Glucose must not drop below 50"
    
def test_multiple_sequential_events():
    aps = ArtificialPancreasSystem(glucose_level=90, insulin_sensitivity=2.0, target_glucose=100, tolerance=5)
    aps.meal(30)
    after_meal = aps.glucose_level
    assert after_meal > 90
    
    aps.exercise(10)
    after_ex = aps.glucose_level
    
    action, after_action = aps.predict_action()
    assert action in ("deliver insulin", "maintain", "warn_low_glucose")
    
    assert pytest.approx(aps.glucose_level, rel=1e-6) == after_action
    
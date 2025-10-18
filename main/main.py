from artificial_pancreas import ArtificialPancreasSystem  

def main():
    aps = ArtificialPancreasSystem(glucose_level=120, insulin_sensitivity=1.5)

    # Simulate a meal
    aps.meal(50)  

    # Simulate exercise
    aps.exercise(30)  

    # Predict what the system should do next
    action, level = aps.predict_action()
    print(f"\nFinal Action: {action}, Final Glucose Level: {level:.2f}")

if __name__ == "__main__":
    main()

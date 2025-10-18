class ArtificialPancreasSystem:
    """Simplified model for data-driven glucose regulation"""
    
    GLUCOSE_PER_CARB = 0.5 #fixed incease per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise
    
    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
    
    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        glucose_up = carbs * self.GLUCOSE_PER_CARB
        self.glucose_level += glucose_up
        print(f"Meal: {carbs}g carbs, Glucose increased by {glucose_up:.2f} to New level: {self.glucose_level:.2f}")

    
    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""
        glucose_down = duration * self.GLUCOSE_BURN_PER_MIN
        self.glucose_level -= glucose_down
        
        # prevent glucose from dropping too low
        if self.glucose_level < 50:
            self.glucose_level = 50
            
        print(f"Exercise: {duration}mins , Glucose decreased by {glucose_down:.2f} to New level: {self.glucose_level:.2f}")

            
    
    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        lower_limit = self.target_glucose - self.tolerance
        upper_limit = self.target_glucose + self.tolerance
        
        #Case 1: When the glucose is too high
        if self.glucose_level > upper_limit:
            excess = self.glucose_level - self.target_glucose
            insulin_dose = excess / self.insulin_sensitivity
            self.glucose_level -= insulin_dose
            action = "deliver insulin"
            print(f"Glucose is high: {self.glucose_level + insulin_dose:.2f}, Delivered insulin dose {insulin_dose:.2f}, New level: {self.glucose_level:.2f}")
            
        #Case 2: When glucose level is low 
        elif self.glucose_level < lower_limit:
            action = "warn_low_glucose"
            print(f"Glucose low: {self.glucose_level:.2f}, Warning issued!")
            
        # Case 3: Glucose normal
        else:
            action = "maintain"
            print(f"Glucose stable at {self.glucose_level:.2f}, No action needed.")
            
        return action, self.glucose_level


            
            
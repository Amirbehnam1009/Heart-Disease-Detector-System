def inferenceRules(sex, age, chest_pain, blood_pressure, cholesterol, blood_sugar, heart_rate):

    output_sick4 = 0
    output_sick3 = 0
    output_sick2 = 0
    output_sick1 = 0
    output_healthy = 0

    output_sick4 = max(
        output_sick4,
        min(age["very_old"], chest_pain["atypical_anginal"]),
        min(heart_rate["high"], age["old"]),
        chest_pain["asymptomatic"],
        blood_pressure["very_high"],
        cholesterol['very_high'],
        heart_rate["high"],
        age["very_old"]
    )

    output_sick3 = max(
        output_sick3,
        min(sex["male"], heart_rate["medium"]),
        min(chest_pain["non_anginal_pain"], blood_pressure["high"]),
        min(blood_sugar["true"], age["mild"]),
        chest_pain["asymptomatic"],
        blood_pressure["high"],
        cholesterol["high"],
        age["old"],
        heart_rate["high"]
    )
    
    output_sick2 = max(
        output_sick2,
        min(sex["female"], heart_rate["medium"]),
        min(chest_pain["typical_anginal"], heart_rate["medium"]),
        min(blood_sugar["false"], blood_pressure["very_high"]),
        chest_pain["non_anginal_pain"],
        sex["male"],
        blood_pressure["high"],
        cholesterol["high"],
        age["old"],
        blood_sugar["true"],
        heart_rate["medium"]
    )
    
    output_sick1 = max(
        output_sick1,
        max(chest_pain["asymptomatic"], age["very_old"]),
        max(blood_pressure["high"], heart_rate["low"]),
        chest_pain["atypical_anginal"],
        sex["female"],
        cholesterol["medium"],
        blood_pressure["medium"],
        heart_rate["medium"],
        age["mild"]
    )
    
    output_healthy = max(
        output_healthy,
        chest_pain["typical_anginal"],
        blood_pressure["low"],
        cholesterol['low'],
        heart_rate["low"],
        age['young']
    )
    return output_healthy, output_sick1, output_sick2, output_sick3, output_sick4
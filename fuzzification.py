# AGE
def age(x):
    age_levels = {
        'young': max(0, min(1, (38 - x) / 9 if x <= 29 else 0)),
        'mild': max(0, min((x - 33) / 5, (45 - x) / 7) if 33 <= x < 45 else 0),
        'old': max(0, min((x - 40) / 8, (58 - x) / 10) if 40 <= x < 58 else 0),
        'very_old': max(0, min((x - 52) / 8, 1) if 52 <= x else 0)
    }
 
    return age_levels

# CHOLESTEROL
def cholesterol(x):
    cholesterol_levels = {
        'low': max(0, min(1, (197 - x) / 46 if x < 151 else 0)),
        'medium': max(0, min((x - 188) / 27, (250 - x) / 35) if 188 <= x < 250 else 0),
        'high': max(0, min((x - 217) / 46, (307 - x) / 44) if 217 <= x < 307 else 0),
        'very_high': max(0, min((x - 281) / 66, 1) if 281 <= x else 0)
    }
    
    return cholesterol_levels

# HEART RATE
def heart_rate(x):
    heart_rate_levels = {
        'low': max(0, min(1, (141 - x) / 41 if x <= 100 else 0)),
        'medium': max(0, min((x - 111) / 41, (194 - x) / 42) if 111 <= x < 194 else 0),
        'high': max(0, min((x - 152) / 58, 1) if x >= 152 else 0)
    }
    
    return heart_rate_levels

# BLOOD SUGAR
def blood_sugar(x):
    blood_sugar_levels = {'true': int(x > 120), 'false': int(x <= 120)}
    return blood_sugar_levels

# SEX
def sex(x):
    sex_levels = {
        'male': int(x == '0'),
        'female': int(x == '1')
    }
    
    return sex_levels

# CHEST PAIN
def chest_pain(x):
    chest_pain_levels = {
        'typical_anginal': int(x == '1'),
        'atypical_anginal': int(x == '2'),
        'non_anginal_pain': int(x == '3'),
        'asymptomatic': int(x == '4')
    }
    
    return chest_pain_levels

# BLOOD PRESSURE
def blood_pressure(x):
    blood_pressure_levels = {
        'low': max(0, min((134 - x) / 23, 1)) if x < 111 else 0,
        'medium': max(0, min((x - 127) / 12, (153 - x) / 14)) if 127 <= x < 153 else 0,
        'high': max(0, min((x - 142) / 15, (172 - x) / 15)) if 142 <= x < 172 else 0,
        'very_high': max(0, min((x - 154) / 17, 1)) if 154 <= x else 0
    }
    
    return blood_pressure_levels

# OUTPUT
def output(x):
    output_levels = {
        'output_healthy': max(0, min(1, (1 - x) / 0.75 if x <= 0.25 else 0)),
        'output_sick1': max(0, min((x - 0) / 1, (2 - x) / 1) if 0 <= x < 2 else 0),
        'output_sick2': max(0, min((x - 1) / 1, (3 - x) / 1) if 1 <= x < 3 else 0),
        'output_sick3': max(0, min((x - 2) / 1, (4 - x) / 1) if 2 <= x < 4 else 0),
        'output_sick4': max(0, min((x - 3) / 0.75, 1) if x >= 3 else 0)
    }
    
    return output_levels

# Get Inputs
def fuzzification(input):
    sex_levels = sex(input['sex'])
    age_level = age(float(input['age']))
    chest_pain_levels = chest_pain(input['chest_pain'])
    blood_pressure_levels = blood_pressure(float(input['blood_pressure']))
    cholesterol_levels = cholesterol(float(input['cholestrol']))
    blood_sugar_levels = blood_sugar(float(input['blood_sugar']))
    heart_rate_levels = heart_rate(float(input['heart_rate']))
    
    return (sex_levels, age_level, chest_pain_levels, blood_pressure_levels, cholesterol_levels, blood_sugar_levels, heart_rate_levels)

import inference as inter
import fuzzification as fuzzy
import defuzzification as defuzzy


class ProvideResult(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(ProvideResult, cls).__new__(cls)
    return cls.instance

  @staticmethod
  def get_final_result(input_dict: dict) -> str:
    # Fuzzification
    fuzzy_values = fuzzy.fuzzification(input_dict)
    sex, age, chest_pain, blood_pressure, cholesterol, blood_sugar, heart_rate = fuzzy_values
    
    # Inference
    output_values = inter.inferenceRules(sex, age, chest_pain, blood_pressure, cholesterol, blood_sugar, heart_rate)
    output_healthy, output_sick1, output_sick2, output_sick3, output_sick4 = output_values
    
    # Defuzzification
    output_fuzzy = defuzzy.defuzzification(output_healthy, output_sick1, output_sick2, output_sick3, output_sick4)
    
    # Generating return string
    diagnosis = {
        (1, 2.51): 'Sick1',
        (1.78, 3.25): 'Sick2',
        (1.5, 4.5): 'Sick3',
        (3.25, float('inf')): 'Sick4'
    }
    
    # Loop through diagnosis ranges
    result = ''
    for rng, diag in diagnosis.items():
        if rng[0] <= output_fuzzy <= rng[1]:
            if result:
                result += '& '
            result += diag + ' '
    
    # Append 'output_healthy' if applicable
    if not result:
        result = 'output_healthy'
    else:
        result = result[:-1]  # Remove trailing space
    
    # Concatenate output_fuzzy
    result += ': ' + str(output_fuzzy)

    return result
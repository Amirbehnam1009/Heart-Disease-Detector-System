import fuzzification

def defuzzy_output(x, output_healthy, output_sick1, output_sick2, output_sick3, output_sick4):
    temp = fuzzification.output(x)
    
    min_values = [min(output_healthy, temp['output_healthy']), min(output_sick1, temp['output_sick1']), min(output_sick2, temp['output_sick2']), min(output_sick3, temp['output_sick3']), min(output_sick4, temp['output_sick4'])]
    output = max(min_values)
    
    return output


def defuzzification(output_healthy, output_sick1, output_sick2, output_sick3, output_sick4):
    step_size = 0.001
    total_sum = 0
    total_weight = 0
    
    for var in range(0, 4001, int(1/step_size)):
        temp = defuzzy_output(var * step_size, output_healthy, output_sick1, output_sick2, output_sick3, output_sick4)
        total_weight = total_weight + temp
        total_sum += temp * (var * step_size)
        
    return total_sum / total_weight if total_weight != 0 else 0
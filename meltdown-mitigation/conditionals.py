
def is_criticality_balanced(temperature, neutrons_emitted):

    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000
def reactor_efficiency(voltage, current, theoretical_max_power):
 
    efficiency = voltage * current / theoretical_max_power * 100
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
def fail_safe(temperature, neutrons_produced_per_second, threshold):
  
    volume = temperature * neutrons_produced_per_second
    if volume < int(threshold*0.4):
        return 'LOW'
    elif volume > int(threshold * 0.9) and volume < int(threshold * 1.1):
        return 'NORMAL'
    else:
        return 'DANGER'
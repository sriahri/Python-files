from collections import defaultdict
d = defaultdict('high_risk_count', 'low_risk_count', 'no_risk_count', 'invalid_count')
class Patient:
    def __init__(self, name, args):
        self.name = name
        self.__medical_conditions = args
    def get_med_con(self):
        return self.__medical_conditions
def get_patient_statistics(p):
    global d
    if len(p.__medical_conditions) == 0:
        d['no_risk_count'] += 1
    elif len(p.__medical_conditions) < 2:
        d['low_risk_count'] += 1
    else:
        d['high_risk_count'] += 1
    return d

try:
    patients = [Patient('Tom'), Patient('Dick', ['hpp','type1diabetic','highcholestrol']), Patient('Harry',['hpp','diabetic']),Patient('JAne',[]),Patient('John',['lbp'])]
    print(get_patient_statistics(patients))
except TypeError:
    d['invalid_count'] += 1
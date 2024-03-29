#Bayes's Theorem

def calc_bayes(prior_A, prob_B_given_A, prob_B):
    return (prior_A * prob_B_given_A) / prob_B

if __name__ == "__main__":
    #probabilidades con la información a disposición
    prob_cancer = 1 / 100000
    prob_symptom_given_cancer = 1
    prob_symptom_given_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer

    #calculo adiccional, cual es la probabilidad de tener sintoma, probabilidad condicional
    prob_symptom = (prob_symptom_given_cancer * prob_cancer) + (prob_symptom_given_no_cancer * prob_no_cancer)

    #probabilidad de tener cancer dado que tengo un sintoma
    prob_cancer_given_symptom = calc_bayes(prob_cancer, prob_symptom_given_cancer, prob_symptom)    
    
    print(prob_cancer_given_symptom)
# ==========================================
# MEDICAL DIAGNOSIS USING BAYESIAN NETWORK
# ==========================================

print("\n===================================")
print("MEDICAL DIAGNOSIS BAYESIAN NETWORK")
print("===================================")

print("\nNetwork Structure:")
print("Disease ---> Fever")
print("Disease ---> Cough")

# Prior Probability

P_disease = 0.10

# Conditional Probabilities

P_fever_given_disease = 0.80
P_fever_given_no_disease = 0.20

P_cough_given_disease = 0.70
P_cough_given_no_disease = 0.30

print("\nPrior Probability:")
print("P(Disease) =", P_disease)

print("\nConditional Probabilities:")
print(
    "P(Fever | Disease) =",
    P_fever_given_disease
)

print(
    "P(Fever | No Disease) =",
    P_fever_given_no_disease
)

print(
    "P(Cough | Disease) =",
    P_cough_given_disease
)

print(
    "P(Cough | No Disease) =",
    P_cough_given_no_disease
)

# Evidence

print("\nEvidence:")
print("Patient has Fever")

# Bayes Theorem

P_fever = (
    P_fever_given_disease * P_disease
    +
    P_fever_given_no_disease
    * (1 - P_disease)
)

P_disease_given_fever = (
    P_fever_given_disease
    * P_disease
) / P_fever

print("\nInference Result:")

print(
    "P(Disease | Fever) =",
    round(
        P_disease_given_fever,
        4
    )
)

if P_disease_given_fever > 0.5:

    print(
        "\nConclusion:"
    )

    print(
        "Disease is likely."
    )

else:

    print(
        "\nConclusion:"
    )

    print(
        "Disease is unlikely."
    )

print("\n===================================")

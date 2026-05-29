# ==========================================
# BAYESIAN NETWORK EXAMPLE
# ==========================================
print("\n===================================")
print("BAYESIAN NETWORK")
print("===================================")
P_rain = 0.30
P_wet_given_rain = 0.90
P_wet_given_no_rain = 0.10

P_wet = (
    P_wet_given_rain * P_rain
    +
    P_wet_given_no_rain * (1 - P_rain)
)
P_rain_given_wet = (
    P_wet_given_rain * P_rain
) / P_wet
print("\nExample:")
print("Rain -> Wet Grass")
print("\nP(Rain) =", P_rain)
print("P(WetGrass | Rain) =", P_wet_given_rain)
print("P(WetGrass | No Rain) =", P_wet_given_no_rain)

print("\nInference Result:")
print(
    "P(Rain | Wet Grass) =",
    round(P_rain_given_wet, 4)
)
print("\n===================================")

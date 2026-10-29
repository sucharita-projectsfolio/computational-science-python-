import math

def first_order_decay(initial_concentration, rate_constant, time_steps):
    return {t: round(initial_concentration * math.exp(-rate_constant * t), 5) for t in time_steps}

if __name__ == "__main__":
    print(first_order_decay(1.0, 0.05, [0, 5, 10, 15, 20, 30]))

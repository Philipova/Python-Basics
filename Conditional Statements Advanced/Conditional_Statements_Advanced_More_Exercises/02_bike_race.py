def calculate_donation(junior_count, senior_count, track_type):
    junior_fees = [5.50, 8, 12.25, 20]
    senior_fees = [7, 9.50, 13.75, 21.50]
    track_fees = {
        "trail": 0,
        "cross-country": 1,
        "downhill": 2,
        "road": 3
    }

    junior_fee = junior_fees[track_fees[track_type]]
    senior_fee = senior_fees[track_fees[track_type]]

    total_participants = junior_count + senior_count
    fee_reduction = 0

    if track_type == "cross-country" and total_participants >= 50:
        fee_reduction = 0.25

    total_fee = (junior_count * junior_fee + senior_count * senior_fee) * (1 - fee_reduction)
    donation_amount = total_fee * (1 - 0.05)  # Deducting 5% for expenses

    return "{:.2f}".format(donation_amount)


# Reading inputs from the console
junior_count = int(input())
senior_count = int(input())
track_type = input()

# Calculating and printing the donated amount
donated_amount = calculate_donation(junior_count, senior_count, track_type)
print(donated_amount)

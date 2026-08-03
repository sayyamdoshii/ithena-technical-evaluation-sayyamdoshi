import random
from datetime import date, timedelta
import csv

random.seed(42)

NUM_CUSTOMERS = 5000

plan_tiers = ["Basic", "Standard", "Premium"]
plan_mrr = {"Basic": 20, "Standard": 50, "Premium": 100}
regions = ["North America", "Europe", "APAC", "LATAM"]
channels = ["Organic", "Paid Ads", "Partnership", "Referral"]

start_range_begin = date(2024, 1, 1)
start_range_end = date(2025, 6, 1)

def random_date(start, end):
    delta_days = (end - start).days
    return start + timedelta(days=random.randint(0, delta_days))

rows = []

for i in range(1, NUM_CUSTOMERS + 1):
    customer_id = f"CUST{i}"
    plan_tier = random.choice(plan_tiers)
    mrr = plan_mrr[plan_tier]
    region = random.choice(regions)
    channel = random.choice(channels)

    start_dt = random_date(start_range_begin, start_range_end)

    # subscription length: most customers stay a few months to a couple years
    length_days = random.randint(30, 900)
    end_dt = start_dt + timedelta(days=length_days)

    # downgrade_flag: about 15% of customers downgrade at some point
    downgrade_flag = 1 if random.random() < 0.15 else 0

    downgrade_date = ""
    if downgrade_flag == 1:
        # downgrade happens sometime between start and end date
        max_offset = max((end_dt - start_dt).days - 1, 1)
        downgrade_offset = random.randint(1, max_offset)
        downgrade_dt = start_dt + timedelta(days=downgrade_offset)
        downgrade_date = downgrade_dt.isoformat()

    rows.append([
        customer_id,
        plan_tier,
        start_dt.isoformat(),
        end_dt.isoformat(),
        mrr,
        region,
        channel,
        downgrade_flag,
        downgrade_date
    ])

with open("subscriptions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "customer_id", "plan_tier", "start_date", "end_date",
        "mrr", "region", "acquisition_channel", "downgrade_flag", "downgrade_date"
    ])
    writer.writerows(rows)

print(f"Done! subscriptions.csv created with {NUM_CUSTOMERS} rows")

import random
import string
from datetime import datetime, timedelta
import pandas as pd

# -------------------------
# CONFIGURATION
# -------------------------
NUM_SKUS = 5489
OUTPUT_FILE = "sku_master_dq_raw.csv"

ERROR_RATE_LOW = 0.01
ERROR_RATE_HIGH = 0.08

START_DATE = datetime(2017, 1, 1)
END_DATE = datetime(2025, 12, 31)
FUTURE_DATE = datetime(2032, 12, 31)

PRODUCT_TYPES = ["OTC", "Pharma"]
COMMERCIAL_TYPES = ["General Market", "Private Label", "Sample"]
ABC_CODES = ["A", "B", "C"]
SKU_STATUS = ["Active", "Inactive"]

VALID_DCS = {
    "NJWH100A": "NJ",
    "PAWH200B": "PA",
    "TXDC300C": "TX",
    "CADC400D": "CA",
    "ILWH500E": "IL"
}

DRUG_NAMES = [
    "Amoxicillin", "Metformin", "Lisinopril", "Atorvastatin",
    "Ibuprofen", "Omeprazole", "Losartan", "Sertraline",
    "Hydrochlorothiazide", "Levothyroxine"
]

OTC_PRODUCTS = [
    "Pain Relief Tablets", "Cold and Flu Capsules",
    "Allergy Relief Caps", "Antacid Chewables", "Cough Syrup"
]

# -------------------------
# HELPER FUNCTIONS
# -------------------------
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_sku(valid=True):
    sku = f"{random.randint(100000,999999)}{''.join(random.choices(string.ascii_uppercase, k=3))}"
    if not valid:
        i = random.randint(0, len(sku)-2)
        sku = list(sku)
        sku[i], sku[i+1] = sku[i+1], sku[i]
        sku = "".join(sku)
    return sku

def typo(text):
    i = random.randint(0, len(text)-2)
    return text[:i] + text[i+1] + text[i] + text[i+2:]

def generate_description(product_type, commercial_type, error=False):
    if product_type == "Pharma":
        base = f"{random.choice(DRUG_NAMES)} {random.choice([5,10,20,50,100,250])}mg Tablets"
    else:
        base = random.choice(OTC_PRODUCTS)

    # Occasionally mention commercial type
    if commercial_type == "Private Label" and random.random() < 0.6:
        base += " Private Label"
    elif commercial_type == "Sample" and random.random() < 0.6:
        base += " Sample"

    return typo(base) if error else base

def generate_fin_group(product_type, dc_code, valid=True):
    if not valid:
        return random.choice(["", "12345", "INVALIDFRG1", None])

    pt = "PHR" if product_type == "Pharma" else "OTC"
    dc = VALID_DCS.get(dc_code, "XX")
    cost_center = f"{random.randint(1000,9999)}"
    return f"{pt}{dc}{cost_center}"

# -------------------------
# ERROR COUNTS
# -------------------------
def error_count():
    return int(NUM_SKUS * random.uniform(ERROR_RATE_LOW, ERROR_RATE_HIGH))

err_sku = error_count()
err_desc = error_count()
err_pt = error_count()
err_lot = error_count()
err_dc = error_count()
err_abc = error_count()
err_frg = error_count()
err_disc = error_count()
err_comm = error_count()

# -------------------------
# BASE DATA
# -------------------------
rows = []

for _ in range(NUM_SKUS):
    product_type = random.choice(PRODUCT_TYPES)
    commercial_type = random.choice(COMMERCIAL_TYPES)
    dc = random.choice(list(VALID_DCS.keys()))
    entry_date = random_date(START_DATE, END_DATE)

    rows.append({
        "SKU": generate_sku(),
        "Description": generate_description(product_type, commercial_type),
        "Commercial Classification": commercial_type,
        "Product Type": product_type,
        "Lot Controlled": "Yes",
        "Primary Distribution Center": dc,
        "ABC Velocity Code": random.choice(ABC_CODES),
        "Financial Reporting Group": generate_fin_group(product_type, dc),
        "SKU Entry Date": entry_date.strftime("%m/%d/%Y"),
        "SKU Status": random.choice(SKU_STATUS),
        "SKU Planned Discontinuation": ""
    })

df = pd.DataFrame(rows)

# -------------------------
# ERROR INJECTION
# -------------------------
df.loc[random.sample(df.index.tolist(), err_sku), "SKU"] = df["SKU"].apply(lambda _: generate_sku(valid=False))
df.loc[random.sample(df.index.tolist(), err_desc), "Description"] = df["Description"].apply(typo)
df.loc[random.sample(df.index.tolist(), err_pt), "Product Type"] = ""
df.loc[random.sample(df.index.tolist(), err_lot), "Lot Controlled"] = random.choice(["No", ""])
df.loc[random.sample(df.index.tolist(), err_dc), "Primary Distribution Center"] = random.choice(["", "TX999", None])
df.loc[random.sample(df.index.tolist(), err_abc), "ABC Velocity Code"] = ""
df.loc[random.sample(df.index.tolist(), err_frg), "Financial Reporting Group"] = generate_fin_group("OTC", "NJWH100A", valid=False)

# Commercial classification errors
df.loc[random.sample(df.index.tolist(), err_comm), "Commercial Classification"] = random.choice(["", "Promo", None])

# Planned discontinuation logic
future_idx = random.sample(df.index.tolist(), err_disc)
df.loc[future_idx, "SKU Planned Discontinuation"] = [
    random_date(datetime(2026,1,1), FUTURE_DATE).strftime("%m/%d/%Y") for _ in future_idx
]

hard_idx = random.sample(df[df["SKU Status"] == "Active"].index.tolist(), int(err_disc * 0.15))
df.loc[hard_idx, "SKU Planned Discontinuation"] = random_date(
    datetime(2019,1,1), datetime(2022,12,31)
).strftime("%m/%d/%Y")

# -------------------------
# OUTPUT
# -------------------------
df.to_csv(OUTPUT_FILE, index=False)

print("SKU MASTER GENERATED")
print(f"Records: {len(df)}")
print(f"Output file: {OUTPUT_FILE}")


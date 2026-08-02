import pandas as pd
orders_df = pd.DataFrame([
("ORD1", "CUST1", "2024-01-05", "completed", "STORE1"),
("ORD2", "CUST2", "2024-01-06", "completed", "STORE1"),
("ORD3", "CUST3", "2024-01-07", "completed", "STORE2"),
("ORD4", "CUST4", "2024-01-08", "completed", "STORE2"),
("ORD5", "CUST5", "2024-01-09", "completed", "STORE1"),
("ORD6", "CUST6", "2024-01-10", "completed", "STORE2"),
], columns=["order_id", "customer_id", "order_date", "order_status", "store_id"])
items_df = pd.DataFrame([
("ITEM1", "ORD1", "PROD1", 2, 50.00, 0),
("ITEM2", "ORD2", "PROD2", 1, 100.00, 0),
("ITEM3", "ORD3", "PROD3", 3, 30.00, 0),
("ITEM4", "ORD4", "PROD4", 1, 200.00, 0),
("ITEM5", "ORD5", "PROD5", 5, 20.00, 0),
("ITEM6", "ORD6", "PROD6", 2, 75.00, 0),
], columns=["order_item_id", "order_id", "product_id", "qty", "unit_price", "discount_pct"])
payments_df = pd.DataFrame([
("PAY1", "ORD1", 100.00, "card", "2024-01-05 10:00:00", "success"),
("PAY2", "ORD2", 90.00, "card", "2024-01-06 11:00:00", "success"),
("PAY3", "ORD3", 90.00, "card", "2024-01-07 09:00:00", "success"),
("PAY3B", "ORD3", 90.00, "card", "2024-01-07 09:00:20", "success"),
("PAY4", "ORD4", 200.00, "card", "2024-01-08 14:00:00", "success"),
("PAY5", "ORD5", 120.00, "card", "2024-01-09 15:00:00", "success"),
], columns=["payment_id", "order_id", "payment_amount", "payment_method", "payment_date", "payment_status"])
refunds_df = pd.DataFrame([
("REF1", "ORD4", 20.00, "2024-01-09", "customer changed mind"),
], columns=["refund_id", "order_id", "refund_amount", "refund_date", "refund_reason"])
items_df["line_total"] = items_df["qty"] * items_df["unit_price"] * (1 - items_df["discount_pct"])
order_value = items_df.groupby("order_id")["line_total"].sum().reset_index(name="order_value")
paid = payments_df[payments_df["payment_status"] == "success"]
total_paid = paid.groupby("order_id")["payment_amount"].sum().reset_index(name="total_paid")
total_refunded = refunds_df.groupby("order_id")["refund_amount"].sum().reset_index(name="total_refunded")
df = orders_df[["order_id"]].merge(order_value, on="order_id", how="left").merge(total_paid, on="order_id", how="left").merge(total_refunded, on="order_id", how="left").fillna(0)
df["net_received"] = df["total_paid"] - df["total_refunded"]
df["difference"] = df["order_value"] - df["net_received"]
tolerance = 1.0
flagged = df[df["difference"].abs() > tolerance].copy()
flagged["flag_reason"] = "overpayment"
flagged.loc[flagged["difference"] > 0, "flag_reason"] = "underpayment"
flagged.loc[flagged["total_refunded"] > 0, "flag_reason"] = "refund_mismatch"
print(flagged.to_string(index=False))



import pandas as pd
def flag_leakage_orders(orders_df, items_df, payments_df, refunds_df, tolerance=1.0)
#going through each order at one time
for order_id in orders_df["order_id"]:
#order worth, total value
order_items = items_df[items_df["order_id"] == order_id]
order_value = (order_items["qty"] * order_items["unit_price"] * (1 - order_items["discount_pct"])).sum()
#order completed payments
order_payments = payments_df[
(payments_df["order_id"] == order_id) 
& (payments_df["payment_status"] == "completed") ]
total_paid = order_payments["payment_amount"].sum()
#order refunds
order_refunds = refunds_df[refunds_df["order_id"] == order_id]
total_refunded = order_refunds["refund_amount"].sum()
#expected vs actual
net_received = total_paid - total_refunded
difference = order_value - net_received
if abs(difference) > tolerance:
if total_refunded > 0:
reason = "refund_mismatch"
elif difference > 0:
reason = "underpayment"
else:
reason = "overpayment"
flagged_orders.append({
  "order_id": order_id,
  "order_value": order_value,
  "total_paid": total_paid,
  "total_refunded": total_refunded,
  "net_received": net_received,
  "difference": difference,
  "flag_reason": reason })

return pd.DataFrame(flagged_orders)




/*
QUESTION 4: Given orders, order_items, payments, and refunds (schema below), 
write one query that flags orders where the net order value does not reconcile 
with payments minus refunds, within a tolerance of ± 1.
*/

SOLUTION:

SELECT
o.order_id,
ov.order_value,
p.total_paid,
r.total_refunded
FROM orders o
JOIN (
SELECT order_id, SUM(qty * unit_price * (1 - discount_pct)) AS order_value
FROM order_items
GROUP BY order_id
) ov ON ov.order_id = o.order_id
JOIN (
SELECT order_id, SUM(payment_amount) AS total_paid
FROM payments
WHERE payment_status = 'completed'
GROUP BY order_id
) p ON p.order_id = o.order_id
JOIN (
SELECT order_id, SUM(refund_amount) AS total_refunded
FROM refunds
GROUP BY order_id
) r ON r.order_id = o.order_id
WHERE ABS(ov.order_value - (p.total_paid - r.total_refunded)) > 1;

----------------------------------------------------------------------------------------------------------------------------------------
/*
QUESTION 5: The payments table has duplicate rows caused by a gateway retry bug — same order, same
amount, timestamps within 60 seconds of each other. Write the de-duplication logic (not
DISTINCT) that must run before Technical Question 1.
/*

SOLUTION:





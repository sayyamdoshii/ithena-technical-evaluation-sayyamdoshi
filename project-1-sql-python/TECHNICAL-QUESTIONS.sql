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
 WHERE payment_status = 'success'
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
*/

SOLUTION:

SELECT p1.payment_id, p1.order_id, p1.payment_amount, p1.payment_date
FROM payments p1
JOIN payments p2
ON p1.order_id = p2.order_id
AND p1.payment_amount = p2.payment_amount
AND p1.payment_id != p2.payment_id
AND ABS(strftime('%s', p1.payment_date) - strftime('%s', p2.payment_date)) <= 60
AND p1.payment_id > p2.payment_id;




----------------------------------------------------------------------------------------------------------------------------------------







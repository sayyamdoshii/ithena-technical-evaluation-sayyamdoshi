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
JOIN 






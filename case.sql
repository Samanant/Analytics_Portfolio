SELECT * FROM invoices;

-- List the invoice number, vendor name, and invoice total for each invoice.
-- Include a column indicating whether the invoice was paid in full, 
-- partially paid, or not paid at all.

-- w/ a simple case statement
SELECT invoice_number,
       vendor_name,
       invoice_total,
       CASE payment_total + credit_total
         WHEN 0 THEN 'Not paid'
         WHEN invoice_total THEN 'Paid in Full'
         ELSE 'Partially Paid'
	   END AS pmt_status
  FROM invoices AS I
  JOIN vendors AS V USING (vendor_id);
  
-- w/ a searched case statement
SELECT invoice_number,
       vendor_name,
       invoice_total,
       CASE WHEN payment_total + credit_total = invoice_total THEN 'Paid in Full'
            WHEN payment_total + credit_total = 0 THEN 'Not Paid'
            ELSE 'Partially Paid'
	   END AS pmt_status
  FROM invoices AS I
  JOIN vendors AS V USING (vendor_id);


-- Show the invoice number, vendor name, and invoice total for all invoices.
-- Include a column indicating whether the invoice was paid on time, late, or
-- not at all.
-- w/a searched case statement
SELECT invoice_number,
       vendor_name,
       invoice_total,
       payment_date,
       invoice_due_date,
       CASE WHEN payment_date <= invoice_due_date THEN 'On Time'
            WHEN payment_date IS NULL THEN 'Not paid'
            ELSE 'Late'
	   END AS paid
  FROM invoices AS I
  JOIN vendors AS V USING (vendor_id);
  
-- Simple case can not handle NULL values
SELECT CASE NULL
         WHEN NULL THEN 'Yes'
         ELSE 'No'
	   END AS test;

-- Show all invoices and whether or not they have been paid.
-- A simple case statement returns incorrect results
SELECT invoice_number,
       vendor_name,
       invoice_total,
       payment_date,
       invoice_due_date,
       CASE payment_date
         WHEN NULL THEN 'Not Paid'
         ELSE 'Paid'
	   END AS paid
  FROM invoices AS I
  JOIN vendors AS V USING (vendor_id);
       
-- Use a searched case when the column contains NULLs
SELECT invoice_number,
       vendor_name,
       invoice_total,
       payment_date,
       invoice_due_date,
       CASE 
         WHEN payment_date IS NULL THEN 'Not Paid'
         ELSE 'Paid'
	   END AS paid
  FROM invoices AS I
  JOIN vendors AS V USING (vendor_id);
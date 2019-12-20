
use ata_online_shop;

-- 1. gabungkan data transaksi dari user id 1 dan user id 2
SELECT * FROM transactions
WHERE user_id = 1 
UNION 
SELECT * FROM transactions
WHERE user_id = 2;
    
-- 2. Jumlah harga transaksi user id 1
SELECT 
    SUM(total_price)
FROM
    transactions
WHERE
    user_id = 1;

-- 3. Total transaksi dengan product type 2
-- karena pada product, product id yang memiliki product type 2 adalah product id 3 - 8;
SELECT 
    COUNT(id)
FROM
    transactions
WHERE
    id IN 
		(SELECT distinct transaction_id
        FROM transaction_details
        WHERE product_id IN 
				(SELECT id 
                from product 
                where product_type_id = 2));-- kebetulan semua transaksi adalah produk type 2
-- 4. 
SELECT 
    p.*, pt.name
FROM
    product_type pt
        INNER JOIN
    product p ON pt.id = p.product_type_id;

-- 5. Tampilkan semua field table transaction,product, & user
SELECT 
    t.*, u.name, td.product_id, p.name AS product
FROM
    transactions t
        LEFT JOIN
    users u ON t.user_id = u.id
        LEFT JOIN
    transaction_details td ON t.id = td.transaction_id
        LEFT JOIN
    product p ON td.product_id = p.id;
        
-- 8. Tampilkan data products yang tidak pernah ada di tabel transaction_details dengan
-- sub-query
SELECT 
    *
FROM
    product
WHERE
    id NOT IN (SELECT 
            product_id
        FROM
            transaction_details);

-- 6. Fungsi delete row transaction
DELIMITER $$
CREATE TRIGGER delete_transaction_details
before DELETE ON transactions FOR EACH ROW
	BEGIN
    -- declare variable
    
    declare v_transaction_id INT;
    set v_transaction_id=OLD.id;
    
    -- trigger code
    Delete from transaction_details where
		transaction_id=v_transaction_id; 
        
END $$
DELIMITER ;

use ata_online_shop;

DELETE FROM transactions 
WHERE
    id = 14;

-- 7. Fungsi update total qty
DELIMITER $$
CREATE TRIGGER update_total_qty
after DELETE ON transaction_details FOR EACH ROW
	BEGIN
    -- declare variable
    
    declare updated_qty INT;
    
	-- trigger code
    set updated_qty=(select SUM(qty) from transaction_details 
    where transaction_id=OLD.transaction_id);
    update transactions set total_qty=updated_qty where id=OLD.transaction_id;
        
END $$
DELIMITER ;

-- drop trigger update_total_qty;

DELETE FROM transaction_details 
WHERE transaction_id = 1 AND product_id = 3;
-- 1. Insert
use ata_online_shop;

-- 1.a. Insert 5 Operator
insert into operators
(name) values
('telkomsel'), ('indosat'), ('XL_Axiata'), ('Telkom'), ('Natrindo'); 

-- 1.b. Insert 3 product Type
insert into product_type
(name) values
('pulsa'), ('paket data'), ('kartu'); 

-- 1.c. Insert 2 product dengan produk type id = 1 dan operator id = 3
insert into product
(product_type_id, operator_id, code, price, name, status) values
(1, 3, 'XL1', 11000, 'Pulsa XL 10.000', 1),
(1, 3, 'XL2', 51000, 'Pulsa XL 51.000', 1); 

-- 1.d. Insert 3 product dengan produk type id = 2 dan operator id = 1
insert into product
(product_type_id, operator_id, code, price, name, status) values
(2, 1, 'Tel1', 20000, 'Paket data Telkomsel 5 GB', 1),
(2, 1, 'Tel2', 75000, 'Paket data Telkomsel 17 GB', 1),
(2, 1, 'Tel3', 100000, 'Paket data Telkomsel 25 GB', 1);

-- 1.e. Insert 3 product dengan produk type id = 3 dan operator id = 4
insert into product
(product_type_id, operator_id, code, price, name, status) values
(2, 1, 'Telkom1', 5000, 'Kartu perdana flexi', 1),
(2, 1, 'Telkom2', 55000, 'Kartu perdana flexi + 15 GB', 1),
(2, 1, 'Telkom3', 110000, 'Kartu perdana flexi + 20 GB', 1);

-- 1.f. Insert product description pada setiap produk
insert into product_description
(description) values
('Produk pulsa kartu XL sebesar 10.000'),
('Produk pulsa kartu XL sebesar 51.000'),
('Produk paket data Telkomsel 5 GB'),
('Produk paket data Telkomsel 17 GB'),
('Produk paket data Telkomsel 25 GB'),
('Produk kartu perdana flexi'),
('Produk kartu perdana flexi + paket data 15 GB'),
('Produk kartu perdana flexi + paket data 20 GB');

-- 1.g. Insert 3 payment methods
insert into payment_methods
(name,status) values
('gopay',1), ('OVO',1), ('Transfer Bank',1);

-- 1.h. Insert 5 user
insert into users
(status,dob,gender) values
(1,'2019-12-02','M'), 
(1,'1996-04-09','M'), 
(1,'2000-01-25','F'),
(1,'1890-02-08','F'), 
(1,'2014-06-10','M');

-- 1.i. Insert 3 transaksi di masing-masing user
insert into transactions
(status, user_id, payment_method_id, total_qty, total_price) values
(1, 1, 1, 1, 10000),
(1, 1, 2, 1, 10000),
(1, 1, 3, 1, 10000),
(1, 2, 1, 1, 10000),
(1, 2, 2, 1, 10000),
(1, 2, 3, 1, 10000),
(1, 3, 1, 1, 10000),
(1, 3, 2, 1, 10000),
(1, 3, 3, 1, 10000),
(1, 4, 1, 1, 10000),
(1, 4, 2, 1, 10000),
(1, 4, 3, 1, 10000),
(1, 5, 1, 1, 10000),
(1, 5, 2, 1, 10000),
(1, 5, 3, 1, 10000);


-- 1.j. Insert 3 produk di masing-masing transaksi
insert into transaction_details
(transaction_id, product_id, status, qty, price) values
(1,6,1,1,5000), (1,5,1,1,100000), (1,3,1,1,20000),
(2,6,1,1,5000), (2,5,1,1,100000), (2,3,1,1,20000),
(3,6,1,1,5000), (3,5,1,1,100000), (3,3,1,1,20000),
(4,6,1,1,5000), (4,5,1,1,100000), (4,3,1,1,20000),
(5,6,1,1,5000), (5,5,1,1,100000), (5,3,1,1,20000),
(6,6,1,1,5000), (6,5,1,1,100000), (6,3,1,1,20000),
(7,6,1,1,5000), (7,5,1,1,100000), (7,3,1,1,20000),
(8,6,1,1,5000), (8,5,1,1,100000), (8,3,1,1,20000),
(9,6,1,1,5000), (9,5,1,1,100000), (9,3,1,1,20000),
(10,6,1,1,5000), (10,5,1,1,100000), (10,3,1,1,20000),
(11,6,1,1,5000), (11,5,1,1,100000), (11,3,1,1,20000),
(12,6,1,1,5000), (12,5,1,1,100000), (12,3,1,1,20000),
(13,6,1,1,5000), (13,5,1,1,100000), (13,3,1,1,20000),
(14,6,1,1,5000), (14,5,1,1,100000), (14,3,1,1,20000),
(15,6,1,1,5000), (15,5,1,1,100000), (15,3,1,1,20000);

-- 2. select

-- 2.a. Tampilkan nama user dengan gender laki-laki

-- tambahkan kolom nama pada tabel user

alter table users add name varchar(250) NOT NULL;

-- Update nama ke kolom nama;

update users set name='Hamdi' where id=1;
update users set name='Ulum' where id=2;
update users set name='Hedy' where id=3;
update users set name='Fazri' where id=4;
update users set name='Fatur' where id=5;

SELECT 
    *
FROM
    users
WHERE
    gender = 'M';

-- 2.b. Tampilkan product dengan id = 3

SELECT 
    *
FROM
    product
WHERE
    id = 3 ;
    
-- 2.c. Tampilkan data pelanggan yang created_at dalam range 7 hari kebelakang
--      dan memiliki nama mengandung kata 'a'

SELECT 
    *
FROM
    users
WHERE
    created_at <= round(now())-7 and name like '%a%' ;
    
-- 2.d. Jumlah user yang memiliki gender perempuan
select count(*) from users where gender = 'F';

-- 2.e. Tampilkan data pelanggan dengan urutan abjad
select * from users order by name ASC;

-- 2.f. Tampilkan 5 data pada soal 2.begin
select * from product where id=3 limit 5;

-- 3.Update 

-- 3.a. ubah product dengan id=1 dengan product dummy
update product set name='product dummy' where id=1;

-- 3.b. ubah qty = 3 pada transaction detail dengan product id = 1
update transaction_details set qty=3 where product_id=1;

-- -- 4. Delete

-- -- 4. a. delete data pada tabel product dengan id 1
-- -- terlebih dahulu mendelete product id = 1 pada product description
-- delete from product_description where product_id = 1;
-- -- lalu (karena pada transaction detail tidak dipakai product id=1 maka bisa langsung

-- delete from product where id = 1 ;

-- -- 4. b. delete pada tabel product dengan product type id 1
-- -- terlebih dahulu mendelete product id=2 pada tabel product_description
-- delete from product_description where product_id = 2;

-- -- sehingga bisa dilakukan;
-- delete from product where product_type_id = 1;

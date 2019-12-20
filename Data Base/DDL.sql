
-- 1.
create database ata_online_shop;

use ata_online_shop;

-- 2.
CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    status SMALLINT(1) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(1) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE product_type (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE operators (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);


CREATE TABLE payment_methods (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    status SMALLINT(1) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE product (
    id INT(11) NOT NULL AUTO_INCREMENT,
    product_type_id INT(11) NOT NULL,
    operator_id INT(11) NOT NULL,
    code VARCHAR(50) NOT NULL,
    price NUMERIC(25 , 2 ) NOT NULL,
    name VARCHAR(100) NOT NULL,
    status SMALLINT(1) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY ol_product_type_id (product_type_id),
    CONSTRAINT ol_product_type_id FOREIGN KEY (product_type_id)
        REFERENCES product_type (id),
    KEY ol_operator_id (operator_id),
    CONSTRAINT ol_operator_id FOREIGN KEY (operator_id)
        REFERENCES operators (id)
);

CREATE TABLE product_description (
    product_id INT(11) NOT NULL auto_increment,
    description VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id),
    KEY ol_description_poduct_id (product_id),
    CONSTRAINT ol_description_poduct_id FOREIGN KEY(product_id)
        REFERENCES product(id)
);

CREATE TABLE transactions (
    id INT(11) NOT NULL AUTO_INCREMENT,
    status SMALLINT(1) NOT NULL,
    user_id INT(11) NOT NULL,
    payment_method_id INT(11) NOT NULL,
    total_qty INT(11) NOT NULL,
    total_price NUMERIC(25 , 2 ) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY ol_user_id (user_id),
    CONSTRAINT ol_user_id FOREIGN KEY (user_id)
        REFERENCES users (id),
    KEY ol_payment_method_id (payment_method_id),
    CONSTRAINT ol_payment_method_id FOREIGN KEY (payment_method_id)
        REFERENCES payment_methods (id)
);

CREATE TABLE transaction_details (
    transaction_id INT(11) NOT NULL,
    product_id INT(11) NOT NULL,
    status VARCHAR(10) NOT NULL,
    qty INT(11) NOT NULL,
    price NUMERIC(25 , 2 ) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (transaction_id , product_id),
		CONSTRAINT ol_transaction_id FOREIGN KEY (transaction_id)
			REFERENCES transactions (id),
		CONSTRAINT ol_product_id FOREIGN KEY (product_id)
			REFERENCES product (id)
);

-- 3.
CREATE TABLE kurir (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- 4.
alter table kurir add column ongkos_dasar NUMERIC(25,2) NOT NULL;

describe kurir;

-- 5.
rename table kurir to shipping;

-- 6.
drop table shipping;

-- 7.

-- 7.a. 1-1
CREATE TABLE payment_method_description(
	id INT(11) NOT NULL AUTO_INCREMENT,
    payment_methods_id INT(11) NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY ol_payment_methods_description_id (payment_methods_id),
    CONSTRAINT ol_payment_methods_description_id FOREIGN KEY (payment_methods_id)
        REFERENCES payment_methods(id)
);

-- 7.b. 1-M
CREATE TABLE alamat(
	id INT(11) NOT NULL AUTO_INCREMENT,
	user_id INT(11) NOT NULL,
    alamat TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY ol_alamat_id (user_id),
    CONSTRAINT ol_alamat_id FOREIGN KEY (user_id)
        REFERENCES users(id)
);

-- 7.c. M-M
CREATE TABLE user_payment_method_detail(
	user_id INT(11) NOT NULL ,
    payment_method_id INT(11) NOT NULL,
    detail_description TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id,payment_method_id),
		CONSTRAINT ol_payment_detail_users_id FOREIGN KEY (user_id)
			REFERENCES users(id),
		CONSTRAINT ol_payment_detail_payment_method_id FOREIGN KEY (payment_method_id)
			REFERENCES payment_methods(id)
);

-- drop database ata_online_shop;

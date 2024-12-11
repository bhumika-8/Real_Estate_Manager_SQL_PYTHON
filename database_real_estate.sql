CREATE DATABASE PROJECT_2;
USE PROJECT_2;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    role ENUM('customer', 'agent') NOT NULL
);

CREATE TABLE agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    license_number VARCHAR(50),
    phone_number VARCHAR(15),
    rating DECIMAL(3, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);


CREATE TABLE properties (
    property_id INT PRIMARY KEY,
    agent_id INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    price DECIMAL(10, 2),
    size DECIMAL(10, 2),
    date_listed DATE,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id) ON DELETE CASCADE
);

CREATE TABLE favorites (
    user_id INT,
    property_id INT,
    date_added DATE,
    PRIMARY KEY (user_id, property_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    buyer_id INT,
    transaction_date DATE,
    transaction_amount DECIMAL(10, 2),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (buyer_id) REFERENCES users(user_id) ON DELETE CASCADE
);


DELIMITER $$

CREATE PROCEDURE insert_user(
    IN p_username VARCHAR(255),
    IN p_password VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_role ENUM('customer', 'agent')
)
BEGIN
    INSERT INTO users (username, password, email, role)
    VALUES (p_username, p_password, p_email, p_role);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE insert_agent(
    IN p_user_id INT,
    IN p_license_number VARCHAR(50),
    IN p_phone_number VARCHAR(15),
    IN p_rating DECIMAL(3, 2)
)
BEGIN
    INSERT INTO agents (user_id, license_number, phone_number, rating)
    VALUES (p_user_id, p_license_number, p_phone_number, p_rating);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE insert_property(
    IN p_property_id INT,
    IN p_agent_id INT,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_location VARCHAR(255),
    IN p_price DECIMAL(10, 2),
    IN p_size DECIMAL(10, 2),
    IN p_date_listed DATE
)
BEGIN
    INSERT INTO properties (property_id, agent_id, title, description, location, price, size, date_listed)
    VALUES (p_property_id, p_agent_id, p_title, p_description, p_location, p_price, p_size, p_date_listed);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE update_property_2(
    IN p_property_id INT,
    IN p_agent_id INT,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_location VARCHAR(255),
    IN p_price DECIMAL(10, 2),
    IN p_size DECIMAL(10, 2),
    IN p_date_listed DATE
)
BEGIN
    UPDATE properties
    SET title = p_title,
        description = p_description,
        location = p_location,
        price = p_price,
        size = p_size,
        agent_id=p_agent_id,
        date_listed = p_date_listedupdate_property_2
    WHERE property_id = p_property_id;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE delete_property(
    IN p_property_id INT
)
BEGIN
    DELETE FROM properties WHERE property_id = p_property_id;
END $$
update_property
DELIMITER ;

DELIMITER $$

CREATE PROCEDURE add_to_favorites(
    IN p_user_id INT,
    IN p_property_id INT
)
BEGIN
    INSERT INTO favorites (user_id, property_id, date_added)
    VALUES (p_user_id, p_property_id, CURDATE());
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE add_transaction(
    IN p_transaction_id INT,
    IN p_property_id INT,
    IN p_buyer_username VARCHAR(255),
    IN p_transaction_amount DECIMAL(10, 2)
)
BEGIN
    DECLARE v_buyer_id INT;

    SELECT user_id INTO v_buyer_id
    FROM users
    WHERE username = p_buyer_username;
    
    INSERT INTO transactions (transaction_id, property_id, buyer_id,transaction_date, transaction_amount)
    VALUES (p_transaction_id, p_property_id, v_buyer_id, CURDATE(), p_transaction_amount);
END $$

DELIMITER ;


DELIMITER $$



CREATE VIEW property_favorite_count AS
SELECT p.property_id, p.title AS property_title, p.location, p.price, COUNT(f.user_id) AS favorite_count
FROM properties p
LEFT JOIN favorites f ON p.property_id = f.property_id
GROUP BY p.property_id, p.title, p.location, p.price;


CREATE TABLE property_deletion_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
   
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




DELIMITER $$

CREATE TRIGGER after_property_delete
AFTER DELETE ON properties
FOR EACH ROW
BEGIN
    INSERT INTO property_deletion_log (property_id)
    VALUES (OLD.property_id);
END $$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER after_transaction_insert
AFTER INSERT ON transactions
FOR EACH ROW
BEGIN
    DECLARE v_agent_id INT;
    SELECT agent_id INTO v_agent_id
    FROM properties
    WHERE property_id = NEW.property_id;

    UPDATE agents
    SET rating = LEAST(rating + 0.1, 5.0)  
    WHERE agent_id = v_agent_id;
END $$

DELIMITER ;


CREATE VIEW active_properties AS
SELECT p.*
FROM properties p
LEFT JOIN transactions t ON p.property_id = t.property_id
WHERE t.transaction_id IS NULL;
select * from active_properties where trim(location)="Pune";

select * from users;
select * from agents;
select * from property_deletion_log;
select * from property_favorite_count;



-- make trigger for table items when there is an INSERT in table orders

DELIMITER //

CREATE TRIGGER items AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END//

DELIMITER ;

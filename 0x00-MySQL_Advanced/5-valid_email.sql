-- creates a trigger that resets the attribute valid_email only when the
-- email has been changed
DELIMITER //

DROP TRIGGER IF EXISTS updt_email;
CREATE TRIGGER updt_email 
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.EMAIL != OLD.email THEN
	SET NEW.valid_email = 0;
	END IF;
END;
//

-- func divides (and returns) the first by the second number or returns 0
-- if the second number is equal to 0.
USE holberton;

DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE result FLOAT;
	IF b = 0 THEN
		SET result = 0;
	ELSE
		SET result = (a / b);
	END IF;
	RETURN result;
END;
//

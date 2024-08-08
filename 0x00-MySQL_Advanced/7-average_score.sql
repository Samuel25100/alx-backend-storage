-- stored procedure that computes and store the average score for a student
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE avr FLOAT;
	SET avr = (
		SELECT AVG(score) FROM corrections
		WHERE corrections.user_id = user_id
	);
	UPDATE users SET average_score=avr
	WHERE id = user_id;
END;
//

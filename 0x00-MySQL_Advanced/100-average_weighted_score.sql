-- stored procedure that computes and store the average weighted score for student
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET users.average_score = (
		SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
		FROM corrections
		JOIN projects ON corrections.project_id = projects.id
		WHERE corrections.user_id = user_id
	)
	WHERE users.id = user_id;

END;
//

-- stored procedure that computes and store the average weighted score for student
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	SET users.average_score = (
		SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
		FROM corrections
		JOIN projects ON corrections.project_id = projects.id
		WHERE corrections.user_id = users.id
	);

END;
//

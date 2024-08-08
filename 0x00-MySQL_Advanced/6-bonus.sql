-- stored procedure AddBonus that adds a new correction for a student
DELIMITER //

CREATE PROCEDURE AddBonus(
	IN use_id INT,
	IN project_name VARCHAR(255),
	IN nwscore FLOAT
)
BEGIN
	INSERT INTO projects (name)
	SELECT project_name
	WHERE NOT EXISTS (
		SELECT 1 FROM projects WHERE name = project_name
	);
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (
		use_id,
		(SELECT id FROM projects WHERE name = project_name),
		nwscore
	);
END
//

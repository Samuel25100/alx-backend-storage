-- using data from metal_bands ranks country origins of bands
-- ordered by number of fans
USE holberton;
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

# Write your MySQL query statement below

WITH FirstLogins AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND((COUNT(T2.player_id)*1.0) / (SELECT COUNT(*) FROM FirstLogins) , 2) AS fraction
FROM FirstLogins T1
INNER JOIN Activity T2 ON T1.player_id = T2.player_id AND T2.event_date = DATE_ADD(T1.first_login_date, INTERVAL 1 DAY);
-- listvthe number of records with the same score
-- list shuld be sorted to descending 

SELECT score, COUNT(*) AS number FROM hbtn_0c_0.second_table GROUP BY score ORDER BY number DESC;

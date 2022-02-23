SELECT MAX(Score)
FROM Performance
WHERE Score < (
                SELECT MAX(Score)
                FROM Performance
);
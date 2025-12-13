CREATE TABLE "input" (v TEXT, n INTEGER PRIMARY KEY);
.import data07.txt input
SELECT * FROM input;


CREATE TABLE vars (rows INTEGER, cols INTEGER);
INSERT INTO vars VALUES (
  (select count(*) from input),
  (select length(v) from input where n=1)
  );

WITH RECURSIVE output(prev, cur, n, x) as (
  SELECT v, '', 1, 0 FROM input WHERE n=1
  UNION ALL
  -- input.v is the current row of the input data
  -- output.prev is the previous row of the output data
  -- output.cur is the current row of the output data, built up to char x-1
  --
  SELECT
    if(x = cols+1, output.cur, output.prev),
    if(x = cols+1, '',
      concat(if(x = cols+1, '',output.cur),
        -- compute the next character of the current line
        IF(
          -- case 1
          'S' is SUBSTR(output.prev, x, 1),
          '|',

          -- case 2
          ('^' is SUBSTR(input.v, x-1, 1)) OR ('^' is SUBSTR(input.v, x+1, 1)),
          '|',

          -- case 3
          ('|' is SUBSTR(output.prev, x, 1)) AND ('.' is SUBSTR(input.v, x, 1)),
          '|',

          -- else
          SUBSTR(input.v, x, 1)
          )
        )
      ),
    if(x = cols+1, output.n+1, output.n),
    if(x = cols+1, 1, x+1) -- x = x+1
    FROM input, output, vars
    WHERE input.n = output.n+1
    LIMIT (SELECT rows*cols FROM vars)
)
SELECT * FROM output WHERE x = (SELECT cols from vars) LIMIT 20;

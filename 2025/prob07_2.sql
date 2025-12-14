CREATE TABLE "input" (v TEXT, n INTEGER PRIMARY KEY);
.import data07.txt input
SELECT * FROM input;


CREATE TABLE vars (rows INTEGER, cols INTEGER);
INSERT INTO vars VALUES (
  (select count(*) from input),
  (select length(v) from input where n=1)
  );

WITH RECURSIVE output(prev, cur, n, x, total) as (
  -- input.v is the current row of the input data
  -- output.prev is the previous row of the output data
  -- output.cur is the current row of the output data, built up to position x-1
  -- output.n is the completed line
  --
  SELECT
    replace(replace(input.v, '.', format("%14d",0)), 'S', format("%14d",1)),
    '', 1, 1, 0
    FROM input WHERE n=1
  UNION ALL
  SELECT
    IF(x = cols+1, output.cur, output.prev),
    CONCAT(if(x = cols+1, '', output.cur),
        -- compute the next number of the current line
        IF(
          x = cols + 1,
          '',

          -- if we are on ^, draw it
          ('^' is SUBSTR(input.v, x, 1)),
          ' ^^^^^^^^^^^^^',

          --if last one was ^^, it's 0
          (' ^^^^^^^^^^^^^' is SUBSTR(output.prev, 8*(x-1)+1, 8)),
          format("%14d",0),

          -- otherwise, compute a sum
          format("%14d",
            IF('^' is SUBSTR(input.v, x-1, 1), SUBSTR(output.prev, 14*(x-2)+1, 14), 0) + -- left
            IF('^' is SUBSTR(input.v, x+1, 1), SUBSTR(output.prev, 14*(x)+1, 14), 0) + -- right
            SUBSTR(output.prev, 14*(x-1)+1, 14) -- above
          )
        )
      ),
    if(x = cols+1, output.n+1, output.n),
    if(x = cols+1, 1, x+1), -- x = x+1
    if(x = cols+1, 0, output.total + substr(output.prev, 14*(x-1)+1, 14))
    FROM input, output, vars
    WHERE input.n = output.n+1

)
SELECT concat(cur, ' -> ', total, ' paths') FROM output where x=(select cols from vars)+1;

-- 문제 : null 처리하기
-- 링크 : https://programmers.co.kr/learn/courses/30/lessons/59410?language=oracle

SELECT
    ANIMAL_TYPE
    ,nvl(NAME,'No name') AS "name"
    ,SEX_UPON_INTAKE
from animal_ins
order by ANIMAL_ID;
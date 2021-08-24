-- 문제 : 상위 n개 레코드
-- 링크 : https://programmers.co.kr/learn/courses/30/lessons/59405?language=oracle

SELECT NAME FROM (SELECT ANIMAL_ID,NAME,DATETIME FROM ANIMAL_INS ORDER BY DATETIME) WHERE ROWNUM=1;
-- 문제 : 동명의 동물 수 찾기
-- 링크 : https://programmers.co.kr/learn/courses/30/lessons/59041

SELECT NAME, COUNT(NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(NAME)>1 ORDER BY NAME;


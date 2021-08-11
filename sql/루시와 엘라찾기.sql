-- 문제 : 루시와 엘라찾기
-- 링크 : https://programmers.co.kr/learn/courses/30/lessons/59046?language=oracle

-- 루시 엘라 등등 조건에 있는 이름을 가진 동물
-- 동물ID순으로
-- 동물ID, 이름, 중성화여부를 검색
SELECT ANIMAL_ID,NAME,SEX_UPON_INTAKE 
FROM ANIMAL_INS 
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY 1;
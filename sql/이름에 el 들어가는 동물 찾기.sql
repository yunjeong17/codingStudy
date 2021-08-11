-- 문제 : 이름에 el 들어가는 동물 찾기
-- 링크 : https://programmers.co.kr/learn/courses/30/lessons/59047

-- 대소문자 구분없이 이름 검색
-- 타입 개
-- 동물ID와 이름을 조회
-- 이름순으로 
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS 
WHERE UPPER(NAME) LIKE UPPER('%el%') 
    AND ANIMAL_TYPE ='Dog' 
ORDER BY NAME;
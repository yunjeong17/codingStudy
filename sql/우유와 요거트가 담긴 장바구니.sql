-- 문제 : 우유와 요거트가 담긴 장바구니
-- 링크 : https://programmers.co.kr/learn/courses/30/lessons/62284?language=oracle

-- 코드를 입력하세요
SELECT DISTINCT A.CART_ID
FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME ='Milk') "A"
JOIN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME ='Yogurt') "B" 
ON A.CART_ID=B.CART_ID ORDER BY CART_ID;
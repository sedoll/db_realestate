-- 컬럼 타입 변경, text 타입으로는 기본키 설정 불가
ALTER TABLE complex modify name varchar(30);
ALTER TABLE complex modify address varchar(30);

-- 다중 기본키 설정
ALTER TABLE complex ADD PRIMARY KEY(address, name, floor);

-- 컬럼 타입 변경, text 타입으로는 기본키 설정 불가
ALTER TABLE apartment modify name varchar(30);
ALTER TABLE apartment modify address varchar(30);

-- 다중 기본키 설정
ALTER TABLE apartment ADD PRIMARY KEY(address, name, floor, area);

-- 외래키 삭제
alter table trade drop foreign key trade_ibfk_2;

-- 설정된 외래키값 확인
SHOW CREATE TABLE trade;

-- 다중 외래키 설정
ALTER TABLE apartment ADD FOREIGN KEY (address, name) REFERENCES complex(address, name);

-- 컬럼 타입 변경, text 타입으로는 기본키 설정 불가
ALTER TABLE trade modify name varchar(30);
ALTER TABLE trade modify address varchar(30);

-- 다중 외래키 설정
ALTER TABLE trade ADD FOREIGN KEY (address, name, floor, area) REFERENCES apartment(address, name, floor, area);

-- 조인 테스트
SELECT a.dong, a.address, a.name, a.year, b.deal, b.area, b.acount, a.station_area
	FROM complex a JOIN trade b
	ON a.address = b.address AND a.name = b.name
    WHERE station_area = '두정역'
    ORDER BY b.acount DESC
    LIMIT 10;
    
-- 뷰 생성
CREATE VIEW trade_view AS
SELECT a.dong, a.address, a.name, a.year, b.deal, b.area, b.acount, a.station_area
	FROM complex a JOIN trade b
	ON a.address = b.address AND a.name = b.name;
    
-- 뷰 데이터 테스트
SELECT count(*) FROM trade_view;

-- 매매 아파트 중에서 역세권인 경우
SELECT * FROM trade_view
	WHERE station_area != '';

SELECT count(*) FROM trade_view
	WHERE station_area != '';
    
-- 테이블 이름 변경
ALTER TABLE trade2 RENAME trade;

-- 테이블 컬럼 삭제
ALTER TABLE trade DROP sub_add;

-- 컬럼 타입 변경, text 타입으로는 기본키 설정 불가
ALTER TABLE rent modify name varchar(30);
ALTER TABLE rent modify address varchar(30);

-- 다중 외래키 설정
ALTER TABLE rent ADD FOREIGN KEY (address, name, floor, area) REFERENCES apartment(address, name, floor, area);

-- 뷰 생성
CREATE VIEW rent_view AS
SELECT a.dong, a.address, a.name, a.year, b.deal, b.area, b.acount, b.rent, a.station_area
	FROM complex a JOIN rent b
	ON a.address = b.address AND a.name = b.name;
    
-- 뷰 데이터 테스트
SELECT count(*) FROM rent_view;

-- 월세 아파트 중에서 역세권인 경우
SELECT * FROM rent_view
	WHERE station_area != ''
    ORDER BY acount DESC, rent DESC;
    
-- 컬럼 타입 변경, text 타입으로는 기본키 설정 불가
ALTER TABLE charter modify name varchar(30);
ALTER TABLE charter modify address varchar(30);

-- 다중 외래키 설정
ALTER TABLE charter ADD FOREIGN KEY (address, name, floor, area) REFERENCES apartment(address, name, floor, area);

-- 뷰 생성
CREATE VIEW charter_view AS
SELECT a.dong, a.address, a.name, a.year, b.deal, b.area, b.acount, a.station_area
	FROM complex a JOIN charter b
	ON a.address = b.address AND a.name = b.name;
    
-- 뷰 데이터 테스트
SELECT count(*) FROM charter_view;

-- 월세 아파트 중에서 역세권인 경우
SELECT * FROM charter_view
	WHERE station_area != '' AND acount <= 10000
    ORDER BY acount DESC;
    
-- 읍 지역 검색
SELECT * FROM trade_view
	WHERE dong LIKE '입장면%';
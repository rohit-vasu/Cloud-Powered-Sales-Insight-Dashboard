CREATE TABLE sales (
  order_id varchar PRIMARY KEY,
  date date,
  product_id varchar,
  product_name varchar,
  qty int,
  price numeric,
  region varchar,
  city varchar,
  revenue numeric
);

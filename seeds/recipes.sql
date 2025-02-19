DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name text,
  average_cooking_time int,
  rating int
);

INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Lasagna', 60, 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Spaghetti Carbonara', 30, 4);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Chicken Curry', 45, 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Beef Stew', 120, 4);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Vegetable Stir Fry', 20, 3);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Tacos', 25, 4);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Grilled Cheese Sandwich', 10, 3);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Caesar Salad', 15, 4);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Pancakes', 20, 5);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Chocolate Cake', 90, 5);
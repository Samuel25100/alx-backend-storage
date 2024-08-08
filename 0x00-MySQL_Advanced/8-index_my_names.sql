-- creates an index idx_name_first on the table names and the first letter of name
USE holberton;
CREATE INDEX firstLt ON names (name(1));

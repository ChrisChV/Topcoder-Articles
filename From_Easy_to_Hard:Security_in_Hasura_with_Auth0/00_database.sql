CREATE TABLE public.product(
    id SERIAL PRIMARY KEY,
    name text NOT NULL,
    bar_code text
);
 
CREATE TABLE public.store(
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);
 
CREATE TABLE public.price(
    id SERIAL PRIMARY KEY,
    id_product integer NOT NULL REFERENCES public.product(id),
    id_store integer NOT NULL REFERENCES public.store(id),
    price float NOT NULL
);
 
CREATE TABLE public.receipt(
    id SERIAL PRIMARY KEY,
    id_store integer NOT NULL REFERENCES public.store(id)
);
 
CREATE TABLE public.receipt_price(
    id_receipt integer NOT NULL REFERENCES public.receipt(id),
    id_price integer NOT NULL REFERENCES public.price(id)
);

CREATE TABLE public.employee(
    id SERIAL PRIMARY KEY,
    auth0_id text,
    name text,
    email text,
    id_store integer NOT NULL REFERENCES public.store(id)
);

CREATE TABLE public.role(
    id SERIAL PRIMARY KEY,
    text_id text NOT NULL
);

CREATE TABLE public.role_employee(
    id_employee integer NOT NULL REFERENCES public.employee(id),
    id_role integer NOT NULL REFERENCES public.role(id)
);

INSERT INTO public.role values
    (1,'trial'),
    (2,'owner'),
    (3,'cashier'),
    (4,'salesperson');

INSERT INTO public.product values
    (1,'chocolate bar','123456789'),
    (2,'bread','223344556'),
    (3,'milk','444444444'),
    (4,'orange juice','777734921'),
    (5,'water','123321453'),
    (6,'coca-cola','552839274');

INSERT INTO public.store values
    (1,'Luchito Store'),
    (2,'Chris Store');

INSERT INTO public.price values
    (1,1,1,2),
    (2,2,1,1),
    (3,1,2,1.5),
    (4,2,2,1);
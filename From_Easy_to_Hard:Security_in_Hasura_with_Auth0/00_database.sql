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
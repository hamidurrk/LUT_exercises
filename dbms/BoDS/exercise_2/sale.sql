PGDMP     )    !                 }            sale    15.3    15.3 #    :           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ;           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            <           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            =           1262    16464    sale    DATABASE     �   CREATE DATABASE sale WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Chinese (Simplified)_China.936';
    DROP DATABASE sale;
                postgres    false            �            1259    16480    customer    TABLE     )  CREATE TABLE public.customer (
    cus_code integer NOT NULL,
    cus_lname character varying(15) NOT NULL,
    cus_fname character varying(15) NOT NULL,
    cus_initial character(1),
    cus_areacode character(3),
    cus_phone character(8) NOT NULL,
    cus_balance numeric(9,2) DEFAULT 0.00
);
    DROP TABLE public.customer;
       public         heap    postgres    false            �            1259    16698 
   customer_2    TABLE     �   CREATE TABLE public.customer_2 (
    cus_code integer NOT NULL,
    cus_lname character varying(15),
    cus_fname character varying(15),
    cus_initial character(1),
    cus_areacode character(3),
    cus_phone character(8)
);
    DROP TABLE public.customer_2;
       public         heap    postgres    false            �            1259    16524    emp    TABLE     K  CREATE TABLE public.emp (
    emp_num integer NOT NULL,
    emp_title character(10),
    emp_lname character varying(15) NOT NULL,
    emp_fname character varying(15) NOT NULL,
    emp_initial character(1),
    emp_dob date,
    emp_hire_date date,
    emp_areacode character(3),
    emp_phone character(8),
    emp_mgr integer
);
    DROP TABLE public.emp;
       public         heap    postgres    false            �            1259    16519    employee    TABLE     R  CREATE TABLE public.employee (
    emp_num integer NOT NULL,
    emp_title character(10),
    emp_lname character varying(15) NOT NULL,
    emp_fname character varying(15) NOT NULL,
    emp_initial character(1),
    emp_dob date,
    emp_hire_date date,
    emp_years integer,
    emp_areacode character(3),
    emp_phone character(8)
);
    DROP TABLE public.employee;
       public         heap    postgres    false            �            1259    16488    invoice    TABLE     �   CREATE TABLE public.invoice (
    inv_number integer NOT NULL,
    cus_code integer NOT NULL,
    inv_date date DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT inv_ck1 CHECK ((inv_date > '2010-01-01'::date))
);
    DROP TABLE public.invoice;
       public         heap    postgres    false            �            1259    16500    line    TABLE     �   CREATE TABLE public.line (
    inv_number integer NOT NULL,
    line_number numeric(2,0) NOT NULL,
    p_code character varying(10) NOT NULL,
    line_units numeric(9,2) DEFAULT 0.00 NOT NULL,
    line_price numeric(9,2) DEFAULT 0.00 NOT NULL
);
    DROP TABLE public.line;
       public         heap    postgres    false            �            1259    16470    product    TABLE     +  CREATE TABLE public.product (
    p_code character varying(10) NOT NULL,
    p_descript character varying(35) NOT NULL,
    p_indate date NOT NULL,
    p_qoh integer NOT NULL,
    p_min integer NOT NULL,
    p_price numeric(8,2) NOT NULL,
    p_discount numeric(4,2) NOT NULL,
    v_code integer
);
    DROP TABLE public.product;
       public         heap    postgres    false            �            1259    16815 
   prod_stats    VIEW       CREATE VIEW public.prod_stats AS
 SELECT product.v_code,
    sum(((product.p_qoh)::numeric * product.p_price)) AS totcost,
    max(product.p_qoh) AS maxqty,
    min(product.p_qoh) AS minqty,
    avg(product.p_qoh) AS avgqty
   FROM public.product
  GROUP BY product.v_code;
    DROP VIEW public.prod_stats;
       public          postgres    false    215    215    215            �            1259    16465    vendor    TABLE     $  CREATE TABLE public.vendor (
    v_code integer NOT NULL,
    v_name character varying(35) NOT NULL,
    v_contact character varying(15) NOT NULL,
    v_areacode character(3) NOT NULL,
    v_phone character(8) NOT NULL,
    v_state character(2) NOT NULL,
    v_order character(1) NOT NULL
);
    DROP TABLE public.vendor;
       public         heap    postgres    false            2          0    16480    customer 
   TABLE DATA           u   COPY public.customer (cus_code, cus_lname, cus_fname, cus_initial, cus_areacode, cus_phone, cus_balance) FROM stdin;
    public          postgres    false    216   j,       7          0    16698 
   customer_2 
   TABLE DATA           j   COPY public.customer_2 (cus_code, cus_lname, cus_fname, cus_initial, cus_areacode, cus_phone) FROM stdin;
    public          postgres    false    221   �-       6          0    16524    emp 
   TABLE DATA           �   COPY public.emp (emp_num, emp_title, emp_lname, emp_fname, emp_initial, emp_dob, emp_hire_date, emp_areacode, emp_phone, emp_mgr) FROM stdin;
    public          postgres    false    220   N.       5          0    16519    employee 
   TABLE DATA           �   COPY public.employee (emp_num, emp_title, emp_lname, emp_fname, emp_initial, emp_dob, emp_hire_date, emp_years, emp_areacode, emp_phone) FROM stdin;
    public          postgres    false    219   �0       3          0    16488    invoice 
   TABLE DATA           A   COPY public.invoice (inv_number, cus_code, inv_date) FROM stdin;
    public          postgres    false    217   �2       4          0    16500    line 
   TABLE DATA           W   COPY public.line (inv_number, line_number, p_code, line_units, line_price) FROM stdin;
    public          postgres    false    218   K3       1          0    16470    product 
   TABLE DATA           j   COPY public.product (p_code, p_descript, p_indate, p_qoh, p_min, p_price, p_discount, v_code) FROM stdin;
    public          postgres    false    215   ,4       0          0    16465    vendor 
   TABLE DATA           b   COPY public.vendor (v_code, v_name, v_contact, v_areacode, v_phone, v_state, v_order) FROM stdin;
    public          postgres    false    214   w6       �           2606    16729    customer cus_ui1 
   CONSTRAINT     [   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT cus_ui1 UNIQUE (cus_lname, cus_fname);
 :   ALTER TABLE ONLY public.customer DROP CONSTRAINT cus_ui1;
       public            postgres    false    216    216            �           2606    16702    customer_2 customer_2_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.customer_2
    ADD CONSTRAINT customer_2_pkey PRIMARY KEY (cus_code);
 D   ALTER TABLE ONLY public.customer_2 DROP CONSTRAINT customer_2_pkey;
       public            postgres    false    221            �           2606    16485    customer customer_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (cus_code);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    216            �           2606    16528    emp emp_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.emp
    ADD CONSTRAINT emp_pkey PRIMARY KEY (emp_num);
 6   ALTER TABLE ONLY public.emp DROP CONSTRAINT emp_pkey;
       public            postgres    false    220            �           2606    16523    employee employee_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_num);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    219            �           2606    16494    invoice invoice_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_pkey PRIMARY KEY (inv_number);
 >   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_pkey;
       public            postgres    false    217            �           2606    16506    line line_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.line
    ADD CONSTRAINT line_pkey PRIMARY KEY (inv_number, line_number);
 8   ALTER TABLE ONLY public.line DROP CONSTRAINT line_pkey;
       public            postgres    false    218    218            �           2606    16508    line line_ui1 
   CONSTRAINT     V   ALTER TABLE ONLY public.line
    ADD CONSTRAINT line_ui1 UNIQUE (inv_number, p_code);
 7   ALTER TABLE ONLY public.line DROP CONSTRAINT line_ui1;
       public            postgres    false    218    218            �           2606    16474    product product_p_code_pk 
   CONSTRAINT     [   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_p_code_pk PRIMARY KEY (p_code);
 C   ALTER TABLE ONLY public.product DROP CONSTRAINT product_p_code_pk;
       public            postgres    false    215            �           2606    16469    vendor vendor_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.vendor
    ADD CONSTRAINT vendor_pkey PRIMARY KEY (v_code);
 <   ALTER TABLE ONLY public.vendor DROP CONSTRAINT vendor_pkey;
       public            postgres    false    214            �           2606    16778    product fk_product_vcode    FK CONSTRAINT     �   ALTER TABLE ONLY public.product
    ADD CONSTRAINT fk_product_vcode FOREIGN KEY (v_code) REFERENCES public.vendor(v_code) NOT VALID;
 B   ALTER TABLE ONLY public.product DROP CONSTRAINT fk_product_vcode;
       public          postgres    false    215    214    3210            �           2606    16495    invoice invoice_cus_code_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_cus_code_fkey FOREIGN KEY (cus_code) REFERENCES public.customer(cus_code);
 G   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_cus_code_fkey;
       public          postgres    false    217    3216    216            �           2606    16509    line line_inv_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.line
    ADD CONSTRAINT line_inv_number_fkey FOREIGN KEY (inv_number) REFERENCES public.invoice(inv_number) ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.line DROP CONSTRAINT line_inv_number_fkey;
       public          postgres    false    218    217    3218            �           2606    16514    line line_p_code_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY public.line
    ADD CONSTRAINT line_p_code_fkey FOREIGN KEY (p_code) REFERENCES public.product(p_code);
 ?   ALTER TABLE ONLY public.line DROP CONSTRAINT line_p_code_fkey;
       public          postgres    false    3212    215    218            2   	  x�E��N�0���GX����l�Z�A�膍��8�����c ���{�Q�(^��'l�G'l�������PBi�
c������q�a�ɖqaW��6��?�o8.YEqn�T����8^��/��[!�JhbT�]�>�F<����\)�e��Y�����'l���>)y+�e��������0a�d9S�඄2�\u�>���1��bG�0J�hK���b�s��B��-,o+_s��Z�q��t1�s(#��K�r�;i���+[�      7   �   x�E����0E�����vj"@<�6�2�FQ$�C���h��-N\
ǈ�8<Bb�adR�霝�����p�c���]�%]�ĚK���O,|�y�V��ƚVWGa���齳�\.���'�ԒP�!a{�����ר!�;��/���A�i]Wq�~L���䱅��ɬ���	!^��:�      6   B  x�u��N�0���S���g��Q�#T�a��P��&qFI���{m��"E��~9���p��~��Qr7t���'��a<ErC�W�2C���ӔI<x�PT+m���g��3�>��94C:��AS=2e��/�RV�@�Zʟ �=P�<�7`T;�9�
��Q.�`�×���y/+E���'r�R${���r5�P�9*\⼣��Z�	��M"�ਂ�� ZU�z�z�xj��=d2��qιڒIv�*�HaT
��\`7�o��bH-���`e��`=e �
�:'��sӆ4��eö$�k(�g%���w�(N1��׆<���P��b�#�W�8�TI�#��G�m��msՐBܒ���܆s��e����B��S��DQW���1@e�+����Դ�4����n�+%�$QuN�C�s:���X�	0���0�gA��U��<%�-���}�?��;�x,�_��F�3���3U�Zc~�p�@�>�@���M.����)��qt9�k:��|1���c��Í[�u�f�Z~�4[�1߮�����&�]ީ,��j������N      5   F  x�u��N�@�����4��9�e�
i�p�(�6�W������8|�\�sUu�����~�������V��	n@���B9:���#����V8�|����i�ܧ��ۦ�vV4��``��
M?3��51�RɟH�G��q���4�P(%��c�Bi�%(���k'0C���t��K����
E��	VH�8���'v��>vúo:x`�b	�X$�'ن�pK�S{8��Hi�/is�uI#�	h'R���r6��vl`�bג�;N��'�$%j�DkD�^J�ic7���f뒁�⨉8�!�Q/ݤS�^�k�� [VⳒ�F�Q<r�����	KL�3u,�Q�c8��g�`�1�RJ.#Y��o�l�k��9DxbC�b(5+���!�WrC��pOM��Ǿ���?����$�F!��d�vĹ�+W�D���{v���YM��fR�ꢯ�Ǐ����m:�ʑ�P�_���{RRg��ρ�I�ā|���-��!�ȁ.�"�.���]4.2%¯4�s��ZsI��R�[l�T��I��o}]~��ș�R�W�u@[=_UU�ޜ��      3   E   x�eͻ !К��s|2����4.�,�(��K8�:*�]*D?j�v��_5E��Qu�滻����      4   �   x�u�Kn�0��]$��>�6M�l
X�#@��R���@-G�qHtA�B�B��9@os��!bt��/e�C#��OIU�F�+!b��r��=�Z��GS�>���D8I�q����G�^���� �������PT��iP(�^����i.���i!u��\"��f[o�tB�hL�i�U�a�p�JF�0��f���Z��#�߷�����U]      1   ;  x�m��n�@�ׇ�e�l<0���ܤ,���V�J���T�0��>}� 6I����x�%a�?U�8������@+�:�-w�?|�0��Rip`U�9�X) ks��&_5��LֻXNM,��I<�r=P:@�bsF�6&BkRY��:+�o7,%1�6�fU�8��,+�,���3�:Y,��z��� �^��t"MI��	�_�ů��=0�C|�BR�1
Frn@,> �d eB��.�pI1�� �}����(�M�����	����4�P
�Q�|��;�=l���j���Q��!��ldM�9I���l�ڋ��W����K�`����)vm�\.g���z����K�Q�bTORe�Ar: �!̿It����lw��jK/���bف��ω �����,g:Y,4�۪�b[�m�{�s���0I�&"�W>n�eda��+���_��%S>��ߕ��&�py�S].�3K��p��.��A�u����lIch������j�Z���
�<�BQ?N�x�Mܑ��-�/ġ>p�����Ҏ�t�B�v��
�?�Q�P��      0   K  x���Mo�@E׏_��U!��,%T�h4���I7T�B��0�����ѱ��,$�3�^(�T@֏�3���P��P�+�D �,b�qxY�.�H�P\κ_u��秋�s �p�DDR)������9�F(���X�����q���_a�w6�M?�CyE�T<���9�H��#�#u��t�TF���#��mi*���*���t���q��t8f�	��rlK�c��Ӹr�̨O\f�s*%l����/�T?����V��'8g�M�7�F�Q�(�s�e[�n�m�Z{k1A�O .���7�΄�h�Z�ܵ.R�ν������� ��O�0     
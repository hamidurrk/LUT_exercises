PGDMP                          }            stu    15.3    15.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            
           1262    66693    stu    DATABASE     �   CREATE DATABASE stu WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Chinese (Simplified)_China.936';
    DROP DATABASE stu;
                postgres    false            �            1259    66723    course    TABLE     �   CREATE TABLE public.course (
    cno character(4) NOT NULL,
    cname character varying(50) NOT NULL,
    cpno character(4),
    credit smallint
);
    DROP TABLE public.course;
       public         heap    postgres    false            �            1259    66726    sc    TABLE     m   CREATE TABLE public.sc (
    sno character(8) NOT NULL,
    cno character(4) NOT NULL,
    grade smallint
);
    DROP TABLE public.sc;
       public         heap    postgres    false            �            1259    66729    student    TABLE     �   CREATE TABLE public.student (
    sno character(8) NOT NULL,
    sname character varying(10) NOT NULL,
    sage integer,
    sgender character(1),
    sdept character varying(10)
);
    DROP TABLE public.student;
       public         heap    postgres    false                      0    66723    course 
   TABLE DATA           :   COPY public.course (cno, cname, cpno, credit) FROM stdin;
    public          postgres    false    214   	                 0    66726    sc 
   TABLE DATA           -   COPY public.sc (sno, cno, grade) FROM stdin;
    public          postgres    false    215   �                 0    66729    student 
   TABLE DATA           C   COPY public.student (sno, sname, sage, sgender, sdept) FROM stdin;
    public          postgres    false    216   �       o           2606    66733    sc PK_sc 
   CONSTRAINT     N   ALTER TABLE ONLY public.sc
    ADD CONSTRAINT "PK_sc" PRIMARY KEY (sno, cno);
 4   ALTER TABLE ONLY public.sc DROP CONSTRAINT "PK_sc";
       public            postgres    false    215    215            m           2606    66735    course course_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (cno);
 <   ALTER TABLE ONLY public.course DROP CONSTRAINT course_pkey;
       public            postgres    false    214            q           2606    66737    student student_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (sno);
 >   ALTER TABLE ONLY public.student DROP CONSTRAINT student_pkey;
       public            postgres    false    216            r           2606    66738 	   sc FK_cno    FK CONSTRAINT     r   ALTER TABLE ONLY public.sc
    ADD CONSTRAINT "FK_cno" FOREIGN KEY (cno) REFERENCES public.course(cno) NOT VALID;
 5   ALTER TABLE ONLY public.sc DROP CONSTRAINT "FK_cno";
       public          postgres    false    3181    215    214            s           2606    66743 	   sc FK_sno    FK CONSTRAINT     s   ALTER TABLE ONLY public.sc
    ADD CONSTRAINT "FK_sno" FOREIGN KEY (sno) REFERENCES public.student(sno) NOT VALID;
 5   ALTER TABLE ONLY public.sc DROP CONSTRAINT "FK_sno";
       public          postgres    false    216    215    3185               �   x�=���0Dg�+�HmC� X�(]��`
C�*q���L'���5DV�sؗ�`[d`}�����+��zvO
���OTY��!S�JȦ�f_h�[�)�Ш!YMA�Ps��Z��cN����Hvs�Yj��i��_w�/C         6   x�3202 CNCNK#.#��H��&`�4@�U �@,�b���� �?�         _   x�3202 CN��R��<N#N7N�`.#��PF!2?/��В�I�%�,3"��6��N,I�4� ��	V
�)@�Ɯ1~@����� S�g     
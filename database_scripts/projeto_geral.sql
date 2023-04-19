-- Table: public.projeto_geral

-- DROP TABLE IF EXISTS public.projeto_geral;

CREATE TABLE IF NOT EXISTS public.projeto_geral
(
    id integer NOT NULL,
    situacao character varying(255) COLLATE pg_catalog."default",
    estado character varying(255) COLLATE pg_catalog."default",
    atividade character varying(255) COLLATE pg_catalog."default",
    titulo character varying(1000) COLLATE pg_catalog."default",
    idtarefaassociada integer,
    titulotarefaassociada character varying(500) COLLATE pg_catalog."default",
    dtprevisaoinicio character varying(50) COLLATE pg_catalog."default",
    dtprevisaofim character varying(50) COLLATE pg_catalog."default",
    dtrealizadainicio character varying(50) COLLATE pg_catalog."default",
    dtrealizadafim character varying(50) COLLATE pg_catalog."default",
    prioridade character varying(255) COLLATE pg_catalog."default",
    assunto character varying(5000) COLLATE pg_catalog."default",
    idatividade integer,
    descricaoatividade character varying(5000) COLLATE pg_catalog."default",
    idsituacao integer,
    dataultimamodificacao character varying(50) COLLATE pg_catalog."default",
    autorultimamodificacao character varying(500) COLLATE pg_catalog."default",
    numdenuncia character varying(5000) COLLATE pg_catalog."default",
    detalhamento character varying(5000) COLLATE pg_catalog."default",
    localidadesplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    proponenteplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    etapaplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    processt character varying(5000) COLLATE pg_catalog."default",
    responsavelplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    origemdemanda character varying(5000) COLLATE pg_catalog."default",
    links character varying(5000) COLLATE pg_catalog."default",
    anexoplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    processoplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    resultadosesperados character varying(5000) COLLATE pg_catalog."default",
    objetoscgemg character varying(5000) COLLATE pg_catalog."default",
    duracaomeses integer,
    recursofinanceiro character varying(5000) COLLATE pg_catalog."default",
    envolvidosplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    homemhora integer,
    gerentesplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    supervisores character varying(5000) COLLATE pg_catalog."default",
    objetivoplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    tipoplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamento character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT projeto_geral_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.projeto_geral
    OWNER to m1478769;

REVOKE ALL ON TABLE public.projeto_geral FROM x09972752;

GRANT SELECT ON TABLE public.projeto_geral TO m13365929;

GRANT ALL ON TABLE public.projeto_geral TO m1478769;

GRANT SELECT ON TABLE public.projeto_geral TO m7532203;

GRANT SELECT ON TABLE public.projeto_geral TO x09972752;

-- Table: public.atividade_continuada

-- DROP TABLE IF EXISTS public.atividade_continuada;

CREATE TABLE IF NOT EXISTS public.atividade_continuada
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
    detalhamento character varying(5000) COLLATE pg_catalog."default",
    propopenente character varying(5000) COLLATE pg_catalog."default",
    etapaplano character varying(5000) COLLATE pg_catalog."default",
    responsavel character varying(5000) COLLATE pg_catalog."default",
    processoplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    localidade character varying(5000) COLLATE pg_catalog."default",
    links character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    resultados character varying(5000) COLLATE pg_catalog."default",
    recurso character varying(5000) COLLATE pg_catalog."default",
    envolvidos character varying(5000) COLLATE pg_catalog."default",
    homemhora integer,
    gerentes character varying(5000) COLLATE pg_catalog."default",
    supervisorplanotrabalho character varying(5000) COLLATE pg_catalog."default",
    tipoplano character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT atividade_continuada_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.atividade_continuada
    OWNER to m1478769;

REVOKE ALL ON TABLE public.atividade_continuada FROM x09972752;

GRANT SELECT ON TABLE public.atividade_continuada TO m13365929;

GRANT ALL ON TABLE public.atividade_continuada TO m1478769;

GRANT SELECT ON TABLE public.atividade_continuada TO m7532203;

GRANT SELECT ON TABLE public.atividade_continuada TO x09972752;

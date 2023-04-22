-- Table: public.comunicacao_auditoria

-- DROP TABLE IF EXISTS public.beneficios;

CREATE TABLE IF NOT EXISTS public.beneficios
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
    beneficioavulso int,
    descricaobeneficio character varying(50000) COLLATE pg_catalog."default",
    valorbruto character varying(5000) COLLATE pg_catalog."default",
    descricaocusto character varying(50000) COLLATE pg_catalog."default",
    dimensaorepercussao character varying(50000) COLLATE pg_catalog."default",
    valorcusto character varying(5000) COLLATE pg_catalog."default",
    unidadesenvolvidas character varying(5000) COLLATE pg_catalog."default",
    unidadegestora character varying(5000) COLLATE pg_catalog."default",
    anexosbeneficio character varying(10485760) COLLATE pg_catalog."default",
    providenciabeneficio character varying(50000) COLLATE pg_catalog."default",
    dimenssaobeneficio character varying(5000) COLLATE pg_catalog."default",
    parcelasbeneficio character varying(5000) COLLATE pg_catalog."default",
    titulofundamento character varying(50000) COLLATE pg_catalog."default",
    textofundamentobeneficio character varying(10485760) COLLATE pg_catalog."default",
	valorliquido character varying(5000) COLLATE pg_catalog."default",
	classebeneficio character varying(5000) COLLATE pg_catalog."default",
	tipobeneficio character varying(5000) COLLATE pg_catalog."default",
	tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
	unidadeproponente character varying(5000) COLLATE pg_catalog."default",
	anofatogeradorbeneficio character varying(500) COLLATE pg_catalog."default",
	situacaoanateriorbeneficio character varying(5000) COLLATE pg_catalog."default",
	anoimplementacaobeneficio character varying(500) COLLATE pg_catalog."default",
	repercussaobeneficio character varying(5000) COLLATE pg_catalog."default",
	classebf character varying(5000) COLLATE pg_catalog."default",
	nivelbeneficio character varying(5000) COLLATE pg_catalog."default",
	classebnf character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT beneficios_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.beneficios
    OWNER to m1478769;

REVOKE ALL ON TABLE public.beneficios FROM x09972752;

GRANT SELECT ON TABLE public.beneficios TO m13365929;

GRANT ALL ON TABLE public.beneficios TO m1478769;

GRANT SELECT ON TABLE public.beneficios TO m7532203;

GRANT SELECT ON TABLE public.beneficios TO x09972752;
